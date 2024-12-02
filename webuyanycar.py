from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from utils.file_handler import FileHandler
import random
# Read car_input.txt to extract vehicle registration numbers

# Implement the extraction logic based on the provided sample text

# Open a browser using Selenium
browser = webdriver.Chrome()


# Extracted registration numbers to iterate over
registration_numbers = ['AD58VNF']

for reg_number in registration_numbers:
    # Navigate to webuyanycar or the car valuation website
    browser.get('https://www.webuyanycar.com/')
    mileage = random.randint(5000, 100000)
    try:
        myElem = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.ID, 'vehicleReg')))
        myElem.send_keys(reg_number)
        search_input = browser.find_element(By.XPATH, '//input[@id="Mileage"]')
        search_input.send_keys(mileage)
        search_button = browser.find_element(By.XPATH, '//button[@id="btn-go"]')
        search_button.click()
        manufacturer = WebDriverWait(browser,30).until(EC.presence_of_element_located((By.XPATH,"//div[@class='d-table-cell heading'][normalize-space()='Manufacturer:']/following-sibling::div"))).get_attribute("innerText")
        model = WebDriverWait(browser,30).until(EC.presence_of_element_located((By.XPATH,"//div[@class='d-table-cell heading'][normalize-space()='Model:']/following-sibling::div"))).get_attribute("innerText")
        year = WebDriverWait(browser,30).until(EC.presence_of_element_located((By.XPATH,"//div[@class='d-table-cell heading'][normalize-space()='Year:']/following-sibling::div"))).get_attribute("innerText")
        print(manufacturer,model,year)
    except TimeoutException: 
        print ("Loading took too much time!")

    # Input the registration number and perform the car valuation search

    # search_input = browser.find_element(By.ID,"vehicleReg")
    # search_input.send_keys(reg_number)
    # search_input = browser.find_element_by_xpath('//input[@id="Mileage"]')
    # search_input.send_keys(mileage)
    # search_button = browser.find_element_by_xpath('//button[@id="btn-go"]')
    # search_button.click()

    # Extract the valuation details from the website
    # Implement the logic to extract the make, model, and other details

    # Compare the extracted details with the expected data from car_output.txt
    # Implement the comparison logic and highlight/fail the test for any mismatches

# Close the browser
browser.quit()