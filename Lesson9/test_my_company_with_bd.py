from My_company import Company
from authorization import My_authorization
from CompanyTable import CompanyTable
from faker import Faker
import pytest
from URL_xclientsbe import URL_xclients_be
fake = Faker()

auth = My_authorization(URL_xclients_be)
company = Company(URL_xclients_be)

db = CompanyTable(
    "postgresql://x_clients_user:95PM5lQE0NfzJWDQmLjbZ45ewrz1fLYa@dpg-cqsr9ulumphs73c2q40g-a.frankfurt-postgres.render.com/x_clients_db_fxd0"
)


@pytest.fixture
def fake_info():
    return {
        "company_name": fake.company(),
        "company_description": fake.word(),
    }


def test_get_companies():
    api_result = company.get_company_list()
    db_result = db.get_companies()
    assert len(api_result) == len(
        db_result
    )


def test_get_one_company_id(fake_info):
    db.create_company(fake_info["company_name"],
                      fake_info["company_description"])
    max_id = db.get_max_id()
    new_company_get_id = company.get_company_id(max_id)
    db.delete_company(max_id)
    assert new_company_get_id["id"] == max_id
    assert new_company_get_id["name"] == fake_info["company_name"]
    assert new_company_get_id["description"] == fake_info["company_description"]
    assert new_company_get_id["isActive"] == True


def test_edit_company(fake_info):
    db.create_company(fake_info["company_name"],
                      fake_info["company_description"])
    max_id = db.get_max_id()
    new_name_company = "Updated"
    new_description_company = "_upd_"
    edited_company = company.edit_company(
        max_id, new_name_company, new_description_company
    )
    db.delete_company(max_id)
    assert edited_company["id"] == max_id
    assert edited_company["name"] == new_name_company
    assert edited_company["description"] == new_description_company
    assert edited_company["isActive"] == True


def test_delete_company(fake_info):
    db.create_company(fake_info["company_name"],
                      fake_info["company_description"])
    max_id = db.get_max_id()

    deleted_company = company.delete_company(max_id)

    assert deleted_company["id"] == max_id
    assert deleted_company["name"] == fake_info["company_name"]
    assert deleted_company["description"] == fake_info["company_description"]
    assert deleted_company["isActive"] == True
    rows = db.get_company_by_id(max_id)
    assert len(rows) == 1
    # assert rows[0]["deleted_at"] is None


def test_deactivate_company(fake_info):
    db.create_company(fake_info["company_name"],
                      fake_info["company_description"])
    max_id = db.get_max_id()
    result_deactivate_company = company.set_active_state(max_id, False)
    db.delete_company(max_id)
    assert result_deactivate_company["isActive"] == False


def test_deactivate_and_activate_back(fake_info):
    db.create_company(fake_info["company_name"],
                      fake_info["company_description"])
    max_id = db.get_max_id()
    result_deactivate_and_activate_company = company.set_active_state(
        max_id, True)
    company.set_active_state(max_id, False)
    db.delete_company(max_id)
    assert result_deactivate_and_activate_company["isActive"] == True
