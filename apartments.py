from selenium import webdriver
import time

PATH = '/home/kibet/chromedriver'
driver = webdriver.Chrome(PATH)
driver.get('https://www.apartments.com/customers/login')
time.sleep(10)
