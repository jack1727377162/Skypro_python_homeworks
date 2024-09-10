import requests
from authorization import MyAuthorization


class TstEmployee:
    def __init__(self, my_url):
        self.my_url = my_url
        self.auth = MyAuthorization(my_url)

    def get_employee_list(self, company_id):
        employee_list = requests.get(
            self.my_url + "/employee" + "?company=" + str(company_id)
        )
        return employee_list.json(), employee_list.status_code

    def get_employee_by_id(self, my_id):
        result_get_employee_id = requests.get(
            self.my_url + "/employee/" + str(my_id))
        return result_get_employee_id.json(), \
            result_get_employee_id.status_code

    def add_new_employee(
        self,
        first_name,
        last_name,
        company_id,
        email,
        id_num,
        middle_name,
        url,
        phone,
        birthdate,
        is_active,
    ):
        employee_info = {
            "id": id_num,
            "firstName": first_name,
            "lastName": last_name,
            "companyId": company_id,
            "email": email,
            "url": url,
            "phone": phone,
            "birthdate": birthdate,
            "isActive": is_active,
        }
        my_token = {}
        my_token["x-client-token"] = self.auth.auth_user()
        result_add_employee = requests.post(
            self.url + "/employee", json=employee_info, headers=my_token
        )
        return result_add_employee.json(), result_add_employee.status_code

    def edit_employee_info(
            self, my_id, last_name, email, my_url="", phone="", is_active=""
    ):
        employee_new_info = {
            "lastName": last_name,
            "email": email,
            "url": my_url,
            "phone": phone,
            "isActive": is_active,
        }
        my_token = {}
        my_token["x-client-token"] = self.auth.auth_user()
        result_edit_employee_info = requests.patch(
            self.my_url + "/employee/" + str(my_id),
            json=employee_new_info, headers=my_token
            )
        return result_edit_employee_info.json(), \
            result_edit_employee_info.status_code
