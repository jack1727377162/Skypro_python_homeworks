from My_company import Company
from authorization import My_authorization
from URL_xclientsbe import URL_xclients_be
from My_employee import Employee
import pytest

auth = My_authorization(URL_xclients_be)
company = Company(URL_xclients_be)
employee = Employee(URL_xclients_be)


@pytest.fixture()
def company_id():
    auth.auth_user()
    create_company = company.add_company("Thebestcompany", "Intheworls")
    id_company = create_company["id"]
    yield id_company


def test_get_employee_list(company_id):
    id_company = company_id
    result_employee_list, status_code = employee.get_employee_list(id_company)
    assert status_code == 200
    assert len(result_employee_list) == 0
    result_add_employee, status_code_employee = employee.add_new_employee(
        "Микеланджело", "Патичувак", id_company, "makejackadullboy@gmail.com", "middle", "url", "phone", True
    )
    assert status_code_employee == 201
    id_employee = result_add_employee["id"]
    result_employee_list_update, _ = employee.get_employee_list(id_company)
    assert len(result_employee_list_update) == len(result_employee_list) + 1
    assert id_employee == result_employee_list_update[-1]["id"]


def test_get_employee_list_negative():
    result_employee_list, status_code = employee.get_employee_list("0")
    assert status_code == 200
    assert len(result_employee_list) == 0


def test_add_new_employee_negative(company_id):
    id_company = company_id
    result_add_employee, status_code_employee = employee.add_new_employee(
        "", "", id_company, "", "", "", "", True
    )
    assert status_code_employee == 400
    assert result_add_employee["message"] == [
        "firstName should not be empty",
        "lastName should not be empty",
        "email must be an email",
    ]
    assert result_add_employee["error"] == "Bad Request"


def test_get_employee_by_id(company_id):
    id_company = company_id
    result_add_employee, status_code_employee = employee.add_new_employee(
        "Микеланджело", "Патичувак", id_company, "makejackadullboy@gmail.com", "middle", "url", "phone", True
    )
    assert status_code_employee == 201
    id_employee = result_add_employee["id"]

    result_get_employee, status_code_get_employee = employee.get_employee_by_id(
        id_employee
    )
    assert status_code_get_employee == 200
    assert result_get_employee["id"] == id_employee
    assert result_get_employee["firstName"] == "Микеланджело"
    assert result_get_employee["lastName"] == "Патичувак"
    print(result_get_employee)
    assert result_get_employee["avatar_url"] == "url"
    assert result_get_employee["companyId"] == id_company


def test_change_employee_info(company_id):
    id_company = company_id
    result_add_employee, status_code_employee = employee.add_new_employee(
        "Донателло", "Непатичувак", id_company, "jacksemail@gmail.com", "middle", "url", "phone", True
    )
    assert status_code_employee == 201
    id_employee = result_add_employee["id"]
    print(result_add_employee)
    result_change_employee_info, change_employee_status_code = (
        employee.edit_employee_info(id_employee, "Совсемнепатичувак",
                                    "changedjacksemail@gmail.com", "N_url", "N_phonetwo", True)
    )
    print(result_change_employee_info)
    assert change_employee_status_code == 200
    assert result_change_employee_info["id"] == id_employee
    assert result_change_employee_info["email"] == "changedjacksemail@gmail.com"
    assert result_change_employee_info["url"] == "N_url"

    result_get_employee, status_code_get_employee = employee.get_employee_by_id(
        id_employee
    )
    print(result_get_employee)
    print(status_code_get_employee)
    assert status_code_get_employee == 200
    assert result_get_employee["lastName"] == "Совсемнепатичувак"


def test_change_employee_info_negative(company_id):
    id_company = company_id
    result_add_employee, status_code_employee = employee.add_new_employee(
        "Рафаэль", "Седмен", id_company, "sadmanrafff@gmail.com", "middle", "N_url", "N_phonetwo", True
    )
    assert status_code_employee == 201
    id_employee = result_add_employee["id"]

    result_change_employee_info_negative, change_employee_status_code_negative = (
        employee.edit_employee_info(id_employee, "", "str", "", "", True)
    )
    assert change_employee_status_code_negative == 400
    assert result_change_employee_info_negative["message"] == [
        "lastName should not be empty",
        "email must be an email",
    ]
    assert result_change_employee_info_negative["error"] == "Bad Request"
