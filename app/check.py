from miyadai_db import MiyadaiDatabaseOutput
from miyadai_sc import MiyadaiScraping


def check_new_miyadai_shienka_news(db):
    """現在の宮大支援課のお知らせをスクレイピングし、データベースに登録されてない記事があるかどうかをチェックする。
    @return ジェネレータ。新しい記事の場合はその記事の情報を辞書型で返す。既にある記事の場合はその記事のURLを返す。
    @param db: MiyadaiDataBaseOutputクラスのインスタンス。
    """
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
    """宮大支援課のお知らせの新しい記事の情報を取得する
    @param db: MiyadaiDataBaseOutputクラスのインスタンス。
    @return: 新しい記事の情報の辞書のタプル。
    """
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
