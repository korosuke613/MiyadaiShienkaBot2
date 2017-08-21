import os

from app.myModules.dbcontrol import DatabaseControl


def test_open_db_1():
    db = DatabaseControl(os.environ["DATABASE_URL"])
    value = db.close_connect()

    assert value is True


def test_sql_execute1():
    db = DatabaseControl(os.environ["DATABASE_URL"])
    value = db.sql_execute("SELECT * FROM noting")
    db.close_connect()

    assert value is False


def test_sql_execute2():
    db = DatabaseControl(os.environ["DATABASE_URL"])
    value = db.sql_execute("SELECT * FROM miyadai_shienka_news")
    db.close_connect()

    assert value is True
