from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select   # ✅ IMPORTANT
from webdriver_manager.chrome import ChromeDriverManager
import time

# Launch browser
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# ✅ CHANGE THIS PATH (VERY IMPORTANT)
driver.get("file:///D:/Selenium/index.html")

driver.maximize_window()
time.sleep(3)

# ------------------------------
# TEST 1: Page Open
# ------------------------------
print("Page Title:", driver.title)

# ------------------------------
# FUNCTION: Fill Valid Data
# ------------------------------
def fill_valid_data():
    driver.find_element(By.ID, "name").clear()
    driver.find_element(By.ID, "name").send_keys("Ojas Charjan")

    driver.find_element(By.ID, "email").clear()
    driver.find_element(By.ID, "email").send_keys("ojascharjan24@gmail.com")

    driver.find_element(By.ID, "mobile").clear()
    driver.find_element(By.ID, "mobile").send_keys("9529319989")

    # ✅ Dropdown fix
    Select(driver.find_element(By.ID, "department")).select_by_visible_text("CSE")

    driver.find_element(By.XPATH, "//input[@value='Male']").click()

    driver.find_element(By.ID, "comments").clear()
    driver.find_element(By.ID, "comments").send_keys(
        "This form is very good and helps students provide useful feedback easily"
    )

# ------------------------------
# TEST 2: Valid Submission
# ------------------------------
fill_valid_data()
driver.find_element(By.XPATH, "//button[text()='Submit']").click()
time.sleep(2)

print("Valid Submission:", driver.find_element(By.ID, "message").text)

# ------------------------------
# TEST 3: Reset Button
# ------------------------------
driver.find_element(By.XPATH, "//button[text()='Reset']").click()
time.sleep(2)

# ------------------------------
# TEST 4: Invalid Email
# ------------------------------
fill_valid_data()
driver.find_element(By.ID, "email").clear()
driver.find_element(By.ID, "email").send_keys("wrong-email")

driver.find_element(By.XPATH, "//button[text()='Submit']").click()
time.sleep(2)

print("Invalid Email:", driver.find_element(By.ID, "message").text)

# ------------------------------
# TEST 5: Invalid Mobile
# ------------------------------
driver.find_element(By.XPATH, "//button[text()='Reset']").click()
time.sleep(2)

fill_valid_data()
driver.find_element(By.ID, "mobile").clear()
driver.find_element(By.ID, "mobile").send_keys("123")

driver.find_element(By.XPATH, "//button[text()='Submit']").click()
time.sleep(2)

print("Invalid Mobile:", driver.find_element(By.ID, "message").text)

# ------------------------------
# TEST 6: Empty Fields
# ------------------------------
driver.find_element(By.XPATH, "//button[text()='Reset']").click()
time.sleep(2)

driver.find_element(By.XPATH, "//button[text()='Submit']").click()
time.sleep(2)

print("Empty Fields:", driver.find_element(By.ID, "message").text)

# ------------------------------
# CLOSE
# ------------------------------
input("Press Enter to close...")
driver.quit()