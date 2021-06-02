import os
from flask import Flask, jsonify, flash
#from flask.wrappers import Request
# from flaskext.mysql import MySQL
import pymysql


app = Flask(__name__)
#mysql = MySQL()
# data = []

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


# def sql_to_json(results):
#     keys = []
#     for data in results:
#         keys.append(data[0])
#     key_number = len(keys)

#     json_data = []
#     for row in results:
#         item = dict()
#         for q in range(key_number):
#             item[keys[q]] = row[q]
#         json_data.append(item)

#     return json_data


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
        query = "SELECT * FROM user WHERE email='{}' AND password='{}'".format(email, password)
        cursor.execute(query)
        results = cursor.fetchall()
        conn.close()
        if results:
            user_info = {'id':results[0][0],'email':results[0][1],'password':results[0][2],'device_id':results[0][3]}
            messages = {"status": "OK", "message":  "Login Success.", "user_info": user_info}
            return jsonify(messages)
        else:
            return jsonify(status="bad",message="Failed to login")
    
# for user in data.query.filter(User.id.in_(ids)).all():
#     if current_user.id == user.id:
#         continue

#     if user.delete():
#         data.append(
#             {
#                 "id": user.id,
#                 "type": "delete",
#                 "reverse": False,
#                 "reverse_name": None,
#                 "reverse_url": None
#             }
#         )


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
            return jsonify(status="OK", message="Account has been registered!")

        except pymysql.err.IntegrityError as e:
            conn.rollback()
            conn.close()
            return jsonify(status="bad", message="Email has been registered. Please use another email!")

    except Exception as e:
        return jsonify(status="err", message="Failed to registered")



#post_dataimage('/report/')
# @app.route('/report/')
# def raspi_to_sql():
#     try:
#         try:
#             conn = conf()
#             with conn.cursor() as cursor:
#                 sql = "INSERT INTO user (email, password, device_id) VALUES('{}', '{}', {})".format(email, password, device_id) #masukin ke dalam table database
#                 cursor.execute(sql)
#             conn.commit()
#             conn.close()
#             return jsonify(message="Account has been registered!")

#         except pymysql.err.IntegrityError as e:
#             conn.rollback()
#             conn.close()
#             return jsonify(message="Email has been registered. Please use another email!")

#     except Exception as e:
#         return jsonify(message="Failed to registered")

#get_dataimage('/')


#post_data('/data/send/<int:device_id>/<float:location>/<string:classification>/<string:url>/<string:time>')
@app.route('/data/post/<int:device_id>/<float:latitude>/<float:longitude>/<string:hole_type>/<string:url_img>', methods=['POST'])
def post_data(device_id, latitude, longitude, hole_type, url_img):
    try:
        try:
            conn = conf()
            with conn.cursor() as cursor:
                # sql = """
                # INSERT INTO data (device_id, latitude, longitude, hole_type, url_img)
                # SELECT id, {}, {}, '{}', '{}' FROM user
                # WHERE device_id = {}""".format(latitude, longitude, hole_type, url_img, device_id) #masukin ke dalam table database
                query = f"INSERT INTO data (device_id, latitude, longitude, hole_type, url_img) VALUES({device_id}, {latitude}, {longitude}, '{hole_type}', '{url_img}')" #masukin ke dalam table database
                cursor.execute(query)
            conn.commit()
            conn.close()
            return jsonify(message="Data added")
        except pymysql.err.IntegrityError as e:
            conn.rollback()
            conn.close()
            return jsonify(message="Failed to upload data")
    except Exception as e:
        return jsonify(message="Failed to upload data")


#get_data('/data/get/<int:device_id>')
@app.route('/data/get/<int:device_id>')
def get_data(device_id):
    conn = conf()
    with conn.cursor() as cursor:
        # query = """
        # SELECT latitude, longitude, hole_type, url_img FROM data
	    #     WHERE user_id={}
        # """.format(user_id)
        query = f"SELECT * FROM data WHERE device_id={device_id}"
        cursor.execute(query)
        results = cursor.fetchall()
        conn.close()
        if results:
            # items=[]
            for x in range(len(results)):
                data_info = {'id':results[x][0],'device_id':results[x][1],'latitude':results[x][2],'longitude':results[x][3],'hole_type':results[x][4],'url_img':results[x][5]}
                messages = {"status":"OK", "message": "data found.", "data_info": [data_info]}
            return jsonify(messages)
        else:
            return jsonify(status="bad", message="data tidak ditemukan")
    

if __name__ == '__main__':
    app.run()
