import allure
import requests


class EmployeeApi:

    def __init__(self,url) ->None:
        self.url = url
    @allure.step("api - Получение токена авторизации {user}:{password}")
    def get_token(self, user='raphael', password='cool-but-crude') -> str:
        """
        Получение токена авторизации
        params user(str): логин
        params password(str): пароль
        
        return: str: token
        """
        
        creds = {
            'username': user,
            'password': password
        }
        resp = requests.post(self.url+'/auth/login',json=creds)
        return resp.json()["userToken"]
    @allure.step("api - создание  компании {name}:{description}")  
    def create_company(self, name, description="") -> str:
        company = {
            "name": name,
            "description": description
        }
        my_headers = {}
        my_headers["x-client-token"] = self.get_token()
        resp = requests.post(self.url + '/company',
                             json=company, headers=my_headers)
        return resp.json()

    @allure.step("api - получение списка сотрудников компании")
    def get_employee_list(self, params_to_add=None) -> str:
        resp = requests.get(self.url + '/employee' + params_to_add)
        return resp.json()

    @allure.step("api - Создание нового сотрудника {id}:{firstName}:{lastName}:{companyId}:{phone}:{isActive}")
    def create_employee(self, id, firstName, lastName, companyId, phone, isActive)->str:
        employer = {
            "id": id,
            "firstName": firstName,
            "lastName": lastName,
            "companyId": companyId,
            "phone": phone,
            "isActive": isActive
        }
        my_headers = {}
        my_headers["x-client-token"] = self.get_token()
        resp = requests.post(self.url+'/employee',
                             json=employer, headers=my_headers)
        return resp.json()
    @allure.step("api - Получение сотрудника по {id}")
    def get_employer(self, id)->str:
        resp = requests.get(self.url + f'/employee/{id}')
        return resp.json()
    @allure.step("api - Изменение данных пользователя {id}:{lastName}:{email}:{phone}:{isActive}")
    def change_data(self, id, lastName, email, phone, isActive, headers)->str:
        employer = {
            "id": id,
            "lastName": lastName,
            "email": email,
            "phone": phone,
            "isActive": isActive,
            "my_headers": headers
        }

        my_headers = {}
        my_headers["x-client-token"] = self.get_token()
        resp = requests.patch(self.url + f'/employee/{id}',
                              json=employer, headers=my_headers)
        return resp.json()
    
    def get_company_by_id(self, id):
        resp = requests.get(self.url + f'/company/{id}')
        return resp.json()