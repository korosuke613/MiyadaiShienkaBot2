import os

from app.myModules.dbcontrol import DatabaseControl
from app.miyadai_sc import MiyadaiScraping
from app.miyadai_db import MiyadaiDatabaseOutput, MiyadaiDataBaseInput
from app.upload import upload_image
from app.myModules.pdf2png import download_pdf, convert


def insert_shienka_all_news_to_miyadai_shienka():
    """
    最初にデータベースにデータを入れるスクリプト
    注意！fetch_shienka_news()は降順でレコードを返すので、昇順にしてください！
    """
    db = DatabaseControl(os.environ["DATABASE_URL"])
    md = MiyadaiScraping()

    iterate = md.fetch_shienka_news()
    while True:
        try:
            dic = iterate.__next__()
            # print(dic["day"], dic["title"], dic["url"])
            sql = "INSERT INTO miyadai_shienka_news(day, title, url_news) VALUES ('%s', '%s', '%s')"\
                  % (dic["day"], dic["title"], dic["url_news"])
            db.sql_execute(sql)
        except StopIteration:
            break

    print("db commit")
    db.commit()
    print("db close")
    db.close_connect()

    # db.sql_execute("INSERT INTO miyadai_shienka (day, title, url) VALUES (%s, %s, %s)",
    # (days[r], menus[r], urls[r]))


def update_shienka_all_news_screen_shot_to_miyadai_shienka():
    db = MiyadaiDatabaseOutput()
    md = MiyadaiScraping()
    db_input = MiyadaiDataBaseInput()

    iterate = db.fetch_shienka_news_all()
    while True:
        dic = iterate.__next__()
        if dic is False:
            break
        print(dic["url_news"])
        md.screenshot_news_crop(dic["url_news"])
        url_screen_shot = upload_image("screenshot_crop.png", tag="miyadai_shienka_news_screen_shot")
        db_input.sql_execute(
            "UPDATE miyadai_shienka_news SET url_screen_shot='%s' WHERE url_news='%s'"
            % (url_screen_shot, dic["url_news"],))

    db_input.commit()
    db_input.close_connect()
    db.close_connect()


def update_shienka_all_news_pdf_shot_to_miyadai_shienka():
    db = MiyadaiDatabaseOutput()
    md = MiyadaiScraping()
    db_input = MiyadaiDataBaseInput()

    iterate = db.fetch_shienka_news_all()
    while True:
        dic = iterate.__next__()
        if dic is False:
            break
        url_pdf = md.check_pdf(dic["url_news"])
        if url_pdf is None:
            continue
        print(url_pdf)
        download_pdf(url_pdf, "news.pdf")
        convert("news.pdf")

        url_pdf_shot = upload_image("news.png", tag="miyadai_shienka_news_pds_shot")
        db_input.sql_execute(
            "UPDATE miyadai_shienka_news SET url_pdf_shot='%s' WHERE url_news='%s'"
            % (url_pdf_shot, dic["url_news"],))
    db_input.commit()
    db_input.close_connect()
    db.close_connect()

if __name__ == "__main__":
    update_shienka_all_news_pdf_shot_to_miyadai_shienka()
