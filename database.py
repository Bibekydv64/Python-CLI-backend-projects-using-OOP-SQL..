import mysql.connector as sql

def database_connection():
    conection = sql.connect(
                            host = 'localhost',
                            user = 'root',
                            # password = 'datascience@123',
                            database = 'bank_database'
                            )
    cursor = conection.cursor()
    cursor.execute('''
                    CREATE TABLE  IF NOT EXISTS bank_data(
                    user_id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(256) NOT NULL,
                    password VARCHAR(256) NOT NULL,
                    email VARCHAR(256) NOT NULL,
                    gender VARCHAR(256) NOT NULL,
                    age VARCHAR(256) NOT NULL,
                    account_number INTEGER NOT NULL,
                    balance INTEGER NOT NULL,
                    status BOOLEAN)
                    ''')
    conection.commit()
    cursor.close()
    # conection.close()
    print('Connection sucessfully')
    return conection


if __name__ == "__main__":
    database_connection()


