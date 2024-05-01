from selenium import webdriver
from selenium.common import ElementNotInteractableException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(chrome_options)
driver.get("https://tinder.com/")
time.sleep(3)
login = driver.find_element(By.XPATH, '//*[@id="s-547617529"]/div/div[1]/div/main/div[1]/div/div/div/div/header/'
                                      'div/div[2]/div[2]/a')
login.click()
time.sleep(3)

login_options = driver.find_element(By.XPATH, '//*[@id="s2018968691"]/main/div[1]/div/div[1]/div/div/div[2]/div[2]'
                                              '/span/div[2]/button')
login_options.click()
time.sleep(3)

base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)

email = driver.find_element(By.XPATH, '//*[@id="email"]')
email.send_keys("pariatest2023@gmail.com")
password = driver.find_element(By.XPATH, '//*[@id="pass"]')
password.send_keys("Mytest2023")
password.send_keys(Keys.ENTER)
time.sleep(5)

driver.switch_to.window(base_window)

allow = driver.find_element(By.XPATH, '//*[@id="s2018968691"]/main/div[1]/div/div/div[3]/button[1]')
allow.click()
time.sleep(2)

accept = driver.find_element(By.XPATH, '//*[@id="s2018968691"]/main/div[2]/div/div/div[1]/div[1]/button')
accept.click()
time.sleep(1)

enable = driver.find_element(By.XPATH, '//*[@id="s2018968691"]/main/div/div/div/div[3]/button[1]')
enable.click()
time.sleep(5)

for n in range(100):
    time.sleep(10)
    try:
        dislike = driver.find_element(By.XPATH, '//*[@id="s-547617529"]/div/div[1]/div/main/div[1]/div/div/div[1]'
                                                '/div[1]/div/div[4]/div/div[2]/button')
        dislike.click()

    except ElementNotInteractableException:
        try:
            dislike_2 = driver.find_element(By.XPATH, '//*[@id="s-547617529"]/div/div[1]/div/main/div[1]/div/div/'
                                                      'div[1]/div[1]/div/div[4]/div/div[2]/button')
            dislike_2.click()
            time.sleep(3)
        except:
            not_int = driver.find_element(By.XPATH, "//*[@id='o-1687095699']/div/div/div[2]/button[2]")
            not_int.click()
            time.sleep(3)
    except:
        dislike_2 = driver.find_element(By.XPATH, '//*[@id="s-547617529"]/div/div[1]/div/main/div[1]/div/div/'
                                                      'div[1]/div[1]/div/div[4]/div/div[2]/button')
        dislike_2.click()
        time.sleep(3)

driver.quit()


