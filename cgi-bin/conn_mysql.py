import mysql.connector
from mysql.connector import Error

class Connect:
    def __init__(self, host='192.168.0.41', database='kripto', user='krok', password='Dthrjy14'):
        self.host = host
        self.database = database
        self.user = user
        self.password = password

    def read_db(self):
        try:
            conn = mysql.connector.Connect(host=self.host,
                                           database=self.database,
                                           user=self.user,
                                           password=self.password)
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM results")

            row = cursor.fetchone()

            while row is not None:
                print(row)
                row = cursor.fetchone()

        except Error as e:
            print(e)

        finally:
            cursor.close()
            conn.close()