from sqlalchemy import create_engine
from sqlalchemy import text
db_connection_string = "postgresql://x_clients_user:95PM5lQE0NfzJWDQmLjbZ45ewrz1fLYa@dpg-cqsr9ulumphs73c2q40g-a.frankfurt-postgres.render.com/x_clients_db_fxd0"


def test_db_connection():
    db = create_engine(db_connection_string)
    names = db.table_names()
    assert names[1] == "company"


def test_select():
    db = create_engine(db_connection_string)
    rows = db.execute("select * from company").fetchall()
    row1 = rows[0]
    assert row1[0] == 4933
    assert row1["name"] == "Эльдорадо"
    rowlast = rows[-1]
    # assert rowlast[0] == 7453
    # assert rowlast["name"] == "New updating company"


def test_select_1_row():
    db = create_engine(db_connection_string)
    sql_statement = text("select * from company where id = :company_id")

    rows = db.execute(sql_statement, company_id=4933).fetchall()

    assert len(rows) == 1
    assert rows[0]["name"] == "Эльдорадо"


def test_select_1_row_with_two_filters():
    db = create_engine(db_connection_string)
    sql_statement = text(
        'select * from company where "is_active" = :is_active and id >= :id'
    )

    params = {"id": 6365, "is_active": True}
    rows = db.execute(sql_statement, params).fetchall()

    # assert len(rows) == 852
    assert rows[0]["name"] == "Ministry Of Magic"


def test_insert():
    db = create_engine(db_connection_string)
    sql = text("insert into company(\"name\") values (:company_new_name)")
    rows = db.execute(sql, company_new_name='Моя_новая_компания')


def test_update():
    db = create_engine(db_connection_string)
    sql = text(
        "update company set description = :company_description where id = :id")
    rows = db.execute(
        sql, company_description="Почти новая, почти моя", id=7467)


def test_delete():
    db = create_engine(db_connection_string)
    sql = text("delete from company where id = :id")
    rows = db.execute(sql, id=7467)
