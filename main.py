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
            return jsonify(status="bad",message="Wrong Email or Password")
    
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
            items=[]
            for x in range(len(results)):
                data_info = {'id':results[x][0],'device_id':results[x][1],'latitude':results[x][2],'longitude':results[x][3],'hole_type':results[x][4],'url_img':results[x][5]}
                items.append(data_info)
            messages = {"status":"OK", "message": "data found.", "data_info": items}
            return jsonify(messages)
        else:
            return jsonify(status="bad", message="data tidak ditemukan")
    

if __name__ == '__main__':
    app.run()
