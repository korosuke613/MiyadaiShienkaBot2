from MiyadaiDataBase import MiyadaiDatabaseOutput
from MiyadaiScraping import MiyadaiScraping


def check_new_miyadai_shienka_news(db):
    sc = MiyadaiScraping()

    record = sc.fetch_shienka_news()

    for dic in record:
        if db.fetch_shienka_news_once(dic["url_news"]) is False:
            # 新しい記事の場合
            yield dic
        else:
            # 古い記事の場合
            yield dic["url_news"]


def get_new_miyadai_shienka_news(db):
    records = check_new_miyadai_shienka_news(db)
    new_newses = [record for record in records if isinstance(record, dict) is True]

    if len(new_newses) == 0:
        # 新着記事がない場合
        return False

    return new_newses


if __name__ == "__main__":
    myzk = MiyadaiDatabaseOutput()
    print(get_new_miyadai_shienka_news(myzk))
    myzk.close_connect()
