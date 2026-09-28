import random
from database import database_connection


def SignUP():
    print("====WELCOME TO RESISTATION=======")
    name = input('Enter a Name:')
    password = input('Enter a Password:')
    email = input('Enter a Email:')
    gender = input('enter a gender:')
    age = input('Enter a age:')

    print('automatically assigin account number:')

    while True:

        account_number = random.randint(10000000, 90000000)

        quary1  = '''
                SELECT account_number
                FROM bank_data
                WHERE account_number = %s 
                '''
        
        connection1 = database_connection()

        cursor = connection1.cursor()

        cursor.execute(quary1,(account_number,))

        result = cursor.fetchone()

        if result:
            connection1.commit()
            connection1.close() 
            continue
        
        else:
            query2 = '''
                INSERT INTO bank_data
                (name, password, email, gender, age, account_number, status)
                VALUES (%s,%s, %s, %s, %s, %s, %s)
            '''
            cursor.execute(query2,(name,password,email,gender,age,account_number,True))

            connection1.commit()

            print('Account created successfully!')
            print('Welcome To Bibek Bank Sir')
            print('Your account number:', account_number)
            cursor.close()
            connection1.close()

            break



        
        


