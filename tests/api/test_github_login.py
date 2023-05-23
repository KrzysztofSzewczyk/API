from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test_login_negative():
    """
    This test will check if we have "Incorrect username or password." when we input wrong data for login
    """
    driver = webdriver.Chrome()
    driver.get("https://github.com/login")
    id = "login_field"
    password = "password"
    element = driver.find_element(By.ID, id)
    element.send_keys("test")
    element = driver.find_element(By.ID, password)
    element.send_keys("test pass")
    element = driver.find_element(By.NAME, "commit")
    element.click()
    element = driver.find_element(By.CLASS_NAME, "js-flash-alert")
    result = element.text
    driver.quit()
    assert result == "Incorrect username or password."


def test_signup():
    """
    This test will check if we can click on Signup link (Create an account.) from login page
    """
    driver = webdriver.Chrome()
    driver.get("https://github.com/login")
    element = driver.find_element(By.XPATH, "//a[contains(@href,'signup')]")
    element.click()
    time.sleep(3) # wait for typing of the text on web page
    element = driver.find_element(By.CSS_SELECTOR, "h1")
    result = element.text
    driver.quit()
    assert result == "Welcome to GitHub! Let's begin the adventure"