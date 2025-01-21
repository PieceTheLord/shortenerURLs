from .Connection import Connection


class DB(Connection):
    def __init__(self):
        super().__init__()

    def check_url(self, params: list = None):
        """check if there's a short or long url in the database"""

        if params is not None:
            sql = "SELECT * FROM urls WHERE short_code = %s OR original_url = %s"
            return db.Rquery(sql, params)
        else:
            raise Exception("No parameters provided")

    def increase_click_by_one(self, params: list = None):
        """Increase the click_count field by one"""

        if params is not None:
            sql = "UPDATE urls SET click_count = click_count + 1 WHERE short_code = %s OR original_url = %s"
            return db.Cquery(sql, params)
        else:
            raise Exception("No parameters provided")

    def insert_data(self, params: list = None):
        """Insert short_code and original_url into the database"""

        if params is not None:
            try:
                sql = "INSERT INTO urls(short_code, original_url) VALUES(%s, %s)"
                return db.Cquery(sql, params)
            except Exception as e:
                return e
        else:
            raise Exception("No parameters provided")


db = DB()
