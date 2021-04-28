#youtube scraper
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import time
import requests
from threading import Thread as tt
from bs4 import BeautifulSoup
import re
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from pynput.mouse import Button, Controller
import numpy as np
import clipboard
import re



global driver,x
x=""

mouse = Controller()
def strt():
    global resp,driver,x
    
    x=(input("enter the link = ")).strip()
    driver =webdriver.Chrome('C:/Project OverLoad/Automation/chromedriver.exe')
    
    #driver.get('https://www.youtube.com/')
    if (x!=None) and (x!=""):
        driver.get(x)
        resp=requests.get(x)
        if (len(driver.window_handles)>1):
            window_name = driver.window_handles[0]
            driver.switch_to.window(window_name=window_name)
            driver.close()
        
    else:
        print("Empty link \n Try again ")
        x=input("Enter the Link = ")
        try:
            driver.get(x)
            resp=requests.get(x)
            window_name = driver.window_handles[0]
            driver.switch_to.window(window_name=window_name)
            driver.close()
        except (Exception):
            pass
    if resp.status_code==200:
        
        #print('valid link')/
        
        #driver.get(x)
        time.sleep(4)    
        window_name = driver.window_handles[0]
        driver.switch_to.window(window_name=window_name)
        #driver.execute_script("window.scrollBy(0, 350)")
        time.sleep(1)
        
        anchor()
        #print(resp.content)
        #print(soup.prettify())
        
    elif resp.status_code==404:
        pass
        #repeatRJ
    else:
        print('invalid link')
    

##def get_info(saved_image, search_img):
##    global driver
##    image = cv2.imread(saved_image)  
##    template = cv2.imread(search_img)  
##    result = cv2.matchTemplate(image,template,cv2.TM_CCOEFF_NORMED)  
##    print (np.unravel_index(result.argmax(),result.shape))
##
##    #return location of image wrt to screenshot
##    return ((np.unravel_index(result.argmax(),result.shape)))
def preser():
    from pynput.keyboard import Key, Controller
    keyboard=Controller()
    keyboard.press('f')

def save_it(text):
    global driver,nme,belna
    
    f=open(str(belna+".txt"),"w+")
    f.write(text)
    f.close()

def run(string):
    global belna
    ar='[@!#$%^&*()<>?/\|}{~":]'
    # Make own character set and pass 
    # this as argument in compile method
    regex = re.compile(ar)
    
    # Pass the string in search 
    # method of regex object.    
    if(regex.search(string) == None):
        belna=string
        return string.strip()
          
    else:
        #strt replacing
        string=string.strip()
        loc=regex.search(string).span()
        dd=string
        string=dd[0:loc[0]]+'_'+dd[loc[1]:len(string)]
        belna=string
        #print(str(regex.search(string).span()))
        run(string)
        
def injector():
##    global driver
##    var mouseEvent = document.createEvent("MouseEvents");
##    mouseEvent.initMouseEvent("contextmenu", true, true, null);
##    $('.html5-video-player').dispatchEvent(mouseEvent);
##    $('.ytp-popup.ytp-contextmenu').querySelector('.ytp-panel-menu').querySelectorAll('.ytp-menuitem')[4].click()
##    
##
    pass
def anchor():
    #resp=requests.get(x)
    global driver,nme,belna

    
    players = driver.find_element_by_id('movie_player')
    time.sleep(5)
    driver.maximize_window()
    #print(players)
    #keyboard.press(Key.alt)
    preser()
    action=ActionChains(driver)
    action.context_click(players).perform()
    time.sleep(10)
    pl=driver.find_element_by_xpath("//*[contains(text(),'Copy debug info')]").click()
    #players.click()
    
    nme=driver.find_element_by_xpath('//*[@id="container"]/h1/yt-formatted-string')
    nme=nme.text
    nme=run(nme)
    print("File Name = "+belna+'.txt')
    print()
    
    #driver.execute_script(injector())
    
    mouse.position = (350, 400)
    mouse.press(Button.right)
    mouse.release(Button.right)
    
    
    #location=get_info(saved_image,search_img)
    #mouse.position = location[1],location[0]
    mouse.move(10,200)
    time.sleep(1)
    mouse.press(Button.left)
    mouse.release(Button.left)
    time.sleep(3)
    text = clipboard.paste()
    print(text)
    save_it(text)
    time.sleep(2)
    #print(location)


    #print(players)
    driver.quit()
    #print('The number of Contents Present are '+str(big_str))
    #wrk_str=str(big_str)
    #driver.quit()
    strt()
    
                            
##    except Exception as e:
##        print(str(e))
##        print('No Contents Found on This Page')

    
strt()


