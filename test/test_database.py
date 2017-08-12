import os
import psycopg2
import pytest

from app.myModules.DatabaseControl import DatabaseControl


def test_open_db_1():
    db = DatabaseControl(os.environ["DATABASE_URL"])
    value = db.close_connect()

    assert value is True


def test_open_db_2():
    with pytest.raises(psycopg2.Error):
        db = DatabaseControl(os.environ["DATABASE_URL"])
        db.sql_execute("SELECT * FROM noting")
