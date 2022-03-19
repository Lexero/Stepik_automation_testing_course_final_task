from pages.login_page import LoginPage
from pages.main_page import MainPage

link = "http://selenium1py.pythonanywhere.com/"


def test_guest_can_go_to_login_page(browser):   # Тест перехода на страницу логина
    page = MainPage(browser, link)   # Инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # Открываем страницу
    page.go_to_login_page()          # Выполняем метод страницы — переходим на страницу логина
    page.should_be_login_link()      # Смотрим, что на странице есть кнопка логина


def test_guest_should_see_login_link(browser):  # Тест на наличие кнопки логина
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_should_see_login_page(browser):  # Тест на наличие элементов на странице логина
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()
