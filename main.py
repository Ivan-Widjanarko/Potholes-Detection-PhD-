import os
from flask import Flask, jsonify, flash
#from flask.wrappers import Request
# from flaskext.mysql import MySQL
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

@app.route('/user/login/<string:email>/<string:password>')
def login(email, password):
    conn = conf()
    with conn.cursor() as cursor:
        query = "SELECT id FROM user WHERE email='{}' AND password='{}'".format(email, password)
        cursor.execute(query)
        results = cursor.fetchall()
        conn.close()
        if results == 1:
            return "Anda berhasil login"
        else:
            return "email belum terdaftar"
    


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
@app.route('/user/register/<string:email>/<string:password>/<int:device_id>', methods=['POST'])
def register_user(email, password, device_id):
    try:
        try:
            conn = conf()
            with conn.cursor() as cursor:
                sql = "INSERT INTO user (email, password, device_id) VALUES('{}', '{}', {})".format(email, password, device_id) #masukin ke dalam table database
                cursor.execute(sql)
            conn.commit()
            conn.close()

            return "User added"

        except pymysql.err.IntegrityError as e:
            conn.rollback()
            conn.close()
            return e.args[1]

    except Exception as e:
        return e.args[1]






#post_dataimage('/')

#get_dataimage('')

#post_data('/data/send/<int:device_id>/<float:location>/<string:classification>/<string:url>/<string:time>')
@app.route('/data/post/<int:device_id>/<float:latitude>/<float:longitude>/<string:hole_type>/<string:url_img>', methods=['POST'])
def post_data(device_id, latitude, longitude, hole_type, url_img):
    conn = conf()
    with conn.cursor() as cursor:
        sql = """
        INSERT INTO data (user_id, latitude, longitude, hole_type, url_img)
	    SELECT id, {}, {}, '{}', '{}' FROM user
	    WHERE device_id = {}""".format(latitude, longitude, hole_type, url_img, device_id) #masukin ke dalam table database
        cursor.execute(sql)
    conn.commit()
    conn.close()

    return "Data added"


#get_data('/data/get/<int:device_id>')
@app.route('/data/get/<int:user_id>')
def get_data(user_id):
    conn = conf()
    with conn.cursor() as cursor:
        query = """
        SELECT latitude, longitude, hole_type, url_img FROM data
	        WHERE user_id={}
        """.format(user_id)
        cursor.execute(query)
        results = cursor.fetchall()
    conn.close()
    return "Data ditemukan"



if __name__ == '__main__':
    app.run()
