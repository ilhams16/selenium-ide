from selenium import webdriver
from selenium.webdriver.common.keys import Keys

usernames = ["","","standard_user","standard_user","locked_out_user","problem_user","performance_glitch_user"]
passwords = ["","secret_sauce","","secret_sauce","secret_sauce","secret_sauce","secret_sauce"]

passed = 0
failed = 0

for i in range(0,len(usernames)):
    driver = webdriver.Edge()
    driver.get("https://www.saucedemo.com")
    print("data test",i+1)
    print("username :",usernames[i])
    print("password :",passwords[i])
    username = driver.find_element("name","user-name")
    password = driver.find_element("name","password")
    btn_login = driver.find_element("name","login-button")
    username.send_keys(usernames[i])
    password.send_keys(passwords[i])
    btn_login.click()
    print(driver.current_url)
    if driver.current_url == "https://www.saucedemo.com/inventory.html":
        passed +=1
        print("passed")
    else :
        failed +=1
        print("failed")
    driver.close()

print("pass :",passed)
print("fail :",failed)