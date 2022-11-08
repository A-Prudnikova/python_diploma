from selene import have, by
from selene.support.shared.jquery_style import s
import allure
from selene.support.shared import browser
from web_ui.model.application import app


@allure.title("Test login skipping password")
def test_login_no_password():
    with allure.step("Open main page"):
        browser.open('/')

    with allure.step("Open login page"):
        app.form.enter_login_page()

    with allure.step("Type login"):
        app.form.type_wrong_login()

    with allure.step("Check the result"):
        s('.modal-custom__error').should(have.text('Incorrect e-mail or password.'))


@allure.title('Test login skipping email')
def test_login_no_email():
    with allure.step("Open main page"):
        browser.open('/')

    with allure.step("Open login page"):
        app.form.enter_login_page()

    with allure.step("Type password"):
        app.form.type_wrong_password()

    with allure.step("Check the result"):
        s('.modal-custom__error').should(have.text('Incorrect e-mail or password.'))


@allure.title('Test login wrong data')
def test_login_wrong_data():
    with allure.step("Open main page"):
        browser.open('/')

    with allure.step("Open login page"):
        app.form.enter_login_page()

    with allure.step("Type login"):
        app.form.type_wrong_login()

    with allure.step("Type password"):
        app.form.type_wrong_password()

    with allure.step("Check the result"):
        s('.modal-custom__error').should(have.text('Incorrect e-mail or password.'))


@allure.title('Test remind password')
def test_remind_password():
    with allure.step("Open main page"):
        browser.open('/')

    with allure.step("Open login page"):
        app.form.enter_login_page()

    with allure.step("Click remind btn"):
        app.form.remind_password()

    with allure.step("Check the result"):
        s('.control-label').should(have.text("E-mail:"))


@allure.title('Test register')
def test_register():
    with allure.step("Open main page"):
        browser.open('/')

    with allure.step("Open login page"):
        app.form.enter_login_page()

    with allure.step("Click register btn"):
        app.form.register()

    with allure.step("Check the result"):
        s('.modal-custom__title').should(have.text("Sign up"))

