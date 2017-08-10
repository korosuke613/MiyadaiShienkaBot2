import os
import psycopg2

from app.myModules.DatabaseControl import DatabaseControl


def test_open_db_1():
    db = DatabaseControl(os.environ["DATABASE_URL"])
    value = db.close_connect()

    assert value is True


def test_open_db_2():
    isExcept = False
    db = DatabaseControl(os.environ["DATABASE_URL"])
    try:
        db.sql_execute("SELECT * FROM noting")
    except psycopg2.Error:
        isExcept = True
    finally:
        db.close_connect()

    assert isExcept is True
