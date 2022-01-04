from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import threading 
from threading import Thread
import sys
import requests
import string    
import random 

S = 10   
ran = ''.join(random.choices(string.ascii_lowercase + string.digits, k = S))    
ree = str(ran)


def ok():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("http://discord.com/register")
    time.sleep(4)
    element = driver.find_element_by_name("email")
    element.send_keys("urmum@hotmilfsinyourarea.com");
    time.sleep(1)
    element = driver.find_element_by_name("username")
    element.send_keys(ree);
    time.sleep(1)
    element = driver.find_element_by_name("password")
    element.send_keys(ree);
    time.sleep(8)
    cope = driver.find_element_by_class_name('contents-18-Yxp').click()
    time.sleep(1)
    sys.exit()

for T in range(1):
    T=Thread(target=ok)
    T.start()
    time.sleep(10)