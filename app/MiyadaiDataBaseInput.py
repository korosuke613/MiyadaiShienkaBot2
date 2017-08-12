import os

from app.myModules.DatabaseControl import DatabaseControl


class MiyadaiDataBaseInput(DatabaseControl):
    def __init__(self):
        super().__init__(os.environ["DATABASE_URL"])

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
