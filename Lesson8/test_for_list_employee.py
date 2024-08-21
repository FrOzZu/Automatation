import requests
import pytest
from EmployeeApi import EmployeeApi


api = EmployeeApi("https://x-clients-be.onrender.com")
                       

def test_get_list():
    name = "Autotest1"
    descr = "HW 8"
    result = api.create_company(name, descr)
    new_id = result["id"]
 
    body = api.get_employee_list(f'?company={new_id}')
    assert len(body) == 0

    
def test_add_new_employer():
    name = "Компания"
    descr = "HW 8"
    result = api.create_company(name, descr)
    new_id = result["id"]
    
    body1 = api.get_employee_list(f'?company={new_id}')
    len_before = len(body1)

    id = ""
    firstName = "Евгений"
    lastName = "Гайнулин"
    middleName = "Александрович"
    companyId = new_id
    email = "test@test.com"
    url = " "
    phone = "+79969570455"
    birthdate = "2020-04-15T17:19:22.062Z"
    isActive = True
    new_emp = api.create_employee(id, firstName, lastName, middleName,  companyId, email, url, phone, birthdate, isActive)
    res = new_emp["id"]
    
    body2 = api.get_employee_list(f'?company={new_id}')
    len_after = len(body2)
   
    assert body2[-1]["id"] ==  res
    assert body2[-1]["firstName"] ==  firstName
    assert body2[-1]["lastName"] ==  lastName
    assert body2[-1]["middleName"] ==  middleName
    assert body2[-1]["companyId"] ==  companyId
    assert body2[-1]["phone"] ==  phone
    assert body2[-1]["isActive"] ==  isActive
    assert len_after - len_before == 1
 
def test_one_employer():
    name = "Autotest"
    descr = "HW8"
    result = api.create_company(name, descr)
    new_id = result["id"]
    
    id = ""
    firstName = "Евгений"
    lastName = "Гайнулин"
    middleName = "Александрович"
    companyId = new_id
    email = "test@mail.ru"
    url = " "
    phone = "+79969570455"
    birthdate = "2020-04-15T17:19:22.062Z"
    isActive =  True
    result = api.create_employee(id, firstName, lastName, middleName,  companyId, email, url, phone, birthdate, isActive)
    new_id_emp = result["id"]
    
    employer_body = api.get_employer(new_id_emp)
    
    
    assert employer_body["firstName"] ==  firstName
    assert employer_body["lastName"] ==  lastName
    assert employer_body["middleName"] ==  middleName
    assert employer_body["companyId"] ==  companyId
    assert employer_body["phone"] ==  phone
    assert employer_body["isActive"] ==  isActive
		   
def test_change_data():
    name = "Autotest"
    descr = "HW8"
    result = api.create_company(name, descr)
    new_id = result["id"]
    
    id = ""
    firstName = "Евгений"
    lastName = "Гайнулин"
    middleName = "Александрович"
    companyId = new_id
    email = "test@mail.ru"
    url = " "
    phone = "+79969570455"
    birthdate = "2020-04-15T17:19:22.062Z"
    isActive =  True
    result = api.create_employee(id, firstName, lastName, middleName,  companyId, email, url, phone, birthdate, isActive)
    new_id_emp = result["id"]
    
    
    id = new_id_emp
    lastName = "Рафаэль"
    email = "test@mail.ru"
    url = "https://my_profile.com"
    phone = "89654789654"
    isActive = True
    new_data = api.change_data(new_id_emp, lastName, email, url, phone, isActive)
    
    employer_body = api.get_employer(new_id_emp)
    
    assert employer_body["id"] == new_id_emp
    assert employer_body["isActive"] == isActive
    assert employer_body["email"] == email
    assert employer_body["url"] == url