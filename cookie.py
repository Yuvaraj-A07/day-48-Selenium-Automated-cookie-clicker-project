from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

minute = 5 * 60

cookie = driver.find_element(By.ID, value="cookie")
c_per_s = driver.find_element(By.ID, value="cps")
money = driver.find_element(By.ID, value="money")
cursor = driver.find_element(By.ID, value="buyCursor")
grandma = driver.find_element(By.ID, value="buyGrandma")

cursor_count = int(cursor.text.split()[2])
grandma_count = int(grandma.text.split()[2])

while minute > 0:
    cookie = driver.find_element(By.ID, value="cookie")
    c_per_s = driver.find_element(By.ID, value="cps")
    money = driver.find_element(By.ID, value="money")
    cursor = driver.find_element(By.ID, value="buyCursor")
    grandma = driver.find_element(By.ID, value="buyGrandma")

    cursor_count = int(cursor.text.split()[2])
    grandma_count = int(grandma.text.split()[2])

    cookie.click()
    if minute % 5 == 0:
        if grandma_count <= int(money.text):
            grandma.click()
        if cursor_count <= int(money.text):
            cursor.click()
    minute -= 1

print(c_per_s.text)

# print(cursor_count)
# print(grandma_count)
