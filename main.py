import os
from flask import Flask, jsonify, flash
#from flask.wrappers import Request
#from flaskext.mysql import MySQL
import pymysql


app = Flask(__name__)
#mysql = MySQL()

#MySQL configuration
db_user = os.environ.get('CLOUD_SQL_USERNAME')
db_password = os.environ.get('CLOUD_SQL_PASSWORD')
db_name = os.environ.get('CLOUD_SQL_DATABASE_NAME')
db_connection_name = os.environ.get('CLOUD_SQL_CONNECTION_NAME')

def conf():
    # When deployed to App Engine, the `GAE_ENV` environment variable will be
    # set to `standard`
    try:
        if os.environ.get('GAE_ENV') == 'standard':
            # If deployed, use the local socket interface for accessing Cloud SQL
            unix_socket = '/cloudsql/{}'.format(db_connection_name)
            cnx = pymysql.connect(user=db_user, password=db_password,
                              unix_socket=unix_socket, db=db_name)
        else:
            # If running locally, use the TCP connections instead
            # Set up Cloud SQL Proxy (cloud.google.com/sql/docs/mysql/sql-proxy)
            # so that your application can use 127.0.0.1:3306 to connect to your
            # Cloud SQL instance
            host = '127.0.0.1'
            cnx = pymysql.connect(user=db_user, password=db_password,
                              host=host, db=db_name)
        return cnx
    
    except pymysql.MySQLError as e:
        print(e)

@app.route('/')
def main():
    return 'halo'

# #get_user('/users/<string:email>/<string:password>')
# @app.route('/users/<string:email>/<string:password>')
# def get_user(email, password):
#     conn = main()
#     with conn.cursor() as cursor:
#         result = "SELECT * FROM data_table WHERE email=%s AND password=%s" #ngambil email dan password dari tabel database
#         val = (email, password)
#         cursor.execute(result, val)
#         user = cursor.fetchall()
#         if result > 0:
#             getUser = jsonify(user)
#         else:
#             getUser = 'Email kamu belum terdaftar'
#     conn.close()
#     return getUser

@app.route('/testing')
def testing():
    conn = conf()
    with conn.cursor() as cursor:
        query = "SELECT * FROM user;"
        cursor.execute(query)
        results = cursor.fetchall()
        for row in results:
            email = row[1]
    conn.close()
    return email

# #post_user('/users/register/<string:email>/<string:password>/<int:device_id>')
# @app.route('/users/register/<string:email>/<string:password>/<int:device_id>', methods=['POST'])
# def post_user(email, password, device_id):
#     conn = main()
#     with conn.cursor() as cursor:
#         sql = "INSERT INTO data_table (email, password, device_id) VALUES(%s, %s, %s)"
#         val = (email, password, device_id)
#         cursor.execute(sql, val) #masukin ke dalam table database
#     conn.commit()
#     conn.close()
#     flash('Email kamu berhasil terdaftar')
@app.route('/post/<string:email>/<string:password>/<int:device_id>', methods=['POST'])
def post(email, password, device_id):
    try:
        conn = conf()
        with conn.cursor() as cursor:
            sql = "INSERT INTO user (email, password, device_id) VALUES('{}', '{}', {})".format(email, password, device_id) #masukin ke dalam table database
            cursor.execute(sql)
        conn.commit()
        conn.close()

        return "User added"

    except pymysql.Error as e:
        code, message = e.args
        return "{}, {}".format(code, message)


if __name__ == '__main__':
    app.run()

#post_dataimage('/')

#get_dataimage('')

#post_data('/data/send/<int:device_id>/<float:location>/<string:classification>/<string:url>/<string:time>')

#get_data('/data/get/<int:device_id>')
