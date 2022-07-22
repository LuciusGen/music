import time
from schedule import every, repeat, run_pending
from database import database


@repeat(every().day.at("12:00"))
def load_weather_by_hour():
    data = dict()  # TODO Load music from spotify
    database.clear_table()
    for author, song in data.items():
        database.insert_info(author=author, song=song)


if __name__ == "__main__":
    while True:
        run_pending()
        time.sleep(1)
