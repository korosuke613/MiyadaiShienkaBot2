import os

from app.myModules.DatabaseControl import DatabaseControl
from app.MiyadaiScraping import MiyadaiScraping


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
                  % (dic["day"], dic["title"], dic["url"])
            db.sql_execute(sql)
        except StopIteration:
            break

    print("db commit")
    db.commit()
    print("db close")
    db.close_connect()

    # db.sql_execute("INSERT INTO miyadai_shienka (day, title, url) VALUES (%s, %s, %s)",
    # (days[r], menus[r], urls[r]))

if __name__ == "__main__":
    insert_shienka_all_news_to_miyadai_shienka()
