import mysql.connector


class MySqlConnector:
    db = None

    def __init__(self, host, port, user, password, db):
        self.db = mysql.connector.connect(
            host=host,
            port=port,
            user=user,
            passwd=password,
            database=db
        )

    def get_connection(self):
        return self.db
