from My_company import Company
from My_employee import Employee
from CompanyTable import CompanyTable
from faker import Faker
from URL_xclientsbe import URL_xclients_be
import pytest

fake = Faker()

company = Company(URL_xclients_be)
employee = Employee(URL_xclients_be)

db = CompanyTable(
    "postgresql://x_clients_user:95PM5lQE0NfzJWDQmLjbZ45ewrz1fLYa@dpg-cqsr9ulumphs73c2q40g-a.frankfurt-postgres.render.com/x_clients_db_fxd0"
)


@pytest.fixture
def fake_info():
    return {
        "company_name": fake.company(),
        "company_description": fake.word(),
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "email": fake.email(),
        "phone_number": fake.phone_number()[:15],
    }


def test_get_employee_list(fake_info):
    db.create_company(fake_info["company_name"],
                      fake_info["company_description"])
    max_id_company = db.get_max_id()
    db.create_employee(
        fake_info["first_name"],
        fake_info["last_name"],
        fake_info["email"],
        max_id_company,
        fake_info["phone_number"],
    )
    list_employee = db.get_employee(max_id_company)
    id_new_employee = list_employee[0]["id"]
    result_employee_list, status_code = employee.get_employee_list(
        max_id_company)
    assert status_code == 200
    assert len(list_employee) == len(result_employee_list)
    assert list_employee[-1][4] == fake_info["first_name"]
    assert list_employee[-1]["last_name"] == result_employee_list[-1]["lastName"]
    assert list_employee[-1]["email"] == result_employee_list[-1]["email"]
    db.delete_employee(id_new_employee)
    db.delete_company(max_id_company)


def test_get_employee_list_negative():
    employee_list = db.get_employee("0")
    assert len(employee_list) == 0


def test_add_new_employee_negative(fake_info):
    empty_field = ""
    db.create_company(fake_info["company_name"],
                      fake_info["company_description"])
    max_id_company = db.get_max_id()
    db.create_employee(empty_field, empty_field, empty_field,
                       max_id_company, empty_field)
    get_employee_list_bd = db.get_employee(max_id_company)
    id_employee = get_employee_list_bd[0]["id"]
    result_employee_list, status_code = employee.get_employee_list(
        max_id_company)
    assert status_code == 200
    assert len(get_employee_list_bd) == len(result_employee_list)  # 1
    assert (
        get_employee_list_bd[-1]["first_name"] ==  result_employee_list[-1]["firstName"]
    )
    db.delete_employee(id_employee)
    db.delete_company(max_id_company)


def test_get_employee_by_id(fake_info):
    db.create_company(fake_info["company_name"],
                      fake_info["company_description"])
    max_id_company = db.get_max_id()
    db.create_employee(
        fake_info["first_name"],
        fake_info["last_name"],
        fake_info["email"],
        max_id_company,
        fake_info["phone_number"],
    )
    list_employee = db.get_employee(max_id_company)
    id_new_employee_bd = list_employee[0]["id"]
    id_employee_api, status_code_api = employee.get_employee_by_id(
        id_new_employee_bd)
    assert status_code_api == 200
    assert id_new_employee_bd == id_employee_api["id"]
    assert id_employee_api["firstName"] == fake_info["first_name"]
    assert id_employee_api["lastName"] == fake_info["last_name"]
    assert id_employee_api["email"] == fake_info["email"]
    assert id_employee_api["companyId"] == max_id_company
    db.delete_employee(id_new_employee_bd)
    db.delete_company(max_id_company)


def test_change_employee_info(fake_info):
    employee_name = "Микеланджело"
    employee_last_name = "Патичувак"
    employee_email = "makejackadullboy@gmail.com"
    employee_phone = "79999999999"
    db.create_company(fake_info["company_name"],
                      fake_info["company_description"])
    first_company = db.get_max_id()
    db.create_employee(
        fake_info["first_name"],
        fake_info["last_name"],
        fake_info["email"],
        first_company,
        fake_info["phone_number"],
    )
    list_employee = db.get_employee(first_company)
    id_new_employee_bd = list_employee[-1]["id"]
    api_result_employee_list_first_company, status_code_first = (
        employee.get_employee_list(first_company)
    )
    assert status_code_first == 200
    assert api_result_employee_list_first_company[0]["companyId"] == \
        first_company
    db.create_company(fake_info["company_name"],
                      fake_info["company_description"])
    second_company = db.get_max_id()
    db.edit_employee_info(
        employee_name,
        employee_last_name,
        employee_email,
        employee_phone,
        second_company,
        id_new_employee_bd,
    )
    changed_employee = db.get_employee(second_company)
    api_result_employee_list_second_company, status_code_second = (
        employee.get_employee_list(second_company)
    )
    assert status_code_second == 200
    assert changed_employee[0]["first_name"] == employee_name
    assert changed_employee[0]["last_name"] == employee_last_name
    assert changed_employee[0]["email"] == employee_email
    assert changed_employee[0]["phone"] == employee_phone
    assert changed_employee[0]["company_id"] == second_company
    db.delete_employee(id_new_employee_bd)
    db.delete_company(first_company)
    db.delete_company(second_company)


def test_change_employee_info_negative(fake_info):
    empty_field = ""
    db.create_company(fake_info["company_name"],
                      fake_info["company_description"])
    first_company = db.get_max_id()
    db.create_employee(
        fake_info["first_name"],
        fake_info["last_name"],
        fake_info["email"],
        first_company,
        fake_info["phone_number"],
    )
    list_employee = db.get_employee(first_company)
    id_new_employee_bd = list_employee[-1]["id"]
    api_result_employee_list_first_company, status_code_first = (
        employee.get_employee_list(first_company)
    )
    assert status_code_first == 200
    assert api_result_employee_list_first_company[0]["companyId"] == \
        first_company
    db.create_company("Second", "Company")
    second_company = db.get_max_id()
    db.edit_employee_info(
        empty_field,
        empty_field,
        empty_field,
        empty_field,
        second_company,
        id_new_employee_bd,
    )
    changed_employee = db.get_employee(second_company)
    api_result_employee_list_second_company, status_code_second = (
        employee.get_employee_list(second_company)
    )
    assert status_code_second == 200
    assert api_result_employee_list_second_company[0]["firstName"] == \
        changed_employee[0]["first_name"]
    assert api_result_employee_list_second_company[0]["lastName"] == \
        changed_employee[0]["last_name"]
    assert api_result_employee_list_second_company[0]["email"] == \
        changed_employee[0]["email"]
    assert api_result_employee_list_second_company[0]["phone"] == \
        changed_employee[0]["phone"]
    assert api_result_employee_list_second_company[0]["companyId"] == \
        second_company
    db.delete_employee(id_new_employee_bd)
    db.delete_company(first_company)
    db.delete_company(second_company)
