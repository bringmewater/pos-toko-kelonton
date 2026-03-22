import mysql.connector
from mysql.connector import Error

class MySQLConnectionHandler:
    def __init__(self, host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.connection = None

    def create_connection(self):
        """ Create a database connection to a MySQL database """
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password
            )
            if self.connection.is_connected():
                print("Connection to MySQL DB successful")
        except Error as e:
            print(f"Error: '{e}'")

    def close_connection(self):
        """ Close database connection """
        if self.connection.is_connected():
            self.connection.close()
            print("Database connection closed")

    def execute_query(self, query):
        """ Execute a query on the database """
        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            self.connection.commit()
            print("Query executed successfully")
        except Error as e:
            print(f"Error: '{e}'")
