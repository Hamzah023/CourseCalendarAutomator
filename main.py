from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

username = 'himran02@uoguelph.ca'
password = ''

url = 'https://colleague-ss.uoguelph.ca/Student/Planning/DegreePlans/PrintSchedule?termId=F24&hideProxyDialog=false'


driver = webdriver.Chrome()

driver.get(url)

time.sleep(30) #this works by waiting for 100 seconds

#wait = WebDriverWait(driver, 600) #this works by waiting for the page to load for 100 seconds, it can be converted to

#popup = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@role="heading" and @aria-level="1"]')))


usernameField = driver.find_element(By.ID, 'i0116') #this works by finding the username field which is the input field and the ID is i0116
#passwordField = driver.find_element(By.ID, 'password')
#submit_button = driver.find_element(By.ID, 'submit')

usernameField.send_keys(username) #this works by sending the keys to the username field which is the input field, keys are the username
time.sleep(30) 
#passwordField.send_keys(password) #this works by sending the keys to the password field which is the input field, keys are the password

#submit_button.click() #this works by clicking the submit button which is the input field

#wait.until(EC.presence_of_element_located((By.ID, 'print-schedule-details-header'))) #this works by waiting until the title is Student Planning - University of Guelph

print(driver.title)