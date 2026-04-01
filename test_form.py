from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
import time

# Setup driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("file:///C:/ProgramData/Jenkins/.jenkins/workspace/Selenium/index.html")
driver.maximize_window()

time.sleep(2)

print("Page Title:", driver.title)

# Function to clean text (remove emojis)
def clean_text(text):
    return text.encode('ascii', 'ignore').decode()

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

# ===================== TEST CASES ===================== #

# VALID
fill_valid_data()
driver.find_element(By.XPATH, "//button[text()='Submit']").click()
time.sleep(2)
msg = clean_text(driver.find_element(By.ID, "message").text)
print("Valid Submission:", msg)

# INVALID EMAIL
driver.find_element(By.XPATH, "//button[text()='Reset']").click()
time.sleep(2)

fill_valid_data()
driver.find_element(By.ID, "email").clear()
driver.find_element(By.ID, "email").send_keys("wrong-email")

driver.find_element(By.XPATH, "//button[text()='Submit']").click()
time.sleep(2)
msg = clean_text(driver.find_element(By.ID, "message").text)
print("Invalid Email:", msg)

# INVALID MOBILE
driver.find_element(By.XPATH, "//button[text()='Reset']").click()
time.sleep(2)

fill_valid_data()
driver.find_element(By.ID, "mobile").clear()
driver.find_element(By.ID, "mobile").send_keys("123")

driver.find_element(By.XPATH, "//button[text()='Submit']").click()
time.sleep(2)
msg = clean_text(driver.find_element(By.ID, "message").text)
print("Invalid Mobile:", msg)

# EMPTY FIELDS
driver.find_element(By.XPATH, "//button[text()='Reset']").click()
time.sleep(2)

driver.find_element(By.XPATH, "//button[text()='Submit']").click()
time.sleep(2)
msg = clean_text(driver.find_element(By.ID, "message").text)
print("Empty Fields:", msg)

# CLOSE DRIVER (NO input() here!)
driver.quit()