from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

driver = webdriver.Chrome()
driver.get('https://phptravels.com/demo')

firstName = driver.find_element('xpath', '/html/body/div[1]/section[1]/div/div/div[2]/div/div/div/div/div/div/div/div[1]/input[1]')
firstName.send_keys('Filipe')

lastName = driver.find_element('xpath', '/html/body/div[1]/section[1]/div/div/div[2]/div/div/div/div/div/div/div/div[1]/input[2]')
lastName.send_keys('Paz')

businessName = driver.find_element('xpath', '/html/body/div[1]/section[1]/div/div/div[2]/div/div/div/div/div/div/div/div[1]/input[3]')
businessName.send_keys('Filipe Paz')

email = driver.find_element('xpath', '/html/body/div[1]/section[1]/div/div/div[2]/div/div/div/div/div/div/div/div[1]/input[4]')
email.send_keys('filipe_paz.28@hotmail.com') 

driver.find_element('xpath', '/html/body/div[1]/section[1]/div/div/div[2]/div/div/div/div/div/div/div/div[1]/div/div[1]/button').click()
time.sleep(2)

try:
    WebDriverWait(driver, 2).until(EC.alert_is_present(),
                                   'Timed out waiting for PA creation ' +
                                   'confirmation popup to appear.')

    alert = driver.switch_to.alert
    if(alert.text == 'Please input result number'):
        print('Test passed')
        
    alert.accept()
    print("alert accepted")
except TimeoutException:
    print("no alert")

driver.close()