import sqlite3
from test_spider import settings
# import settings


class Connector(object):
    def __init__(self):
        self.conn = sqlite3.connect(settings.SQLITE_DB_PATH)
        self.cursor = self.conn.cursor()

    def get_urls(self):
        # lon, lat, address, source_id, st_name, source
        self.cursor.execute("""
            SELECT from_cur, to_cur
            FROM main_currencyсorrelation;
            """)

        res = self.cursor.fetchall()
        # base = "https://ru.cryptonator.com/rates/{}-{}"
        # urls = [base.format(el[0], el[1]) for el in res]
        base = "https://ru.cryptonator.com/rates/convert/?amount=1&primary={}&secondary={}&source=liverates"
        urls = [base.format(el[0].lower(), el[1].lower()) for el in res]
        # self.close()
        return urls

    def get_corr_id(self, from_cur, to_cur):
        self.cursor.execute("""
            SELECT id
            FROM main_currencyсorrelation WHERE from_cur="{}" AND to_cur="{}";
            """.format(from_cur.upper(), to_cur.upper())
        )

        _id = self.cursor.fetchone()
        if _id:
            try:
                _id = _id[0]
                return _id
            except Exception:
                return None
        else:
            return None

    def write_record(self, correlation_id, value):
        # CurrencyValue
        self.cursor.execute("""
            INSERT INTO main_currencyvalue(correlation_id, value)
            VALUES ({}, {});
            """.format(correlation_id, value)
        )
        self.conn.commit()
        # self.close()

    def close(self):
        self.conn.close()

if __name__ == "__main__":
    c = Connector()
    print(c.get_corr_id("BTC", "USD"))

    _id = c.get_corr_id("BTC", "USD")
    if _id:
        c.write_record(_id, 2222)
    # print(c.get_urls())
