import allure

from data import MestoAuthData
from pages.login_page import LoginPage


class TestLoginPage:

    @allure.title("Проверка авторизации")
    @allure.description("Авторизуемся под тестовым пользователем и проверяем что авторизовались под ним")
    def test_success_authorization(self, driver):
        login_page = LoginPage(driver)

        login_page.set_email_input(MestoAuthData.LOGIN)
        login_page.set_password_input(MestoAuthData.PASSWORD)
        main_page = login_page.click_auth_button()

        assert main_page.get_current_user() == MestoAuthData.LOGIN
