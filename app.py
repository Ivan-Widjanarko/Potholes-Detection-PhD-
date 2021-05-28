# import os
from flask import Flask
# from flask_restful import Resource, Api
# import pymysql


# db_user = os.environ.get('CLOUD_SQL_USERNAME')
# db_password = os.environ.get('CLOUD_SQL_PASSWORD')
# db_name = os.environ.get('CLOUD_SQL_DATABASE_NAME')
# db_connection_name = os.environ.get('CLOUD_SQL_CONNECTION_NAME')


# app = Flask(__name__)
# api = Api(app)

# users = []
# list_data = []

# def open_connection():
#     if os.environ.get('GAE_ENV') == 'standard':
#         # If deployed, use the local socket interface for accessing Cloud SQL
#         unix_socket = '/cloudsql/{}'.format(db_connection_name)
#         conn = pymysql.connect(user=db_user, password=db_password,
#                               unix_socket=unix_socket, db=db_name)
#     else:
#         # If running locally, use the TCP connections instead
#         # Set up Cloud SQL Proxy (cloud.google.com/sql/docs/mysql/sql-proxy)
#         # so that your application can use 127.0.0.1:3306 to connect to your
#         # Cloud SQL instance
#         host = '127.0.0.1'
#         conn = pymysql.connect(user=db_user, password=db_password,
#                               host=host, db=db_name)


# class User(Resource):
#     ##login & register
#     def get(self, email, password):
#         conn =  open_connection()
#         with conn.cursor() as cursor:
#             result = cursor.execute(f'SELECT * FROM table_user WHERE col_email={email} AND col_password={password};') #nama table
#             user = cursor.fetch()
#             if result > 0:
#                 got_user = jsonify(user)
#             else:
#                 got_user = "The user not found"
#         conn.close()
#         return got_user
#         # for user in users:
#         #     if user['email'] == email and user['password'] == password  :
#         #         return user
#         #     else:
#         #         return "The user not found"
#         # return {'email': None}, 404

# class UserRegister(Resource):    
#     #register
#     def post(self, email, password, device_id):

#         conn = open_connection()
#         with conn.cursor() as cursor:
#             cursor.execute(f'INSERT INTO table_user (col_email, col_password, device_id) VALUES({email}, {password}, {device_id}) WHERE NOT EXISTS (SELECT * FROM table_user WHERE code={email})') 
#             message = cursor.message()
#         conn.commit()
#         conn.close()

#         return message
#         #dua hal yang menyebabkan postnya gagal. 1) akun user udah ada
#         #kalo email udah terdaftar dan udah ada di database user. return/response pesan gagal

#         # if next(filter(lambda x: x['email'] == email, users), None) is not None:
#         #     return {'message': "An item with name '{}' already registered. Please re-registered again use another email.".format(email)}
#         # else:
#         #     user = {'email': email , 'password': password, 'device_id':device_id}
#         #     users.append(user)
#         #     return user, 201


# class Report(Resource):
#     #report gambar dari raspi
#     def post(self, device_id, location, classification, url, time):
#         data = {'device_id': device_id, 'location': location, 'classification': classification, 'url': url, 'time': time}
#         list_data.append(data)
#         return data, 201
        

# class GetReport(Resource):
#     def get(self, device_id): #device_id dari user harus foreign key sama yang ada di data report
#         for user in users :
#             if user['device_id'] == device_id:
#                 for item in list_data:
#                     if item['device_id'] == device_id:
#                         return item
#                     else:
#                         return "The user not found"
#         return {'email': None}, 404

# api.add_resource(User, '/users/<string:email>/<string:password>') #/users/dila/abcde
# api.add_resource(UserRegister, '/users/register/<string:email>/<string:password>/<int:device_id>') #/users/register/dila/abcde/12345
# api.add_resource(Report, '/data/send/<int:device_id>/<float:location>/<string:classification>/<string:url>/<string:time>') #/data/send/12345/0.1234/berat/url.com/10-10-10
# api.add_resource(GetReport, '/data/get/<int:device_id>') #/data/get/12345


# app.run(port=5000, debug=True)

from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()