import pytest

from app.MiyadaiDataBase import MiyadaiDataBaseInput


_record = ["100000000",
           "2017年6月13日",
           "ひらこばの誕生日",
           "https://korosuke613.github.io",
           "https://korosuke613.github.io/screen_shot",
           "https://korosuke613.github.io/pdf_shot",
           ]

_record2 = ["100000001",
            "2017年7月27日",
            "こにしの誕生日",
            "https://pokemon.com",
            "https://pokemon.com/screen_shot",
            "https://pokemon.com/pdf_shot",
            ]


def insert_dic_news(record):
    dic = {"day": record[1],
           "title": record[2],
           "url_news": record[3],
           "url_screen_shot": record[4],
           "url_pdf_shot": record[5],
           }
    return dic


@pytest.fixture()
def fixture_db():
    db_in = MiyadaiDataBaseInput()
    dic = insert_dic_news(_record)
    dic2 = insert_dic_news(_record2)
    yield [db_in, dic, dic2]
    db_in.close_connect()


def test_insert_news1(fixture_db):
    db = fixture_db[0]
    input_dic = fixture_db[1]

    db.insert_news(input_dic)

    db.sql_execute("SELECT * FROM miyadai_shienka_news ORDER BY day DESC;")
    record = db.sql_fetch_one()
    output_dic = insert_dic_news(record)

    assert input_dic["day"] == output_dic["day"]
    assert input_dic["title"] == output_dic["title"]
    assert input_dic["url_news"] == output_dic["url_news"]


def test_update_images_url1(fixture_db):
    db = fixture_db[0]
    input_dic1 = fixture_db[1]
    input_dic2 = fixture_db[2]

    db.insert_news(input_dic1)
    db.insert_news(input_dic2)
    db.update_images_url(input_dic1)
    db.update_images_url(input_dic2)

    db.sql_execute("SELECT * FROM miyadai_shienka_news WHERE url_news='https://korosuke613.github.io'")
    record1 = db.sql_fetch_one()
    output_dic1 = insert_dic_news(record1)

    db.sql_execute("SELECT * FROM miyadai_shienka_news WHERE url_news='https://pokemon.com'")
    record2 = db.sql_fetch_one()
    output_dic2 = insert_dic_news(record2)

    assert input_dic1 == output_dic1
    assert input_dic2 == output_dic2
    assert output_dic2 is not output_dic1
