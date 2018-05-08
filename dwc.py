from selenium import webdriver
from selenium.webdriver.common.action_chains import *
import time


for i in range(5):
    driver = webdriver.Chrome(service_args=['--ignore-ssl-errors=true'])
    driver.implicitly_wait(30)
    driver.set_window_size(1280, 720)
    driver.get("https://www.youtube.com/watch?v=zEkg4GBQumc")
    element = driver.find_element_by_css_selector("#toggleButton")
    ActionChains(driver).move_to_element(element).click(element).perform()
    time.sleep(240)
    driver.quit()
