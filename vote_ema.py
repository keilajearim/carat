from selenium import webdriver
from selenium.webdriver.common.action_chains import *
import time

driver = webdriver.Chrome(service_args=['--ignore-ssl-errors=true'])
driver.implicitly_wait(30)
driver.set_window_size(1280, 720)

for i in range(10):
    driver.get("http://www.mtvema.com/ko-kr/artists/1ape33/seventeen")
    element = driver.find_element_by_css_selector(
        "#best-korea-act > div > div > div.artist-voting__category-back-side > div.artist-voting__vote-button.show")
    ActionChains(driver).move_to_element(element).click(element).perform()
    time.sleep(3)
    driver.refresh()

driver.quit()
