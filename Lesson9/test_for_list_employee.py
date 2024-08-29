import requests
import pytest
import psycopg2
from EmployeeApi import EmployeeApi
from EmployeDB import EmployerTable

api = EmployeeApi("https://x-clients-be.onrender.com")
db = EmployerTable("postgresql://x_clients_user:95PM5lQE0NfzJWDQmLjbZ45ewrz1fLYa@dpg-cqsr9ulumphs73c2q40g-a.frankfurt-postgres.render.com/x_clients_db_fxd0")


def test_get_list():
    name = "My company"
    db.create_company(name)
    max_id = db.get_max_id_comp()

    api_result = api.get_employee_list(f'?company={max_id}')
    db_result = db.select_employers(max_id)
    db.delete_company(max_id)
    assert len(api_result) == len(db_result)


def test_add_new_employer():
    db.create_company('Моя компания')
    max_id_c = db.get_max_id_comp()

    api_result_b = api.get_employee_list(f'?company={max_id_c}')
    db_result_b = db.select_employers(max_id_c)

    f_name = 'Иван'
    l_name = 'Петров'
    phone = '+79969598584'

    db.create_employer(max_id_c, f_name, l_name, phone)

    api_result_a = api.get_employee_list(f'?company={max_id_c}')
    db_result_a = db.select_employers(max_id_c)

    assert len(api_result_b) == len(db_result_b)
    assert len(api_result_a) == len(db_result_a)
    assert len(db_result_a) - len(db_result_b) == 1
    for employee in api_result_a:
        if api_result_a == employee["id"]:
            assert employee["first_name"] == f_name
            assert employee["last_name"] == l_name
            assert employee["phone"] == phone
            assert employee["company_id"] == max_id_c

    db.clear_table_employers(max_id_c)


def test_one_employer():
    name = "Autotest"
    descr = "HW8"
    result = api.create_company(name, descr)
    new_id = result["id"]
    
    id = ""
    firstName = "Евгений"
    lastName = "Гайнулин"
    companyId = new_id
    phone = "+79969570455"
    isActive =  True
    result = api.create_employee(id, firstName, lastName, companyId, phone, isActive)
    new_id_emp = result["id"]
    
    employer_body = api.get_employer(new_id_emp)


def test_change_data():
    db.create_company('Моя компания')
    max_id_c = db.get_max_id_comp()

    f_name = 'Иван'
    l_name = 'Петров'
    phone = '+79969598584'

    db.create_employer(max_id_c, f_name, l_name, phone)
    max_id_e = db.get_max_id_emp(max_id_c)
    

    id = max_id_e
    l_name = 'Белов'
    email = 'test@mail.com'
    phone = '89654789654'
    is_active = True
    my_headers = {"x-client-token": api.get_token()}
    resp = api.change_data(id, l_name, email, phone, is_active, headers=my_headers)

    employer_body = api.get_employer(max_id_e)

    assert employer_body["id"] == max_id_e
    assert employer_body["isActive"] == is_active
    assert employer_body["email"] == email

    db.clear_table_employers(max_id_c)