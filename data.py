from datetime import datetime
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


def mobile_online_status():
    try:
        browser.find_element(By.CLASS_NAME, "ProfileIndicatorBadge__badgeOnlineMobile")
    except Exception:
        status_mobile = 0
    else:
        status_mobile = 1
    return status_mobile


def pc_online_status():
    try:
        browser.find_element(By.CLASS_NAME, "ProfileIndicatorBadge__badgeOnline")
    except Exception:
        status_pc = 0
    else:
        status_pc = 1
    return status_pc


def log_in(login, password):
    """Открытие сайта и авторизация"""
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)

    browser.get('https://vk.com/') #Открытие сайта
    sleep(1)

    username_input = browser.find_element(By.CSS_SELECTOR, "input[name='login']")   #поиск поля для ввода логина
    username_input.send_keys(login)   #Ввод логина
    login_button = browser.find_element(By.XPATH, "//button[@type='submit']")   #поиск кнопки войти
    login_button.click()    #нажатие кнопки войти
    sleep(1)
    password_input = browser.find_element(By.CSS_SELECTOR, "input[name='password']")
    password_input.send_keys(password)
    login_button = browser.find_element(By.XPATH, "//button[@type='submit']")
    login_button.click()
    sleep(1)
    return browser


def get_data(browser, people_links, N, sleeping_time):
    j = 1
    while j <= N:
        print('итерация номер: ', j)
        date_now = datetime.now().strftime("%Y-%m-%d; %H:%M:%S")
        for i, item in enumerate(people_links):
            file_name = str(item[15:]) + '.txt'
            file = open(file_name, "a")
            browser.get(item)  # Открытие сайта
            file.write(str(date_now) + ',' + str(pc_online_status()) + ',' + str(mobile_online_status()) + '\n')
            file.close()
        sleep(sleeping_time)
        j = j + 1
    browser.close()


"""ВХОДНЫЕ ДАННЫЕ"""
login = "79832921152"
password = "K0stya^^"
sleeping_time = 5 #время в секундах сколько ждать до следующей итерации
N = 70 #сколько итераций провести
people_links = ['https://vk.com/livekrasivo',
                'https://vk.com/daryasokolovaa',
                'https://vk.com/reshwhat']  #вставить ссылку на человека

length = len(people_links)
browser = log_in(login, password)
get_data(browser, people_links, N, sleeping_time)
