from selenium import webdriver                          # output done

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


import time

options = Options()

options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(executable_path=r"C:/Users/Lenovo/Downloads/chromedriver_win32/chromedriver.exe",chrome_options=options)



driver.get('https://docs.google.com/forms/d/e/1FAIpQLSdGHOt20EK9t8Ccfa2jBalyUEVi02gU6m5JEyGwFpePe8rbbQ/viewform?vc=0&c=0&w=1&flr=0')

time.sleep(2)



RadioButtonPeriod = driver.find_element("xpath" , '//*[@id="i5"]/div[3]/div')
RadioButtonPeriod.click()
time.sleep(1)

RadioButtonP = driver.find_element("xpath" , '//*[@id="i21"]/div[3]/div')
RadioButtonP.click()
time.sleep(1)


FirstName = ' Het patel'

# name = driver.find_elements_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')   # Error  selenium new version 

name = driver.find_element("xpath" , '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')      # selenium new version choose by xpath 
name.send_keys(FirstName)
time.sleep(1)


date = driver.find_element("xpath" , '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/input')
date.send_keys('07/10/2022')
time.sleep(1)



# drop = driver.find_element("xpath" , '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div[1]/div[1]/span').click()
drop = driver.find_element("xpath" , '/html/body/div/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div').click()
time.sleep(1)   # output done

drop = driver.find_element("xpath" , '/html/body/div/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[2]/div[3]').click()
time.sleep(1)   # output done


submit = driver.find_element("xpath" , '/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div').click()




# Drop_down  try 

# drop = driver.find_element("xpath" , '/html/body/div/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[2]/div[3]').click()
# drop = driver.find_element("xpath" , '/html/body/div/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[2]/div[4]').click()
# drop = driver.find_element("xpath" , '/html/body/div/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[2]/div[5]').click()



# /html/body/div/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]

# /html/body/div/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div

# /html/body/div/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]

# /html/body/div/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div[1]

# /html/body/div/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div[1]/div[1]

# /html/body/div/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div[1]/div[3]

# /html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div[1]/div[3]

# /html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div[1]
