# -*- coding: utf-8 -*-
# @Author: Halloweenwx
# @Date:   2019-11-14 19:58:51
# @Last Modified by:   Halloweenwx
# @Last Modified time: 2019-11-16 14:22:38

import re
from urllib import parse
import requests
from bs4 import BeautifulSoup
import bs4
from lxml import etree
from selenium import webdriver
import time
import json

def geturl(title_arr):
    res_arr = []
    res = {}

    times = 0
    driver = webdriver.Chrome('/Users/Halloween/Downloads/chrome/chromedriver')
    with open('../transformed/title_res.txt','a') as o:
        # for title in title_arr:
        #     o.write(title+'\n')
        res['title'] = title

        times += 1
        url = 'https://apps.webofknowledge.com/UA_GeneralSearch_input.do?product=UA&search_mode=GeneralSearch&SID=6A1wQZxeRZ2F9w4hAYT&preferencesSaved='
        driver.get(url)
        driver.find_element_by_id("clearIcon1").click()#点击清除输入框内原有缓存地址
        driver.find_element_by_id("value(input1)").send_keys(title)#模拟在输入框输入入藏号
        
        driver.execute_script("document.querySelector(\"#select1\").selectedIndex = 1")
        
        driver.find_elements_by_xpath("//*[@id=\"searchCell1\"]/span[1]/button")[0].click()
        
        try:
            driver.find_elements_by_xpath("//*[@id=\"RECORD_1\"]/div[3]/div[1]/div/a/value")[0].click()  
            driver.find_elements_by_xpath("//*[@id=\"exportTypeName\"]")[0].click()
            print(times)
            if times == 1:
                driver.find_elements_by_xpath("//*[@id=\"saveToMenu\"]/li[3]/a")[0].click()
                
                # driver.find_elements_by_xpath("//*[@id=\"saveToMenu\"]/li[3]/a")[0].click()
                # driver.find_elements_by_xpath("/html/body/div[1]/div[26]/div/div/div/div[3]/div/div[1]/ul/li/button")[0].click()
            
            # driver.find_elements_by_xpath("/html/body/div[11]/div[2]/form/div[2]/div[2]/div/span/span[1]/span")[0].setAttribute("aria-activedescendant", "select2-bib_fields-result-ccb8-HIGHLY_CITED HOT_PAPER OPEN_ACCESS PMID USAGEIND AUTHORSIDENTIFIERS ACCESSION_NUM FUNDING SUBJECT_CATEGORY JCR_CATEGORY LANG IDS PAGEC SABBR CITREFC ISSN PUBINFO KEYWORDS CITTIMES ADDRS CONFERENCE_SPONSORS DOCTYPE CITREF ABSTRACT CONFERENCE_INFO SOURCE TITLE AUTHORS  ");
            # driver.find_elements_by_xpath("//*[@id=\"bib_fields\"]")[0].select_by_value('HIGHLY_CITED HOT_PAPER OPEN_ACCESS PMID USAGEIND AUTHORSIDENTIFIERS ACCESSION_NUM FUNDING SUBJECT_CATEGORY JCR_CATEGORY LANG IDS PAGEC SABBR CITREFC ISSN PUBINFO KEYWORDS CITTIMES ADDRS CONFERENCE_SPONSORS DOCTYPE CITREF ABSTRACT CONFERENCE_INFO SOURCE TITLE AUTHORS  ')
            
            # loc = driver.find_elements_by_xpath("//*[@id=\"select2-saveOptions-container\"]")[0]
            
            # loc = driver.find_elements_by_xpath("//*[@id=\"select2-saveOptions-result-ux4r-tabMacUTF8\"]")[0]
            # ActionChains(driver).move_to_element(loc).click(loc).perform()
            
            driver.execute_script("document.querySelector(\"#bib_fields\").selectedIndex = 3")
            driver.execute_script("document.querySelector(\"#saveOptions\").selectedIndex = 3")

            driver.find_elements_by_xpath("//*[@id=\"exportButton\"]")[0].click()
            
            # driver.find_elements_by_xpath("//*[@id=\"exportButton\"]")[0].click()
            # url1 = driver.current_url 
            res["wos"] = True
            res_arr.append(dict(res))
            with open('../transformed/title_res.txt','w+') as o:
                o.write(title)
        except Exception as e:
            print(e)
            times -= 1
            print("FAIL :"+title)
            res["wos"] = False
            res_arr.append(dict(res))
        else:
            continue
    
    return res_arr

def main():
    res_arr = []
    with open('../transformed/title.txt','r') as f:
        title_arr = json.load(f)

        print(geturl(title_arr))
    


if __name__ == '__main__':
    main()
