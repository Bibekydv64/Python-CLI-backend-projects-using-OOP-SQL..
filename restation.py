from database import database_connection
from Sign_UP_process import SignUP
from bank_services import *


def Sign_UP():
     user_name = input('Enter a name:')
     user_password = input('Enter a password:')


     connection = database_connection()

     cursor = connection.cursor()

     quary = '''
            SELECT name, email 
            FROM bank_data
            WHERE name = %s AND password = %s
            '''
     cursor.execute(quary,(user_name,user_password))

     result = cursor.fetchone()

     if result:
          print(BankServices_obj.menu())
          print('Email already registered')

     else:
          print('USER NOT REGISTERED.PLEASE SIGN UP.')
          SignUP()

     cursor.close()
     connection.close()














     

     



     



















































