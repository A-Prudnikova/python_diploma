import os
import pytest
from dotenv import load_dotenv
from api.utils.session import req_session
from faker import Faker


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


def test_auth_positive():
    login = os.getenv('BIGANTOLOGIN')
    password = os.getenv('BIGANTOPASSWORD')
    payload = {"email": login, "password": password}
    params = {"client": "web", "client_version": "1.0"}
    response = req_session().post('/users/login', json=payload, params=params)
    assert response.status_code == 200


def test_auth_wrong_login():
    password = os.getenv('BIGANTOPASSWORD')
    payload = {"email": "wrong login", "password": password}
    params = {"client": "web", "client_version": "1.0"}
    response = req_session().post('/users/login', json=payload, params=params)
    assert response.status_code == 403


def test_auth_wrong_password():
    login = os.getenv('BIGANTOLOGIN')
    payload = {"email": login, "password": "wrong password"}
    params = {"client": "web", "client_version": "1.0"}
    response = req_session().post('/users/login', json=payload, params=params)
    assert response.status_code == 403


def test_get_user_data():
    login = os.getenv('BIGANTOLOGIN')
    password = os.getenv('BIGANTOPASSWORD')
    payload = {"email": login, "password": password}
    params = {"client": "web", "client_version": "1.0"}
    login_data = req_session().post('/users/login', json=payload, params=params)
    response_text = login_data.text
    token = str(response_text[98:148])
    auth_params = {"client": "web", "client_version": "1.0", "auth_token": token}
    response = req_session().get('/my', params=auth_params)
    assert str(response.json()['result']['id']) == '2527'


def test_change_user_data():
    login = os.getenv('BIGANTOLOGIN')
    password = os.getenv('BIGANTOPASSWORD')
    payload = {"email": login, "password": password}
    params = {"client": "web", "client_version": "1.0"}
    login_data = req_session().post('/users/login', json=payload, params=params)
    response_text = login_data.text
    token = str(response_text[98:148])
    auth_params = {"client": "web", "client_version": "1.0", "auth_token": token}
    fake = Faker()
    name = fake.name()
    payload = {"name": name}
    response = req_session().put('/my', params=auth_params, json=payload)
    assert str(response.json()['result']['name']) == name