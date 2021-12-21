#Eric bank without function

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

# (executable_path="c:\selenium webdrivers\chromedriver.exe")

driver = webdriver.Chrome()
driver.get('http://sampleapp.tricentis.com/101/app.php')

#element=driver.find_element_by_name()

element=driver.find_element_by_id('nav_automobile')
element.click()

make = Select(driver.find_element_by_id('make'))
make.select_by_index(1)
# make.select_by_visible_text('Audi')


performance= driver.find_element_by_name('[kW]')
performance.send_keys("1500")

manufactureDate = driver.find_element_by_id('dateofmanufacture')
manufactureDate.send_keys('09/21/2010')

numberSeats=Select(driver.find_element_by_id('numberofseats'))
numberSeats.select_by_index(5)

fuelType=Select(driver.find_element_by_id('fuel'))
fuelType.select_by_index(3)

listPrice = driver.find_element_by_id("listprice")
listPrice.send_keys("2000")

license=driver.find_element_by_id('licenseplatenumber')
license.send_keys("DL2020")

aMillage=driver.find_element_by_id('annualmileage')
aMillage.send_keys("2000")

nextButton=driver.find_element_by_id('nextenterinsurantdata')
nextButton.click()

fName=driver.find_element_by_id('firstname')
fName.send_keys("Aaaaa")

lName=driver.find_element_by_id('lastname')
lName.send_keys('Bbbbb')

bDate = driver.find_element_by_id('birthdate')
bDate.send_keys('05/25/1999')


# gender.select_by_index(1)

# to use in Radio Button $ list
gender = driver.find_element_by_id('gendermale')
driver.execute_script('arguments[0].click();',gender)


street=driver.find_element_by_id('streetaddress')
street.send_keys("Eindhoven")

country = Select(driver.find_element_by_id('country'))
country.select_by_visible_text('Netherlands')

zipcode=driver.find_element_by_id('zipcode')
zipcode.send_keys("1002")


city=driver.find_element_by_id('city')
city.send_keys("eindhoven")


occ = Select(driver.find_element_by_id('occupation'))
occ.select_by_index(3)

hobbies = driver.find_element_by_id('skydiving')
driver.execute_script('arguments[0].click();',hobbies)

website=driver.find_element_by_id('website')
website.send_keys("https://stackoverflow.com/questions")


preButton=driver.find_element_by_id('preventervehicledata')
preButton.click()

preAnnual=driver.find_element_by_id("annualmileage")
assert preAnnual.get_attribute("value") == "2000"
print("Value from Previouse Page is Correct")

nextButton=driver.find_element_by_id('nextenterinsurantdata')
nextButton.click()


next2Button=driver.find_element_by_id('nextenterproductdata')
next2Button.click()

startdate=driver.find_element_by_id('startdate')
startdate.send_keys('06/02/2022')

insurancesum= Select(driver.find_element_by_id('insurancesum'))
insurancesum.select_by_index(2)

meritrating = Select(driver.find_element_by_id('meritrating'))
meritrating.select_by_index(2)

damageinsurance=Select(driver.find_element_by_id('damageinsurance'))
damageinsurance.select_by_index(2)

optionalProducts = driver.find_element_by_id('EuroProtection')
driver.execute_script('arguments[0].click();',optionalProducts)

courtesycar = Select(driver.find_element_by_id('courtesycar'))
courtesycar.select_by_index(1)

nextSelection =driver.find_element_by_id('nextselectpriceoption')
nextSelection.click()

selectoption = driver.find_element_by_id('selectgold')
driver.execute_script('arguments[0].click();',selectoption)

nextButton=driver.find_element_by_id("nextsendquote")
nextButton.click()

driver.execute_script()

#gender.is_selected()
#
#print(driver.title)
#assert "Tricentis Vehicle Insurance" in driver.title
#target = driver.find_element_by_id('get_camper')
#target=driver.find_element_by_xpath('//*[@id="get_camper"]')
#driver.execute_script('arguments[0].scrollIntoView(true);', target)
#time.sleep(2)
#target.click()


#actions = ActionChains(driver)
#target = driver.find_element_by_id('get_camper')
#actions.perform()
#target.click()

driver.close()