import psycopg2
import logging


class DB:
    def __init__(self):
        self.db = db = psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="Ganner1203!",
            host="localhost",
            port=5432,
        )
        self.cur = db.cursor()

    def Rquery(self, query: str):
        """Query to read something (e.g. rows)"""
        try:
            self.cur.execute(query)
            return self.cur.fetchall()
        except psycopg2.Error as e:
            return print(e)

    def Cquery(self, query: str):
        """Query to create something (e.g. table, add a column)"""
        try:
            self.cur.execute(query)
            self.db.commit()
        except Exception as e:
            print(e)


db = DB()
