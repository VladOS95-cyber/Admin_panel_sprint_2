import os
import os.path
import sqlite3
from contextlib import contextmanager

import psycopg2
from dotenv import dotenv_values
from psycopg2.extensions import connection as _connection
from psycopg2.extras import DictCursor

import app_logger
import DataMigration
from DataMigration import PostgresSaver, SQLiteLoader

logger = app_logger.get_logger(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "db.sqlite")

env_config = dotenv_values(".env")


def load_from_sqlite(connection: sqlite3.Connection, pg_conn: _connection):
    """Основной метод загрузки данных из SQLite в Postgres"""

    postgres_saver = PostgresSaver(pg_conn)
    sqlite_loader = SQLiteLoader(connection)

    logger.info('Loading data')
    DataMigration.process(msg="message")
    data = sqlite_loader.load_movies()
    logger.info('Data from db.sqlite saved sucessfully')

    logger.info('Save data into postgre database')
    DataMigration.process(msg="message")
    postgres_saver.save_all_data(data)
    logger.info('All data saved sucessfully')


@contextmanager
def connection_context(db_path: str):
    connection = sqlite3.connect(db_path)
    yield connection
    connection.close()


if __name__ == '__main__':
    dsl = {
        'dbname': env_config['DB_NAME'],
        'user': env_config['DB_USER'],
        'password': env_config['DB_PASSWORD'],
        'host': 'localhost',
        'port': 5432,
        'options': '-c search_path=content'}
    with connection_context(DB_PATH) as sqlite_conn, psycopg2.connect(
        **dsl, cursor_factory=DictCursor
    ) as pg_conn:
        load_from_sqlite(sqlite_conn, pg_conn)
