#Eric bank with function

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


driver = webdriver.Chrome()
driver.get("http://sampleapp.tricentis.com/101/app.php")
driver.maximize_window()
assert "Enter Vehicle Data" in driver.title, "title is incorrect"
print(driver.title)

def SelectItem(comboboxId, comboboxValue):
 combobox = Select(driver.find_element_by_id(comboboxId))
 combobox.select_by_value(comboboxValue)
 print(comboboxId + ": " + comboboxValue)

def SetText(textElement, textToSend):
 element = driver.find_element_by_id(textElement)
 element.clear()
 element.send_keys(textToSend)
 print(textElement + "updated with : " + textToSend)

def ScrollToObjectAndClick(objectId):
 objectToScrollAndClick = driver.find_element_by_id(objectId)
 driver.execute_script('arguments[0].scrollIntoView(true);', objectToScrollAndClick)
 time.sleep(2)
 objectToScrollAndClick.click()
 time.sleep(2)
 print("Clicked on " + objectId)

def SelectRadioButton(valueOfRadioButton):
 radiobutton = driver.find_element_by_xpath(".//input[@type='radio' and @value='" + valueOfRadioButton + "']")
 driver.execute_script("arguments[0].click();", radiobutton)
 print("selected radio button: " + valueOfRadioButton)

def SelectCheckBox(valueOfCheckBox):
 checkbox = driver.find_element_by_xpath(".//input[@type='checkbox' and @id='" + valueOfCheckBox + "']")
 if checkbox.get_attribute('checked') is not None:
  print("Checkbox: " + valueOfCheckBox + " is already checked")
 else:
  driver.execute_script("arguments[0].click();", checkbox)
 print("Checkbox: " + valueOfCheckBox + " is checked")


driver.find_element_by_id("nav_automobile").click()
print("Getting quote for following car - ")

assert WebDriverWait(driver, 10).until(EC.presence_of_element_located(
 (By.ID, "entervehicledata"))).text.split("\n")[0] in "Enter Vehicle Data", "Not in Vehicle Data Section"
SelectItem("make", "Audi")
SetText("engineperformance", "1500")
SetText("dateofmanufacture", "01/01/2018")
SelectItem("numberofseats", "5")
SelectItem("fuel", "Petrol")
SetText("listprice", "35000")
SetText("annualmileage", "20000")
ScrollToObjectAndClick("nextenterinsurantdata")

assert WebDriverWait(driver, 10).until(EC.presence_of_element_located(
 (By.ID, "enterinsurantdata"))).text.split("\n")[0] in "Enter Insurant Data", "Not in Vehicle Insurant Section"

print("Navigating back to validate if the mileage filled still shows as expected")
ScrollToObjectAndClick("preventervehicledata")

assert WebDriverWait(driver, 10).until(EC.presence_of_element_located(
 (By.ID, "annualmileage"))).get_attribute("value") in "20000", "Mileage is not as expected"

ScrollToObjectAndClick("nextenterinsurantdata")
ScrollToObjectAndClick("firstname")
SetText("firstname", "Dhar")
SetText("lastname", "Shanmu")
SetText("birthdate", "09/08/1984")
SelectRadioButton("Male")
SelectItem("country", "Netherlands")
SetText("zipcode", "5627")
SelectItem("occupation", "Employee")
SelectCheckBox("other")
ScrollToObjectAndClick("nextenterproductdata")

assert WebDriverWait(driver, 10).until(EC.presence_of_element_located(
 (By.ID, "enterproductdata"))).text.split("\n")[0] in "Enter Product Data", "Not in Vehicle Product Section"
SetText("startdate", "07/01/2022")
SelectItem("insurancesum", "5000000")
SelectItem("meritrating", "Bonus 1")
SelectItem("damageinsurance", "Partial Coverage")
SelectCheckBox("EuroProtection")
SelectItem("courtesycar", "Yes")
ScrollToObjectAndClick("nextselectpriceoption")

assert WebDriverWait(driver, 10).until(EC.presence_of_element_located(
 (By.ID, "selectpriceoption"))).text.split("\n")[0] in "Select Price Option", "Not in Select Price Section"
SelectRadioButton("Gold")

viewQuote = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
 (By.XPATH, "//*[@id=\"quote-sub-container\"]/div/div[1]/div/div[2]"))).get_attribute("innerText")

assert viewQuote in "VIEW QUOTE", "VIEW QUOTE not visible"
downloadQuote = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
 (By.XPATH, "//*[@id=\"quote-sub-container\"]/div/div[2]/div/div[2]"))).get_attribute("innerText")

assert downloadQuote in "DOWNLOAD QUOTE", "Download QUOTE not visible"
print ("View and Download Quote visible")

pricetable = driver.find_element_by_xpath("//*[@id=\"priceTable\"]/thead/tr")
pricetableHeaders = pricetable.find_elements_by_tag_name("th")

for eachHeader in pricetableHeaders:
 print (eachHeader.text)

priceTableBody = driver.find_element_by_xpath("//*[@id=\"priceTable\"]/tbody").find_elements_by_tag_name("tr")

for eachRow in priceTableBody:
 priceTableRow = eachRow.find_elements_by_tag_name("td")
 print ("***")

for eachColumn in priceTableRow:
  print (eachColumn.text)
  print ("---")

driver.close()

#Webhook payload url is changed so commiting again

#Commiting with latest webhook
