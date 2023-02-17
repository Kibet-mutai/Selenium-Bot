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

    def click_button(self, by:By, value:str, text:str):
        button = self.browser.find_element(by=by, value=value)
        button.click()
        time.sleep(2)

    def login_web(self, email:str, password:str):
        self.add_input(by=By.NAME, value='username', text=email)
        self.add_input(by=By.NAME, value='password', text=password)
        self.click_button(by=By.ID, value='loginButton')



if __name__ == '__main__':
    browser = Browser('/home/kibet/chromedriver')

    browser.open_page('https://www.apartments.com/customers/login')
    time.sleep(3)

    browser.login_web(email='email', password='password')
    time.sleep(10)

    browser.close_page()