import mysql.connector

class user_model():
    def __init__(self):
        #connection establishment code
        try:
            con=mysql.connector.connect(host="localhost",user="root",password="",database="temp")
            print('Connection Successfull')
        except:
            print('Some error')
    def user_getall_model(self):
        #business logic
        return "This is user_signup_model"