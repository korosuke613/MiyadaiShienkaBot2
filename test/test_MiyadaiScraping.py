from app.MiyadaiScraping import MiyadaiScraping
import os.path


def test_shienka_all_news_1():
    sc = MiyadaiScraping()
    dic = sc.fetch_shienka_news()

    latest = oldest = dic.__next__()

    for news in dic:
        oldest = news

    latest = latest['day']
    oldest = oldest['day']

    assert latest[:4] > oldest[:4]


def test_check_pdf_1():
    sc = MiyadaiScraping()
    url = sc.check_pdf("http://gakumu.of.miyazaki-u.ac.jp/gakumu/andsoon/andsoon/3508-2017-08-10-04-08-15.html")

    assert url is not None


def test_check_pdf_2():
    sc = MiyadaiScraping()
    url = sc.check_pdf("http://gakumu.of.miyazaki-u.ac.jp/gakumu/andsoon/andsoon/3495-2017-07-25-05-33-46.html")

    assert url is None


def test_screenshot_news_crop1():
    sc = MiyadaiScraping()
    url = "http://gakumu.of.miyazaki-u.ac.jp/gakumu/andsoon/andsoon/3508-2017-08-10-04-08-15.html"
    assert sc.screenshot_news_crop(url) is True

    assert os.path.isfile("screenshot.png")
    assert os.path.isfile("screenshot_crop.png")


def test_screenshot_news_crop2():
    sc = MiyadaiScraping()
    url = sc.check_pdf("http://gakumu.of.miyazaki-u.ac.jp/gakumu/andsoon/andsoon/3508-2017-08-10-04-08-15.html")
    assert sc.screenshot_news_crop(url) is False
