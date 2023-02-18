from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import os
from dotenv import load_dotenv


load_dotenv()


class Browser:
    browser, services = None, None


    def __init__(self, driver:str):
        self.services = Service(driver)
        self.browser = webdriver.Chrome(service=self.services)

    
    def open_page(self, url:str):
        self.browser.get(url)


    def close_page(self):
        self.browser.close()

    def add_input(self, by:By, value:str, text:str):
        fields = self.browser.find_element(by=by, value=value)
        fields.send_keys(text)
        time.sleep(2)

    def click_button(self, by:By, value:str):
        button = self.browser.find_element(by=by, value=value)
        button.click()
        time.sleep(2)

    def login_web(self, email:str, password:str):
        self.click_button(by=By.CSS_SELECTOR, value='#nav-main > div > a.nav-item.login-link.d-none.d-lg-block.px-20')
        self.add_input(by=By.ID, value='login_username', text=email)
        self.click_button(by=By.ID, value = 'login_password_continue')
        self.add_input(by=By.ID, value='login_password', text=password)
        self.click_button(by=By.ID, value='login_control_continue')


    def search_gigs(self, value:str):
        self.add_input(by=By.CSS_SELECTOR, value='#fwh-search-for-job-input > div > div > div > div > input', text=value)
        self.click_button(by=By.CSS_SELECTOR, value='#main > div > div > div > div.d-none.d-lg-block.d-block-mobile-app > div.d-flex.justify-space-between > div > div.up-input-group-append > button')


if __name__ == '__main__':
    browser = Browser(os.getenv('DRIVER_PATH'))

    browser.open_page('https://www.upwork.com')
    time.sleep(3)

    browser.login_web(email=os.getenv('EMAIL'), password=os.getenv('PASSWORD'))
    time.sleep(10)

    browser.search_gigs(value='PHP')
    time.sleep(10)

    browser.close_page()