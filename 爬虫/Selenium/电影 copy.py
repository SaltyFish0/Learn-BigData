from webbrowser import get
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

MainUrl = 'https://spa2.scrape.center/'

driver = webdriver.Firefox()

driver.get(MainUrl)
original_window = driver.current_window_handle

try:
    wait1 = WebDriverWait(driver, 10, 0.5)
    wait1.until(EC.presence_of_element_located(
        (By.XPATH, "/html/body/div[1]/div[2]/div[1]/div[1]/div[1]/div/div/div[2]/a/h2")))
except:
    print(1)


def getA():
    Lista = driver.find_elements(
        By.XPATH, '//div[contains(@class,"el-col-md-4")]/a')
    return Lista


def NewCreate(driver):  # 子页面数据获取
    try:
        wait = WebDriverWait(driver, 2, 0.5)
        wait.until(EC.presence_of_all_elements_located(
            (By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/div/div[1]/div/div[2]/div[4]/h3")))
    except:
        print('')
    XName = driver.find_element(
        By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/div/div[1]/div/div[2]/a/h2")
    XInfo = driver.find_element(
        By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/div/div[1]/div/div[2]/div[4]/p")

    print(XName.get_attribute('innerHTML'))
    print(XInfo.get_attribute('innerHTML'))


count = 0
Lista = getA()
for i in range(len(Lista)):
    NewHref = Lista[i].get_attribute('href')
    driver.execute_script(f'window.open("{NewHref}", "_blank");')
    driver.switch_to.window(driver.window_handles[-1])
    NewCreate(driver)

    driver.close()
    driver.switch_to.window(original_window)

    count += 1
    print(count)
    print(len(Lista))
    if(count == len(Lista)):
        next = driver.find_element(
            By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/div/div/button[2]/i")
        Lista = getA()


def Main():
    print()
