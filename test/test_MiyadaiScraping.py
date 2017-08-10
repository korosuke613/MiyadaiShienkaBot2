from app.MiyadaiScraping import MiyadaiScraping


def test_shienka_all_news_1():
    sc = MiyadaiScraping()
    dic = sc.shienka_all_news()

    latest = oldest = dic.__next__()

    for news in dic:
        oldest = news

    latest = latest['day']
    oldest = oldest['day']

    assert latest[:4] > oldest[:4]
