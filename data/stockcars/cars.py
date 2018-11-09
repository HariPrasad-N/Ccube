from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver import TouchActions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from time import ctime
import re
import os

def get_links1(links):
        for ln in links:
                driver.get(ln)
                car=driver.find_element_by_class_name("titleFont").get_attribute("innerHTML").replace(" ","_")
                td1=driver.find_elements_by_class_name("slide")                
                td=driver.find_elements_by_class_name("text")
                p=re.compile(".*side.*view.*")
                j=0
                i=0
                for ele in td:
                        try:
                                text=ele.find_element_by_xpath("a").get_attribute("innerHTML")
                                m=p.match(text)
                                #print(text,ele.find_element_by_xpath("..").find_element_by_xpath("..").find_element_by_xpath("//tr[1]/td[1]/a/img").get_attribute("href"))
                                img=td1[j].find_element_by_xpath("a/img").get_attribute("src")
                                if m!=None:
                                        i+=1
                                        #os.system("wget -O {0} {1}".format(car+"_"+str(i),img))
                                        print(car+"_"+str(i),img)
                        except:
                                pass
                        j+=1
                        

                

def get_links(link):
        links=[]
        for ln in link:
                driver.get(ln)
                if len(driver.find_elements_by_class_name("thumb_links_cart psCartAddLink"))!=0:
                        links.append(ln)
                else:
                        td=driver.find_elements_by_class_name("slide")
                        for ele in td:
                                try:
                                        links.append(ele.find_element_by_xpath("a").get_attribute("href"))   
                                except:
                                        pass
                       
        get_links1(links)
                                

driver=webdriver.Firefox()
driver.get("http://www.izmostock.com/car-stock-photos-by-brand")
div=driver.find_element_by_id("page-content")
brands=div.find_elements_by_xpath("//div/div[@id='by_brand']/a")
links=[]
for ele in brands:
        links.append(ele.get_attribute("href"))

get_links(links)
        


