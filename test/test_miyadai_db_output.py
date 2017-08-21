import pytest

from app.miyadai_db import MiyadaiDatabaseOutput


@pytest.fixture()
def fixture_db():
    db = MiyadaiDatabaseOutput()
    yield db
    db.close_connect()


def test_fetch_shienka_news_all1(fixture_db):
    record = fixture_db.fetch_shienka_news_all()
    dic = record.__next__()
    assert isinstance(dic, dict)


def test_fetch_shienka_news_once1(fixture_db):
    dic = fixture_db.fetch_shienka_news_once(
        "http://gakumu.of.miyazaki-u.ac.jp/gakumu/andsoon/andsoon/3507-2017-08-10-02-47-07.html")

    assert isinstance(dic, dict)

    assert dic["day"] == "2017年08月10日"
    assert dic["title"] == "学生ボランティア活動支援室ホームページ立ち上げのお知らせ"
    assert dic["url_news"] == "http://gakumu.of.miyazaki-u.ac.jp/gakumu/andsoon/andsoon/3507-2017-08-10-02-47-07.html"


def test_fetch_shienka_news_once2(fixture_db):
    dic = fixture_db.fetch_shienka_news_once(
        "http://ppp-lab.sakura.ne.jp/ProgrammingPlacePlus/cpp/index.html")

    assert dic is False
