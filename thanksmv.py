from selenium import webdriver
from selenium.webdriver.common.action_chains import *
import time


for i in range(10):
    driver = webdriver.Chrome(service_args=['--ignore-ssl-errors=true'])
    driver.implicitly_wait(30)
    driver.set_window_size(1280, 720)
    driver.get("")
    element = driver.find_element_by_css_selector("#toggleButton")
    ActionChains(driver).move_to_element(element).click(element).perform()
    time.sleep(240)
    driver.quit()
