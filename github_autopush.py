# importing modules
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
import os
import xlrd

# getcurrent working directory
cwd = os.getcwd()

# Now getting list of files
path = cwd + r'\source'
files = os.listdir(path)

# call browser
browser = webdriver.Chrome(executable_path=cwd + r'\configuration\chromedriver.exe')
action = ActionChains(browser)
headers = {"User-Agent": "Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11"}

# opening login credentials text file which contains login information
credentials = open(cwd + r"\configuration\login.txt", "r")
user = credentials.readlines()  # it will return a list that contains every line as individual string

#opening message for commit
msg = open(cwd + r"\configuration\commit_message.txt", "r")
msg = msg.read()

# timing for every commit
timing = open(cwd + r"\configuration\time.txt", "r")
timing = timing.read()

# Getting repository
cwd=os.getcwd()

loc =cwd+r'\configuration\repository.xlsx'
xlrd.xlsx.ensure_elementtree_imported(False, None)
xlrd.xlsx.Element_has_iter = True

wb=xlrd.open_workbook(loc)
sheet=wb.sheet_by_index(0)
url=sheet.cell_value(0,0)



# getting linkedin login page
browser.get("https://github.com/login")
username = browser.find_element_by_id('login_field')
username.send_keys(user[0])
password = browser.find_element_by_id('password')
password.send_keys(user[1])
time.sleep(1)


# for link in target_links:
browser.get(url)

for f in files:
    time.sleep(1)

    add_file = browser.find_element_by_xpath('/html/body/div[4]/div/main/div[2]/div/div/div[2]/div[1]/div[2]/details')
    add_file.click()

    time.sleep(1)

    upload = browser.find_element_by_xpath('//*[@id="repo-content-pjax-container"]/div/div[2]/div[1]/div[2]/details/div/ul/li[3]')
    upload.click()

    time.sleep(1)



    choose_file = browser.find_element_by_id('upload-manifest-files-input')
    choose_file.send_keys(cwd + f'/source/{f}')

    time.sleep(5)

    
    commit_message = browser.find_element_by_id('commit-summary-input')
    browser.execute_script("arguments[0].scrollIntoView();", commit_message)
    commit_message.send_keys(f'{msg}')

    time.sleep(1)

    commit = browser.find_element_by_xpath('//*[@id="repo-content-pjax-container"]/form/button')
    commit.click()

    time.sleep(timing)

