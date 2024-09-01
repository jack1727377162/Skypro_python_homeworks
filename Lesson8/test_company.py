from My_company import Company
from authorization import My_authorization
from URL_xclientsbe import URL_xclients_be


auth = My_authorization(URL_xclients_be)
company = Company(URL_xclients_be)


def test_get_companies():
    body = company.get_company_list()
    assert len(body) > 0


def test_get_active_companies():
    full_company_list = company.get_company_list()
    active_company_list = company.get_company_list(
        params_to_add={"active": "true"})
    assert len(full_company_list) > len(active_company_list)


def test_add_new_company():
    full_company_list = company.get_company_list()
    len_before = len(full_company_list)
    name_company = "My company to add"
    description_company = "to add"
    new_company = company.add_company(name_company, description_company)
    new_id = new_company["id"]
    full_company_list = company.get_company_list()
    len_after = len(full_company_list)
    assert len_after - len_before == 1
    assert full_company_list[-1]["name"] == name_company
    assert full_company_list[-1]["description"] == description_company
    assert full_company_list[-1]["id"] == new_id


def test_get_one_company_id():
    name_company = "My company to get id"
    description_company = "get id"
    new_company = company.add_company(name_company, description_company)
    new_id = new_company["id"]
    new_company_get_id = company.get_company_id(new_id)
    assert new_company_get_id["id"] == new_id
    assert new_company_get_id["name"] == name_company
    assert new_company_get_id["description"] == description_company
    assert new_company_get_id["isActive"] == True


def test_edit_company():
    name_company = "My company to edit"
    description_company = "to edit"
    new_company = company.add_company(name_company, description_company)
    new_id = new_company["id"]
    new_name_company = "My new company"
    new_description_company = "new company"
    edited_company = company.edit_company(
        new_id, new_name_company, new_description_company
    )
    assert edited_company["id"] == new_id
    assert edited_company["name"] == new_name_company
    assert edited_company["description"] == new_description_company
    assert edited_company["isActive"] == True


def test_delete_company():
    name_company = "My company to delete"
    description_company = "to delete"
    new_company = company.add_company(name_company, description_company)
    new_id = new_company["id"]
    deleted_company = company.delete_company(new_id)
    assert deleted_company["id"] == new_id
    assert deleted_company["name"] == name_company
    assert deleted_company["description"] == description_company
    assert deleted_company["isActive"] == True
    new_company_list = company.get_company_list()
    assert new_company_list[-1]["id"] == new_id


def test_deactivate_company():
    name_company = "My company to deactivate"
    description_company = "to deactivate"
    new_company = company.add_company(name_company, description_company)
    new_id = new_company["id"]
    result_deactivate_company = company.set_active_state(new_id, False)
    assert result_deactivate_company["isActive"] == False


def test_deactivate_and_activate_back():
    name_company = "My company deact and act"
    description_company = "deact and act!"
    new_company = company.add_company(name_company, description_company)
    new_id = new_company["id"]
    company.set_active_state(new_id, False)
    result_deactivate_and_activate_company = company.set_active_state(
        new_id, True)
    assert result_deactivate_and_activate_company["isActive"] == True
