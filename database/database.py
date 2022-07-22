import os

import psycopg2

DATABASE_URL = os.getenv("DATABASE_URL")


def select_by_author(author: str):
    db_connector = psycopg2.connect(DATABASE_URL)
    db_cursor = db_connector.cursor()

    db_cursor.execute("SELECT * FROM new_music "
                      "WHERE singer = %s",
                      (author,))

    try:
        return db_cursor.fetchall()[0]
    except Exception:
        return None


def clear_table():
    db_connector = psycopg2.connect(DATABASE_URL)
    db_cursor = db_connector.cursor()

    db_cursor.execute("DELETE FROM new_music")
    db_connector.commit()


def insert_info(author: str, song: str):
    db_connector = psycopg2.connect(DATABASE_URL)
    db_cursor = db_connector.cursor()
    try:
        db_cursor.execute("INSERT INTO new_music (singer, song)"
                          "VALUES (%s, %s )",
                          (author, song))
        db_connector.commit()
    except Exception:
        return None
