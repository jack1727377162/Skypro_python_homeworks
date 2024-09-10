from sqlalchemy import create_engine
from sqlalchemy import text

db_connection_string = ("postgresql://x_clients_user:95PM5lQE0NfzJWDQmLjbZ45"
                        "ewrz1fLYa@dpg-cqsr9ulumphs73c2q40g-a.frankfurt-postg"
                        "res.render.com/x_clients_db_fxd0")


def test_db_connection():
    comp_base = create_engine(db_connection_string)
    comp_names = comp_base.table_names()
    assert comp_names[1] == "company"


# def test_select():
#     comp_base = create_engine(db_connection_string)
#     comp_rows = comp_base.execute("select * from company").fetchall()
#     comp_rows1 = comp_rows[0]
#     assert comp_rows1[0] == 5470
#     assert comp_rows1["name"] == "Chamomile"
#     row_last = comp_rows[-1]
#     assert row_last[0] == 9792
#     assert row_last["name"] == "Моя_новая_компания3"


def test_select_1_row():
    comp_base = create_engine(db_connection_string)
    sql_statement = text("select * from company where id = :company_id")

    comp_rows = comp_base.execute(sql_statement, company_id=5369).fetchall()

    assert len(comp_rows) == 1
    assert comp_rows[0]["name"] == "Color Glass"


# def test_select_1_row_with_two_filters():
#     comp_base = create_engine(db_connection_string)
#     sql_statement = text(
#         'select * from company where "is_active" = :is_active and id >= :id'
#     )

#     my_params = {"id": 10349, "is_active": True}
#     comp_rows = comp_base.execute(sql_statement, my_params).fetchall()

#     assert len(comp_rows) == 2231
#     assert comp_rows[0]["name"] == "Цветочек"


def test_insert():
    comp_base = create_engine(db_connection_string)
    sql_statement = text(
        "insert into company(\"name\") values (:company_new_name)"
        )
    comp_base.execute(sql_statement, company_new_name='Моя_новая_компания')


def test_update():
    comp_base = create_engine(db_connection_string)
    sql_statement = text(
        "update company set description = :company_description where id = :id")
    comp_base.execute(
        sql_statement, company_description="Почти новая, почти моя", id=9792
        )


def test_delete():
    comp_base = create_engine(db_connection_string)
    sql_statement = text("delete from company where id = :id")
    comp_base.execute(sql_statement, id=9795)
