import os

from myModules.dbcontrol import DatabaseControl


class MiyadaiDataBase(DatabaseControl):
    def __init__(self):
        """コンストラクタ
        """
        super().__init__(os.environ["DATABASE_URL"])

    @staticmethod
    def insert_dic_news(record: tuple) -> dict:
        """宮大の記事のタプルを辞書型に変換する。
        @param record: 宮大支援課の記事の情報のタプル
        @return: 変換した辞書
        """
        dic = {"day": record[1],
               "title": record[2],
               "url_news": record[3],
               "url_screen_shot": record[4],
               "url_pdf_shot": record[5],
               }
        return dic


class MiyadaiDataBaseInput(MiyadaiDataBase):
    def insert_user(self, dic: dict):
        # TODO 未実装
        """データベースにユーザを登録する
        @param dic: ユーザの辞書
        """
        pass

    def insert_news(self, dic: dict) -> bool:
        """データベースに記事を登録する
        @param dic: 記事の辞書
        @return sqlの実行が成功したかどうか
        """
        return self.sql_execute("INSERT INTO miyadai_shienka_news (day, title, url_news) VALUES ('%s', '%s', '%s')"
                                % (dic["day"], dic["title"], dic["url_news"]))

    def update_images_url(self, dic: dict) -> bool:
        """データベースに記事の各画像を登録する
        @param dic: 記事の辞書
        @return sqlの実行が成功したかどうか
        """
        return self.sql_execute(
            "UPDATE miyadai_shienka_news SET url_screen_shot='%s' , url_pdf_shot='%s' WHERE url_news='%s'"
            % (dic["url_screen_shot"], dic["url_pdf_shot"], dic["url_news"],))


class MiyadaiDatabaseOutput(MiyadaiDataBase):
    def get_users(self) -> tuple:
        """ユーザを取得する
        @return ユーザリストのタプル
        """
        # TODO usersテーブルは未実装
        self.sql_execute("SELECT user_id FROM users")
        rows = self.sql_fetch_all()
        return rows

    def fetch_shienka_news_all(self, offset: int=0):
        """記事の情報を一つずつ取得する
        @return ジェネレータで記事の情報を辞書で返す
        """
        if offset == 0:
            self.sql_execute("SELECT * FROM miyadai_shienka_news ORDER BY day DESC;")
        else:
            self.sql_execute("SELECT * FROM miyadai_shienka_news ORDER BY day DESC LIMIT 10 OFFSET %s" % (offset,))
        while True:
            record = self.sql_fetch_one()
            if record is None:
                yield False
            dic = self.insert_dic_news(record)
            yield dic

    def fetch_shienka_news_once(self, url: str):
        """指定したurlの記事の情報を取得する
        @param url: 取得したい記事のurl
        @return: データベースに記事が登録されていたら、その記事を辞書型で返す。登録されていなければ、Falseを返す。
        """
        sql = "SELECT * FROM miyadai_shienka_news WHERE url_news = '%s'" % (url,)
        if self.sql_execute(sql):
            record = self.sql_fetch_one()
            if isinstance(record, tuple):
                return self.insert_dic_news(record)
            else:
                return False
        return False