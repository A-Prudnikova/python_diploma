from selene.support.shared.jquery_style import s
from selene import have, by


class LoginPage:
    def enter_login_page(self):
        s('.auth__sign-in').click()

    def type_wrong_login(self):
        s('[name="email"]').type("test").press_enter()

    def type_wrong_password(self):
        s('[name="password"]').type("test").press_enter()


    def remind_password(self):
        s('[href="/users/remind/"]').click()

    def register(self):
        s('[href="/users/register/"]').click()

