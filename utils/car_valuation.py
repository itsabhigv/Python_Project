from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random

class CarValuation:
    def __init__(self):
        self.driver = webdriver.Chrome()  

    def fetch_valuation(self, reg_number):
       
        try:
            self.driver.get("https://www.webuyanycar.com/")
            mileage = random.randint(5000, 100000)
            myElem = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.ID, 'vehicleReg')))
            myElem.send_keys(reg_number)
            search_input = self.driver.find_element(By.XPATH, '//input[@id="Mileage"]')
            search_input.send_keys(mileage)
            search_button = self.driver.find_element(By.XPATH, '//button[@id="btn-go"]')
            search_button.click()
            manufacturer = WebDriverWait(self.driver,30).until(EC.presence_of_element_located((By.XPATH,"//div[@class='d-table-cell heading'][normalize-space()='Manufacturer:']/following-sibling::div"))).get_attribute("innerText")
            model = WebDriverWait(self.driver,30).until(EC.presence_of_element_located((By.XPATH,"//div[@class='d-table-cell heading'][normalize-space()='Model:']/following-sibling::div"))).get_attribute("innerText")
            year = WebDriverWait(self.driver,30).until(EC.presence_of_element_located((By.XPATH,"//div[@class='d-table-cell heading'][normalize-space()='Year:']/following-sibling::div"))).get_attribute("innerText")
            return {
                "VARIANT_REG" :reg_number,
                "MAKE":manufacturer,
                "MODEL":model,
                "YEAR": year
            }
        except TimeoutException: 
            print ("Loading took too much time!")
        self.driver.quit()


class values:
    def __init__(self, VARIANT_REG,MAKE,MODEL,YEAR):
        self.VARIANT_REG = VARIANT_REG
        self.MAKE = MAKE
        self.MODEL = MODEL
        self.YEAR = YEAR
    