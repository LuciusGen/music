from database import database


def test_all():
    database.insert_info("testA", "testS")
    info = database.select_by_author("testA")

    assert info[0] == "testA"
    assert info[1] == "testS"

    database.clear_table()
    info = database.select_by_author("testA")

    assert info is None
