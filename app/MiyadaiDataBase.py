import os

from myModules.DatabaseControl import DatabaseControl


class MiyadaiDataBase(DatabaseControl):
    def __init__(self):
        super().__init__(os.environ["DATABASE_URL"])

    @staticmethod
    def insert_dic_news(record):
        dic = {"day": record[1],
               "title": record[2],
               "url_news": record[3],
               "url_screen_shot": record[4],
               "url_pdf_shot": record[5],
               }
        return dic


class MiyadaiDataBaseInput(MiyadaiDataBase):
    def insert_user(self, dic):
        # TODO 未実装
        pass

    def insert_news(self, dic):
        return self.sql_execute("INSERT INTO miyadai_shienka_news (day, title, url_news) VALUES ('%s', '%s', '%s')"
                                % (dic["day"], dic["title"], dic["url_news"]))

    def update_images_url(self, dic):
        return self.sql_execute(
            "UPDATE miyadai_shienka_news SET url_screen_shot='%s' , url_pdf_shot='%s' WHERE url_news='%s'"
            % (dic["url_screen_shot"], dic["url_pdf_shot"], dic["url_news"],))


class MiyadaiDatabaseOutput(MiyadaiDataBase):
    def get_users(self):
        # TODO usersテーブルは未実装
        self.sql_execute("SELECT user_id FROM users")
        rows = self.sql_fetch_all()
        return rows

    def fetch_shienka_news_all(self):
        self.sql_execute("SELECT * FROM miyadai_shienka_news ORDER BY day DESC;")
        while True:
            record = self.sql_fetch_one()
            if record is None:
                yield False
            dic = self.insert_dic_news(record)
            yield dic

    def fetch_shienka_news_once(self, url):
        sql = "SELECT * FROM miyadai_shienka_news WHERE url_news = '%s'" % (url,)
        if self.sql_execute(sql):
            record = self.sql_fetch_one()
            if isinstance(record, tuple):
                return self.insert_dic_news(record)
            else:
                return False
        return False
