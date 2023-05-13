from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
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

numb1 = driver.find_element('id', 'numb1').text
numb2 = driver.find_element('id', 'numb2').text
sum = int(numb1) + int(numb2) 

result = driver.find_element('xpath', '/html/body/div[1]/section[1]/div/div/div[2]/div/div/div/div/div/div/div/div[1]/div/div[2]/div/input')
result.send_keys(sum)

driver.find_element('xpath', '/html/body/div[1]/section[1]/div/div/div[2]/div/div/div/div/div/div/div/div[1]/div/div[1]/button').click()
time.sleep(5)

try:
    element = driver.find_element('xpath', '/html/body/div[1]/section[1]/div/div/div[2]/div/div/div/div/div/div/div/div[3]/h2/strong').text
    if(element == 'Thank you!'):
        print("Test passed")
except NoSuchElementException:
    print("Test not passed")

driver.close()