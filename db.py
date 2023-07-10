import pickle
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException


def hh_login(driver: webdriver.ChromiumEdge, email: str, password: str, cookies_patch: str) -> bool:
    safety_get(driver, 'https://hh.ru/account/login')

    def login():
        driver.find_element(By.XPATH, '//input[@type="email"]').send_keys(email)
        time.sleep(2)
        driver.find_element(By.XPATH, '//input[@type="password"]').send_keys(password)
        time.sleep(2)
        driver.find_element(By.XPATH, '//input[@type="submit"]').click()
        time.sleep(2)

        safety_get(driver, 'https://hh.ru/application/settings?from=header_new')

        try:
            driver.find_element(By.XPATH, '//button[@data-qa="mainmenu_applicantProfile "]')
            pickle.dump((driver.get_cookies(), open(cookies_patch, "wb")))
            print('new cookies saved')
            return True

        except NoSuchElementException:
            raise Exception('authorization failed')

    try:
        driver.find_element(By.XPATH, '//button[@data-qa="mainmenu_applicantProfile "]')
        print('authorization has been made')
        return True

    except NoSuchElementException:
        return login()


def safety_get(driver: webdriver.ChromiumEdge, url: str):
    driver.set_page_load_timeout(7)
    try:
        driver.get(url)

    except TimeoutException:
        print('page refresh')
        driver.refresh()


# Create a new instance of the Chrome driver
driver = webdriver.ChromiumEdge()

# Call the hh_login function
email = 'zi@calculate.ru'
password = 'Anna0809'
cookies_patch = 'cookies.pkl'

hh_login(driver, email, password, cookies_patch)

# Quit the driver
driver.quit()