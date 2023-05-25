import time
from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service


def test_signIn():
    obj_service = Service("/Users/apoorvgupta/Downloads/geckodriver")
    driver = webdriver.Firefox(service=obj_service)
    driver.maximize_window()
    driver.get("https://ucm.sapidblue.in/#/signin")
    time.sleep(2)
    driver.find_element(By.ID,"username").send_keys('apoorv')
    driver.find_element(By.ID,"password").send_keys('12345678')
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    assert driver.find_element(By.CSS_SELECTOR,'.user-container')
    return driver

# def test_userRegistration():
#     driver.find_element(By.)
