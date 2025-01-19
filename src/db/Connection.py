import psycopg2


class Connection:
    def __init__(self):
        self.db = db = psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="Ganner1203!",
            host="localhost",
            port=5432,
        )
        self.cur = db.cursor()

    def Rquery(self, query: str, params: list = None):
        """Query to read something (e.g. rows)"""
        if params is None:
            params = []
        
        try:
            self.cur.execute(query, params)
            return self.cur.fetchall()
        except psycopg2.Error as e:
            return print(e)

    def Cquery(self, query: str, params: list = None):
        """Query to create something (e.g. table, add a column)"""
        if params is None:
            params = []

        try:
            self.cur.execute(query, params)
            self.db.commit()
        except Exception as e:
            print(e)


conn = Connection()
