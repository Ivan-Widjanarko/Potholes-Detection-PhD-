import os
from flask import Flask, jsonify, flash
import pymysql
# from gcloud import storage
# from oauth2client.service_account import ServiceAccountCredentials


app = Flask(__name__)

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

#main route
@app.route('/')
def main():
    return 'halo'

#get raspi
@app.route('/raspi/credential')
def connect_to_gstorage():
    return jsonify(
        type="service_account",
        project_id= "pothole-detection-315702",
        private_key_id= "a1d3aef5ad5975f75f359657328273e159ee6e4e",
        private_key= "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDWIRJGOR6q3SB8\ntoiTURguGyNP9567t0pTvcO5QMVVpDDi3et5hnZXhC07OtdjDzaN3gYbr9JPXi6P\nMXtsWBjcC1daETDNJrEkOv/ljFkGo8PKPXclSrHjjDPC7fEaFCScHoLXwKBJUvZG\nrCPBcRRpVKl/45tRm7WQPRJVJrVJ1D7UZAj1wgBFtNbDkivuJsIMC4HdgtDtWUP7\nz/mkXYXu61qwFUGjRBTGui0Dw+ui0ag8aY9BbyPcRs+cl6V+4b0dbpdPt9duwraA\n66Pqk7yVpLBdCShXvs1ow/tZfbNd4sKiA9X08WdCGPFD4Kb1Z/kvKMzwNQVjv12C\n7dD0aPSRAgMBAAECggEAAVkqoPU8c4hPlg7ILrVKA7BOuUguiwa3xG3jd50oIPFB\nuuFO2ZsLz7fuA6YhM7x6yXXmb/IxeX0hqevT18t44e8oWPwsDylOiuiG3U5+7lhw\nToEIk7GJYTdsHq7E3+HUloRn/9fJ/+wyeiDHW4Z3bG+zXtzIs5YuvykYnnSkm5cO\n7ZvZ6RErvw06BU2p+muNBoD5tVnjFeb/t6qNdNiubeAtuetng5VIA6VcTjKFK1fs\nJas5QniO8KRrJiP7T0SZZZGGlxjN2lz06E+WPYSXKSkXCW0ojMKTBBQtwPeHvRtl\nqFJa67Rr8V0ODKI/fcKtdMcyejodzPm3i1I1Y43M4QKBgQDyYcDen8DmCU/kSvZ6\nLcSFnvIopl4Yi0Z0HDJlf9EC1Txu+KgUHrROkB5aA0oXhzjnJwkLxm1opevruAa2\nivSE2G3Qgf2+GabbsHu/cw4T/wikkXadjxlVwUqFAsCUoedfzETTjDUOYMbqGP3w\n2IrFy8e0W3p7N1x8IJ360Bu+bQKBgQDiKPOyPpZPcsusqZrmOQZalTb+cOFzcpBc\nEyTyZWTYXSG6BvUuJVxT6AEt2RaNDu0GZz2ce/JhjMaMSFzARXTfP3fJT/a31ToV\nlP1ntd6RlTaZVFfUcyrGp498PshDJZCfzeFkY1qMtbCvrwsp6Dxk8NQd5qknEPns\nu8vhdJ+oNQKBgQCP+ZMIapq5yhRDxmeMgb03pgewL8q7B5gNBmbFNdxgs2tXe6rT\ncL2n4SG2VDfhq/gYDm7oKLD6tXxjI4gRTI8cjjcE4QJptnEQFFAdk+lr5VUr9CAi\nTUs+TjfGtLDSWS3IEN1dT+6AIOpnSfsl4mrkPTzeHGyv3l24eeN9hbrFLQKBgB83\nc9vIk8rHl6Fvj7fzaxMZwYuBXT0oNRDge5sRr8fFoyAgUbta4NGcFn2Tl29E/iaC\nHZj56szYN5epbVQEwksGYaxh4zYgsnHELO4hxmTl6bFkWPM0KlVdT4rgx5etGbdV\nHaVTqW3+rjKxwKK6MYvlSgIOko6X40dv7IZkKJ15AoGAdVxVYUc5Xe5RerTje7Wn\n3Adg+2imq7oYCHpkjWTKeFed/zDT4UKJQKd/FQIwDJXwZfjjNm/EcMSR3ZGpIwD2\ny5/RPKf8yNlKtJZ3Oe2gplxr5sthNQaD2++sjLmRTIkCmC3rmR/+PQhPmejuX0YZ\n1OA1XbEiYqzQm9elDf8y60o=\n-----END PRIVATE KEY-----\n",
        client_email= "google-cloud-storage@pothole-detection-315702.iam.gserviceaccount.com",
        client_id= "103162368217828849366",
        auth_uri= "https://accounts.google.com/o/oauth2/auth",
        token_uri= "https://oauth2.googleapis.com/token",
        auth_provider_x509_cert_url= "https://www.googleapis.com/oauth2/v1/certs",
        client_x509_cert_url= "https://www.googleapis.com/robot/v1/metadata/x509/google-cloud-storage%40pothole-detection-315702.iam.gserviceaccount.com"
    )

#user login
@app.route('/user/login/<string:email>/<string:password>')
def login(email, password):
    conn = conf()
    with conn.cursor() as cursor:
        query = f"SELECT * FROM user WHERE email='{email}' AND password='{password}'"
        cursor.execute(query)
        results = cursor.fetchall()
        conn.close()
        if results:
            user_info = {'id':results[0][0],'email':results[0][1],'password':results[0][2],'device_id':results[0][3], 'state':results[0][4]}
            messages = {"status": "OK", "message":  "Login Success.", "user_info": user_info}
            return jsonify(messages)
        else:
            return jsonify(status="bad",message="Wrong Email or Password")

#user get status
@app.route("/user/get/status/<int:device_id>")
def get_status(device_id):
    conn = conf()
    with conn.cursor() as cursor:
        query = f"SELECT state FROM user WHERE device_id={device_id}"
        cursor.execute(query)
        results=cursor.fetchall()
        conn.close()
        if results:
            return jsonify(status=results[0][0])
        else:
            return jsonify(status="False")

@app.route("/user/set/status/<int:id>/<int:state>", methods=['PUT'])
def set_status(id, state):
    try:
        try:
            conn = conf()
            with conn.cursor() as cursor:
                query = f"UPDATE user SET state = {state} WHERE id={id}"
                cursor.execute(query)
            conn.commit()
            conn.close()
            return jsonify(status="OK", message="State is changed!")

        except pymysql.err.IntegrityError as e:
            conn.rollback()
            conn.close()
            return jsonify(status="bad", message="Failed to set state!")

    except Exception as e:
        return jsonify(status="err", message="Failed to set state!")


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
#user register
@app.route('/user/register/<string:email>/<string:password>/<int:device_id>/<int:state>', methods=['POST'])
def register_user(email, password, device_id, state):
    try:
        try:
            conn = conf()
            with conn.cursor() as cursor:
                query = f"INSERT INTO user (email, password, device_id, state) VALUES('{email}', '{password}', {device_id}, {state})" #masukin ke dalam table database
                cursor.execute(query)
            conn.commit()
            conn.close()
            return jsonify(status="OK", message="Account has been registered!")

        except pymysql.err.IntegrityError as e:
            conn.rollback()
            conn.close()
            return jsonify(status="bad", message="Email has been registered. Please use another email!")

    except Exception as e:
        return jsonify(status="err", message="Failed to registered")


#upload data report
@app.route('/data/post/<int:device_id>/<float:latitude>/<float:longitude>/<string:hole_type>/<string:url_img>', methods=['POST'])
def post_data(device_id, latitude, longitude, hole_type, url_img):
    try:
        try:
            conn = conf()
            with conn.cursor() as cursor:
                query = """
                INSERT INTO data (user_id, latitude, longitude, hole_type, url_img)
                SELECT id, {}, {}, '{}', '{}' FROM user
                WHERE device_id = {}""".format(latitude, longitude, hole_type, url_img, device_id) #masukin ke dalam table database
                # query = f"INSERT INTO data (device_id, latitude, longitude, hole_type, url_img) VALUES({device_id}, {latitude}, {longitude}, '{hole_type}', '{url_img}')" #masukin ke dalam table database
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

#get data report
@app.route('/data/get/<int:user_id>')
def get_data(user_id):
    conn = conf()
    with conn.cursor() as cursor:
        # query = """
        # SELECT latitude, longitude, hole_type, url_img FROM data
	    #     WHERE user_id={}
        # """.format(user_id)
        query = f"SELECT * FROM data WHERE user_id={user_id}"
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
