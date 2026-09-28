from database import database_connection

class BankServices:
    def __init__(self):
        # self.menu()
        pass


    def __str__(self):
        print('Welcome To Our Bank Services'.upper())

    def menu(self):
        user_menu_input = input('''
                                =======WELCOME=======
                                1. Balance inquaries
                                2. Cash Deposite
                                3. fund transfer
                                4. Transection History
                                5. Withdrowl Balance
                                6. Exit
                                ''')
        match user_menu_input:
            case '1':
                self.balance_inquaries_method()

            case '2':
                pass

            case '3':
                pass

            case '4':
                pass

            case '5':
                pass

            case _:
                print('Invalid keyword!')

    def balance_inquaries_method(self):

        user_name = input('Enter a name: ')
        account_number = input('Enter an account number: ')

        query = '''
            SELECT name, account_number
            FROM bank_data
            WHERE name = %s AND account_number = %s
                '''

        connection = database_connection()
        cursor = connection.cursor()

        cursor.execute(query, (user_name, account_number))
        result = cursor.fetchone()
        print(result)

        if result:
            print("Account found!")
            print("Name:", result[0])
            print("Account Number:", result[1])

        else:
            print("Account not found!")
            

        cursor.close()
        connection.close()



    def cash_deposite_method(self):
        user_name = input('Enter a name: ')
        account_number = input('Enter an account number: ')

        query = '''
            UPDATE bank_data
            SET 
                '''

        connection = database_connection()
        cursor = connection.cursor()

        cursor.execute(query, (user_name, account_number))
        result = cursor.fetchone()
        print(result)



        cursor.close()
        connection.close()

    def fund_transfer_method(self):
        pass

    def Transection_History(self):
        pass

    def Withdrowl_balance(self):
        pass





        

BankServices_obj = BankServices()


        
        



