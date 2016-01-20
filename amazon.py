from selenium import webdriver

print('Input your Amazon email address')
userEmail = input()
print('Input your Amazon password')
userPassword = input()

browser = webdriver.Firefox()
browser.get('www.amazon.com/sign-in')

emailElem = browser.find_element_by_id('ap_email')
emailElem.send_keys (userEmail)

passwordElem = browser.find_element_by_id('ap_password')
passwordElem.send_keys (userPassword)
passwordElem.submit()