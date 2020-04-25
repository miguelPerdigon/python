from psycopg2 import connect
from logging import error


class Postgress:
    def __init__(self, host, user, db_name, password):

        self.conn = connect('host={host} dbname={dbname} user={user} password={password}'.format(
            host=host,
            user=user,
            dbname=db_name,
            password=password
        ))

    def do_query(self, query):
        try:
            cursor = self.conn.cursor()
            cursor.execute(query)
            return cursor.fetchall()

        except Exception as e:
            error(str(e))

    def do_insert(self, query, return_id=False):
        try:
            cursor = self.conn.cursor()
            cursor.execute(query)

            if return_id:
                return cursor.fetchone()[0]

        except Exception as e:
            self.conn.rollback()
            error(str(e))
            exit(1)

    def commit(self):
        self.conn.commit()

    def close_conn(self):
        try:
            self.conn.close()

        except Exception as e:
            error(str(e))
