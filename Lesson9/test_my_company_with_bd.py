from my_company import TstCompany
from authorization import MyAuthorization
from company_table import CompanyTable
from faker import Faker
import pytest
from URL_xclientsbe import URL_xclients_be
tst_fake = Faker()

auth_tst = MyAuthorization(URL_xclients_be)
company_tst = TstCompany(URL_xclients_be)

dt_base = CompanyTable("postgresql://x_clients_user:95PM5lQE0NfzJWDQmLjbZ45"
                       "ewrz1fLYa@dpg-cqsr9ulumphs73c2q40g-a.frankfurt-postg"
                       "res.render.com/x_clients_db_fxd0")


@pytest.fixture
def fake_info():
    return {
        "company_name": tst_fake.company(),
        "company_description": tst_fake.word(),
    }


def test_get_companies():
    api_result = company_tst.get_company_list()
    db_result = dt_base.get_companies()
    assert len(api_result) == len(
        db_result
    )


def test_get_one_company_id(fake_info):
    dt_base.create_company(fake_info["company_name"],
                           fake_info["company_description"])
    max_id = dt_base.get_max_id()
    new_company_get_id = company_tst.get_company_id(max_id)
    dt_base.delete_company(max_id)
    assert new_company_get_id["id"] == max_id
    assert new_company_get_id["name"] == fake_info["company_name"]
    assert new_company_get_id["description"] == \
        fake_info["company_description"]
    assert new_company_get_id["isActive"] is True


def test_edit_company(fake_info):
    dt_base.create_company(fake_info["company_name"],
                           fake_info["company_description"])
    max_id = dt_base.get_max_id()
    new_name_company = "Updated"
    new_description_company = "_upd_"
    edited_company = company_tst.edit_company(
        max_id, new_name_company, new_description_company
    )
    dt_base.delete_company(max_id)
    assert edited_company["id"] == max_id
    assert edited_company["name"] == new_name_company
    assert edited_company["description"] == new_description_company
    assert edited_company["isActive"] is True


def test_delete_company(fake_info):
    dt_base.create_company(fake_info["company_name"],
                           fake_info["company_description"])
    max_id = dt_base.get_max_id()

    deleted_company = company_tst.delete_company(max_id)

    assert deleted_company["id"] == max_id
    assert deleted_company["name"] == fake_info["company_name"]
    assert deleted_company["description"] == fake_info["company_description"]
    assert deleted_company["isActive"] is True
    comp_rows = dt_base.get_company_by_id(max_id)
    assert len(comp_rows) == 1
    # assert comp_rows[0]["deleted_at"] is None


def test_deactivate_company(fake_info):
    dt_base.create_company(fake_info["company_name"],
                           fake_info["company_description"])
    max_id = dt_base.get_max_id()
    result_deactivate_company = company_tst.set_active_state(max_id, False)
    dt_base.delete_company(max_id)
    assert result_deactivate_company["isActive"] is False


def test_deactivate_and_activate_back(fake_info):
    dt_base.create_company(fake_info["company_name"],
                           fake_info["company_description"])
    max_id = dt_base.get_max_id()
    result_deactivate_and_activate_company = company_tst.set_active_state(
        max_id, True)
    company_tst.set_active_state(max_id, False)
    dt_base.delete_company(max_id)
    assert result_deactivate_and_activate_company["isActive"] is True
