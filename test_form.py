from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("file:///C:/ProgramData/Jenkins/.jenkins/workspace/Selenium/index.html")
driver.maximize_window()

time.sleep(2)

print("Page Title:", driver.title)

def fill_valid_data():
    driver.find_element(By.ID, "name").clear()
    driver.find_element(By.ID, "name").send_keys("Ojas Charjan")

    driver.find_element(By.ID, "email").clear()
    driver.find_element(By.ID, "email").send_keys("ojascharjan24@gmail.com")

    driver.find_element(By.ID, "mobile").clear()
    driver.find_element(By.ID, "mobile").send_keys("9529319989")

    Select(driver.find_element(By.ID, "department")).select_by_visible_text("CSE")

    driver.find_element(By.XPATH, "//input[@value='Male']").click()

    driver.find_element(By.ID, "comments").clear()
    driver.find_element(By.ID, "comments").send_keys(
        "This form is very good and helps students provide useful feedback easily"
    )

# VALID
fill_valid_data()
driver.find_element(By.XPATH, "//button[text()='Submit']").click()
time.sleep(2)
print("Valid Submission:", driver.find_element(By.ID, "message").text)

# INVALID EMAIL
driver.find_element(By.XPATH, "//button[text()='Reset']").click()
time.sleep(2)

fill_valid_data()
driver.find_element(By.ID, "email").clear()
driver.find_element(By.ID, "email").send_keys("wrong-email")

driver.find_element(By.XPATH, "//button[text()='Submit']").click()
time.sleep(2)
print("Invalid Email:", driver.find_element(By.ID, "message").text)

# INVALID MOBILE
driver.find_element(By.XPATH, "//button[text()='Reset']").click()
time.sleep(2)

fill_valid_data()
driver.find_element(By.ID, "mobile").clear()
driver.find_element(By.ID, "mobile").send_keys("123")

driver.find_element(By.XPATH, "//button[text()='Submit']").click()
time.sleep(2)
print("Invalid Mobile:", driver.find_element(By.ID, "message").text)

# EMPTY
driver.find_element(By.XPATH, "//button[text()='Reset']").click()
time.sleep(2)

driver.find_element(By.XPATH, "//button[text()='Submit']").click()
time.sleep(2)
print("Empty Fields:", driver.find_element(By.ID, "message").text)

# CLOSE DRIVER (IMPORTANT)
driver.quit()