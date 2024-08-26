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
    company_id = db.get_max_id_comp()

    api_result_b = api.get_employee_list(f'?company={company_id}')
    db_result_b = db.select_employers(company_id)

    f_name = 'Иван'
    l_name = 'Петров'
    phone = '+79969598584'

    db.create_employer(company_id, f_name, l_name, phone)

    api_result_a = api.get_employee_list(f'?company={company_id}')
    db_result_a = db.select_employers(company_id)

    assert len(api_result_b) == len(db_result_b)
    assert len(api_result_a) == len(db_result_a)
    assert len(db_result_a) - len(db_result_b) == 0
    for employee in api_result_a:
        if api_result_a == employee["id"]:
            assert employee["first_name"] == f_name
            assert employee["last_name"] == l_name
            assert employee["phone"] == phone
            assert employee["company_id"] == company_id

    db.clear_table_employers(company_id)
    db.delete_company(company_id)


def test_one_employer():
    db.create_company('Моя компания')
    company_id = db.get_max_id_comp()

    f_name = 'Гайнулин'
    l_name = 'Евгений'
    phone = '+79969598676'

    db.create_employer(company_id, f_name, l_name, phone)
    max_id_e = db.get_max_id_emp(company_id)
    db_result = db.get_employer_by_id(max_id_e)

    assert db_result["first_name"] == f_name
    assert db_result["last_name"] == l_name
    assert db_result["company_id"] == company_id
    assert db_result["phone"] == phone

    db.clear_table_employers(company_id)
    db.delete_company(company_id)


def test_change_data():
    db.create_company('Моя компания')
    company_id = db.get_max_id_comp()

    f_name = 'Иван'
    l_name = 'Петров'
    phone = '+79969598676'

    db.create_employer(company_id, f_name, l_name, phone)
    max_id_e = db.get_max_id_emp(company_id)
    

    id = max_id_e
    l_name = 'Рафаэль'
    email = 'test@mail.com'
    url = 'https://my_profile.com'
    phone = '89654789654'
    is_active = True
    resp = api.change_data(id, l_name, email, url, phone, is_active)

    employer_body = api.get_employer(max_id_e)

    assert employer_body["id"] == max_id_e
    assert employer_body["isActive"] == is_active
    assert employer_body["email"] == email

    db.clear_table_employers(company_id)
    db.delete_company(company_id)


def test_delete_company_and_employers():
    name = 'Моя компания'
    db.create_company(name)
    company_id = db.get_max_id_comp()

    f_name = 'Иван'
    l_name = 'Петров'
    phone = '+79969598676'

    db.create_employer(company_id, f_name, l_name, phone)
    db.clear_table_employers(company_id)
    api_result = api.get_employee_list(f'?company={company_id}')
    assert len(api_result) == 1
    deleted = db.delete_company(company_id)

    assert len(api_result) == 0
    assert deleted["id"] == company_id
    assert deleted["f_name"] == f_name
    assert deleted["l_name"] == l_name
    assert deleted["phone"] == phone

    rows = api.get_company_by_id(company_id)
    assert len(rows) == 0