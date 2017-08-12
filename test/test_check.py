import pytest

from app.MiyadaiDataBase import MiyadaiDatabaseOutput
from app.check import get_new_miyadai_shienka_news

NUM = 5


@pytest.fixture()
def fixture_db():
    db = MiyadaiDatabaseOutput()
    yield db
    db.close_connect()


@pytest.fixture()
def fixture_db_five_remove(fixture_db):
    fixture_db.sql_execute("DELETE FROM miyadai_shienka_news WHERE max(id) > max(id) - %s" % (NUM,))
    yield fixture_db


def test_get_new_miyadai_shienka_news1(fixture_db_five_remove):
    new_newses = get_new_miyadai_shienka_news(fixture_db_five_remove)

    assert isinstance(new_newses, list)

    for i in range(NUM):
        value = fixture_db_five_remove.fetch_shienka_news_once(new_newses[i]["url_news"])
        assert value is False
