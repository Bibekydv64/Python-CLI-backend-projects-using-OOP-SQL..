from restation import Sign_UP
from Sign_UP_process import SignUP



def first_login_signup():
    user_input = input('''
                    1. sign in
                    2. sign up
                    Enter a choise:
                    ''')
    match user_input:
        case '1':
            Sign_UP()

        case '2':
            SignUP()

        case _:
            print('Invalid keyword')

first_login_signup()



