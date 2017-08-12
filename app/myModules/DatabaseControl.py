import urllib.request
import psycopg2


class DatabaseControl:
    def __init__(self, db_url_):
        self.__database_url = urllib.parse.urlparse(db_url_)
        self.__conn = psycopg2.connect(
            database=self.__database_url.path[1:],
            user=self.__database_url.username,
            password=self.__database_url.password,
            host=self.__database_url.hostname,
            port=self.__database_url.port
        )
        self.__cur = self.__conn.cursor()

    def close_connect(self):
        self.__cur.close()
        self.__conn.close()
        return True

    def sql_execute(self, sql):
        try:
            self.__cur.execute(sql)
        except psycopg2.Error:
            return False
        else:
            return True

    def sql_fetch_one(self):
        # TODO 例外を作る
        return self.__cur.fetchone()

    def sql_fetch_all(self):
        # TODO 例外を作る
        return self.__cur.fetchall()

    def commit(self):
        self.__conn.commit()
