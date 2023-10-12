# dz_05.10.2023
"""
1. Найти любой сайт, где есть элементы, которые нужно ожидать
(или появляются с задержкой, или неактивные кнопки, которые впоследствии
становятся активными, или какие-то исчезающие сообщения и т.п.),
и написать автотест, где использовать методы явного ожидание.

2. Создать новое репо, в котором будет скрипт из задачи №1.
Требования к репо:
ссылка на репо корректная, репо публичная, при переходе по ссылке, открывается страница с репо.
в репо есть описание в файле readme есть хотя бы один комит (а лучше два),
грамотно описывающий то, что было изменено.

ВНИМАНИЕ! Ответ на данное д/з должен быть только посредством ссылки на репо в github.
Никаких файлов скриптов и архивов отправлять не нужно.

"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

browser = webdriver.Chrome() # Создаем экземпляр нашего драйвера
# Говорим WebDriver'у искать каждый элемент на протяжении 2 секунд. Прописываем один раз.

browser.implicitly_wait(7) # это  неявное ожидание

try:
    print("Browser Start!")
    browser.get("https://solmar.com.ua/ua/")
    print("Переходим на сайт - страница авторизации")
    # time.sleep(5)
    to_come_in_log = browser.find_element(By.XPATH, "//div[@class='s-header__item -account']").click()
    # time.sleep(3)
    email_filed = browser.find_element(By.XPATH, "//input[@name='USER_LOGIN']")
    email_filed.send_keys("anat966@gmail.com")
    print("Ввели почту")
    # time.sleep(3)
    password_filed = browser.find_element(By.XPATH, "//input[@name='USER_PASSWORD']")
    password_filed.send_keys("Qwerty1234")
    print("Ввели пароль")
    # time.sleep(3)
    login_button = browser.find_element(By.XPATH, "//input[@name='Login']").click()
    print("нажали кнопку Вход")
    # Явное ожидание
    message = WebDriverWait(browser, 5).until_not(
        EC.visibility_of_element_located((By.XPATH, "//div[@class='s-modal__title s-h2']"))
    )

    time.sleep(3)
finally:
    browser.quit() # закрываем браузер
    print("Browser quit")

