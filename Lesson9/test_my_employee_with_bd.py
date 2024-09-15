from my_company import TstCompany
from my_employee import TstEmployee
from company_table import CompanyTable
from faker import Faker
from URL_xclientsbe import URL_xclients_be
import pytest

tst_fake = Faker()

company_tst = TstCompany(URL_xclients_be)
employee_tst = TstEmployee(URL_xclients_be)

dt_base = CompanyTable("postgresql://x_clients_user:95PM5lQE0NfzJWDQmLjbZ45"
                       "ewrz1fLYa@dpg-cqsr9ulumphs73c2q40g-a.frankfurt-postg"
                       "res.render.com/x_clients_db_fxd0")


@pytest.fixture
def fake_info():
    return {
        "company_name": tst_fake.company(),
        "company_description": tst_fake.word(),
        "first_name": tst_fake.first_name(),
        "last_name": tst_fake.last_name(),
        "email": tst_fake.email(),
        "phone_number": tst_fake.phone_number()[:15],
    }


def test_get_employee_list(fake_info):
    dt_base.create_company(fake_info["company_name"],
                           fake_info["company_description"])
    max_id_company = dt_base.get_max_id()
    dt_base.create_employee(
        fake_info["first_name"],
        fake_info["last_name"],
        fake_info["email"],
        max_id_company,
        fake_info["phone_number"],
    )
    list_employee = dt_base.get_employee(max_id_company)
    id_new_employee = list_employee[0]["id"]
    result_employee_list, status_code = employee_tst.get_employee_list(
        max_id_company)
    assert status_code == 200
    assert len(list_employee) == len(result_employee_list)
    assert list_employee[-1][4] == fake_info["first_name"]
    assert list_employee[-1]["last_name"] == \
        result_employee_list[-1]["lastName"]
    assert list_employee[-1]["email"] == result_employee_list[-1]["email"]
    dt_base.delete_employee(id_new_employee)
    dt_base.delete_company(max_id_company)


def test_get_employee_list_negative():
    employee_list = dt_base.get_employee("999999")
    assert len(employee_list) == 0


def test_add_new_employee_negative(fake_info):
    empty_field = ""
    dt_base.create_company(fake_info["company_name"],
                           fake_info["company_description"])
    max_id_company = dt_base.get_max_id()
    dt_base.create_employee(empty_field, empty_field, empty_field,
                            max_id_company, empty_field)
    get_employee_list_bd = dt_base.get_employee(max_id_company)
    id_employee = get_employee_list_bd[0]["id"]
    result_employee_list, status_code = employee_tst.get_employee_list(
        max_id_company)
    assert status_code == 200
    assert len(get_employee_list_bd) == len(result_employee_list)  # 1
    assert (
        get_employee_list_bd[-1]
        ["first_name"] == result_employee_list[-1]["firstName"]
    )
    dt_base.delete_employee(id_employee)
    dt_base.delete_company(max_id_company)


def test_get_employee_by_id(fake_info):
    dt_base.create_company(fake_info["company_name"],
                           fake_info["company_description"])
    max_id_company = dt_base.get_max_id()
    dt_base.create_employee(
        fake_info["first_name"],
        fake_info["last_name"],
        fake_info["email"],
        max_id_company,
        fake_info["phone_number"],
    )
    list_employee = dt_base.get_employee(max_id_company)
    id_new_employee_bd = list_employee[0]["id"]
    id_employee_api, status_code_api = employee_tst.get_employee_by_id(
        id_new_employee_bd)
    assert status_code_api == 200
    assert id_new_employee_bd == id_employee_api["id"]
    assert id_employee_api["firstName"] == fake_info["first_name"]
    assert id_employee_api["lastName"] == fake_info["last_name"]
    assert id_employee_api["email"] == fake_info["email"]
    assert id_employee_api["companyId"] == max_id_company
    dt_base.delete_employee(id_new_employee_bd)
    dt_base.delete_company(max_id_company)


def test_change_employee_info(fake_info):
    employee_name = "Микеланджело"
    employee_last_name = "Патичувак"
    employee_email = "makejackadullboy@gmail.com"
    employee_phone = "79999999999"
    dt_base.create_company(fake_info["company_name"],
                           fake_info["company_description"])
    first_company = dt_base.get_max_id()
    dt_base.create_employee(
        fake_info["first_name"],
        fake_info["last_name"],
        fake_info["email"],
        first_company,
        fake_info["phone_number"],
    )
    list_employee = dt_base.get_employee(first_company)
    id_new_employee_bd = list_employee[-1]["id"]
    api_result_employee_list_first_company, status_code_first = (
        employee_tst.get_employee_list(first_company)
    )
    assert status_code_first == 200
    assert api_result_employee_list_first_company[0]["companyId"] == \
        first_company
    dt_base.create_company(fake_info["company_name"],
                           fake_info["company_description"])
    second_company = dt_base.get_max_id()
    dt_base.edit_employee_info(
        employee_name,
        employee_last_name,
        employee_email,
        employee_phone,
        second_company,
        id_new_employee_bd,
    )
    changed_employee = dt_base.get_employee(second_company)
    api_result_employee_list_second_company, status_code_second = (
        employee_tst.get_employee_list(second_company))
    assert status_code_second == 200
    assert changed_employee[0]["first_name"] == employee_name
    assert changed_employee[0]["last_name"] == employee_last_name
    assert changed_employee[0]["email"] == employee_email
    assert changed_employee[0]["phone"] == employee_phone
    assert changed_employee[0]["company_id"] == second_company
    dt_base.delete_employee(id_new_employee_bd)
    dt_base.delete_company(first_company)
    dt_base.delete_company(second_company)


def test_change_employee_info_negative(fake_info):
    empty_field = ""
    dt_base.create_company(fake_info["company_name"],
                           fake_info["company_description"])
    first_company = dt_base.get_max_id()
    dt_base.create_employee(
        fake_info["first_name"],
        fake_info["last_name"],
        fake_info["email"],
        first_company,
        fake_info["phone_number"],
    )
    list_employee = dt_base.get_employee(first_company)
    id_new_employee_bd = list_employee[-1]["id"]
    api_result_employee_list_first_company, status_code_first = (
        employee_tst.get_employee_list(first_company)
    )
    assert status_code_first == 200
    assert api_result_employee_list_first_company[0]
    ["companyId"] == first_company
    dt_base.create_company("Second", "Company")
    second_company = dt_base.get_max_id()
    dt_base.edit_employee_info(
        empty_field,
        empty_field,
        empty_field,
        empty_field,
        second_company,
        id_new_employee_bd,
    )
    changed_employee = dt_base.get_employee(second_company)
    api_result_employee_list_second_company, status_code_second = (
        employee_tst.get_employee_list(second_company)
    )
    assert status_code_second == 200
    assert api_result_employee_list_second_company[0]
    ["firstName"] == changed_employee[0]["first_name"]
    assert api_result_employee_list_second_company[0]
    ["lastName"] == changed_employee[0]["last_name"]
    assert api_result_employee_list_second_company[0]
    ["email"] == changed_employee[0]["email"]
    assert api_result_employee_list_second_company[0]
    ["phone"] == changed_employee[0]["phone"]
    assert api_result_employee_list_second_company[0]
    ["companyId"] == second_company
    dt_base.delete_employee(id_new_employee_bd)
    dt_base.delete_company(first_company)
    dt_base.delete_company(second_company)
