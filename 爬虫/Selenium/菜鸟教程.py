from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
driver = webdriver.Firefox()
driver.get('https://www.runoob.com/python3/python3-examples.html')
try:  # 主页面获取
    wait = WebDriverWait(driver, 10, 0.5)
    wait.until(EC.presence_of_all_elements_located(
        (By.XPATH, "//a[@href='/python3/python3-helloworld.html']")), message="Python")
except:
    print('未获取到')
UrlList = driver.find_elements(By.XPATH, "//div[@id='content']/ul/li/a")
Result = []

original_window = driver.current_window_handle  # 记录主页面


def NewCreate(driver):  # 子页面数据获取
    try:
        wait = WebDriverWait(driver, 2, 0.5)
        wait.until(EC.presence_of_all_elements_located(
            (By.XPATH, "//div[@id='content']/p[1]")), message="Python")
    except:
        print(UrlList[i], '处报错')
    XName = driver.find_element(By.XPATH, "//div[@id='content']/h1")
    XInfo = driver.find_element(By.XPATH, "//div[@id='content']/p[2]")
    name = XName.get_attribute('innerHTML')
    info = XInfo.get_attribute('innerHTML').replace('\n', ' ')
    Result[i][name] = info


for i in range(len(UrlList)):  # 打开关闭子页面
    Result.append({})
    href = UrlList[i].get_attribute('href')
    driver.execute_script(f'window.open("{href}", "_blank");')
    # execute_script switch_to.window
    driver.switch_to.window(driver.window_handles[-1])

    NewCreate(driver)

    driver.close()
    driver.switch_to.window(original_window)
print(Result)
