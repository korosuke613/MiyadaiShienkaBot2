import os

from myModules.DatabaseControl import DatabaseControl


class MiyadaiDatabaseOutput(DatabaseControl):
    def __init__(self):
        super().__init__(os.environ["DATABASE_URL"])

    def get_users(self):
        # TODO usersテーブルは未実装
        self.sql_execute("SELECT user_id FROM users")
        rows = self.sql_fetch_all()
        return rows

    def fetch_shienka_news_all(self):
        self.sql_execute("SELECT * FROM miyadai_shienka_news ORDER BY day DESC;")
        while True:
            record = self.sql_fetch_one()
            dic = self.insert_dic_news(record)
            yield dic

    def fetch_shienka_news_once(self, url):
        sql = "SELECT * FROM miyadai_shienka_news WHERE url_news = '%s'" % (url,)
        if self.sql_execute(sql):
            record = self.sql_fetch_one()
            return self.insert_dic_news(record)
        return False

    @staticmethod
    def insert_dic_news(record):
        dic = {"day": record[1],
               "title": record[2],
               "url_news": record[3],
               "url_screen_shot": record[4],
               "url_pdf_shot": record[5],
               }
        return dic
