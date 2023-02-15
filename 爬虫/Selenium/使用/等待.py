from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
driver = webdriver.Firefox()
# 隐式等待
# implicitly_wait
driver.implicitly_wait(1)
# 由webdriver提供的方法，一旦设置，这个隐式等待会在WebDriver对象实例的整个生命周期起作用，它不针对某一个元素，是全局元素等待，即在定位元素时，需要等待页面全部元素加载完成，才会执行下一个语句。如果超出了设置时间的则抛出异常。

# 缺点：当页面某些js无法加载，但是想找的元素已经出来了，它还是会继续等待，直到页面加载完成（浏览器标签左上角圈圈不再转），才会执行下一句。某些情况下会影响脚本执行速度。


# 显示等待:WebDriverWait()
# WebDriverWait(driver, timeout, poll_frequency=0.5, ignored_exceptions=None)

# driver：浏览器驱动
# timeout：最长超时时间，默认以秒为单位
# poll_frequency：检测的间隔步长，默认为0.5s
# ignored_exceptions：超时后的抛出的异常信息，默认抛出NoSuchElementExeception异常

# 与until()或者until_not()方法结合使用
# WebDriverWait(driver, 10).until(method，message="")
# 调用该方法提供的驱动程序作为参数，直到返回值为True
# WebDriverWait(driver,10).until_not(method，message="")
# 调用该方法提供的驱动程序作为参数，直到返回值为False

# 在设置时间（10s）内，等待后面的条件发生。如果超过设置时间未发生，则抛出异常。在等待期间，每隔一定时间（默认0.5秒)，调用until或until_not里的方法，直到它返回True或False.

# WebDriverWait与expected_conditions结合使用
# wait = WebDriverWait(driver, 10, 0.5)
# element = wait.until(EC.presence_of_element_located((By.ID, "kw")), message="")
# 注意正确的写法为：presence_of_element_located((By.ID,“su”))，需要嵌套两层英文圆括号，如果省略message=“”，则By.ID外面是三层()
