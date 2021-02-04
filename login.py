import configparser
import mysql.connector
from mysql.connector import Error

config = configparser.ConfigParser()
config.read("config.ini")
USERNAME = config['database credentials']['username']
PASSWORD = config['database credentials']['passphrase']
DATABASE = config['database credentials']['databaseName']
TABLE_NAME = config['database credentials']['tableName'] 

def login(_username,_pass):
    """ Connect to MySQL database & login """
    conn = None
    try:
        conn = mysql.connector.connect(host = 'localhost',
                                       database = DATABASE,
                                        user = USERNAME,
                                        password = PASSWORD)
        if conn.is_connected():
            # print('Connected to MySQL database')

            mycursor = conn.cursor()
            querry = """SELECT password FROM {}.{} WHERE username = "{}" """.format(DATABASE,TABLE_NAME,_username)
            mycursor.execute(querry)
            result = mycursor.fetchall() # returns a list of touples 
            if(not len(result) == 0):
                if(str(result[0][0]) == str(_pass)):
                    return True
                    conn.close()
            else:
                return False
                conn.close()

    except Error as e:
        print(e)
        return False

    finally:
        if conn is not None and conn.is_connected():
            conn.close()
