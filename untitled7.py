# -*- coding: utf-8 -*-
"""Untitled7.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1C9BNveMP9m-IGNDCFUpSBYD13TDykgeX
"""

#! /usr/bin/python3

diaries = range(1,101)
years = range(2000,2021)

import requests
import pandas as pd 
from bs4 import BeautifulSoup as bs

casesData = []




cookies = {
    'BNI_persistence': 'NUIffASvAES-Jfr7DCxSQMtFVHFbIE1c9pth3xH4rA1jUKtiDGvBUg0z-lEWCRTcSfIuUWPWSAqd_uVdJtAGFw==',
    'has_js': '1',
    'SESS3e237ce09ea0ff0fb3e315573005c968': 'PfnwAuTyxt_eHcRtU9n23fMhK2SW43WgRjQDMWwovFY',
}

headers = {
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'sec-ch-ua': '"Google Chrome";v="87", "\\"Not;A\\\\Brand";v="99", "Chromium";v="87"',
    'Accept': '*/*',
    'DNT': '1',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': 'https://main.sci.gov.in',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://main.sci.gov.in/case-status',
    'Accept-Language': 'en-US,en;q=0.9,hi-IN;q=0.8,hi;q=0.7,da;q=0.6',
}





def read_data(diary,year):
    data = {
    'd_no': diary,
    'd_yr': year,
    'ansCaptcha': '393993939'
    }
    response = requests.post('https://main.sci.gov.in/php/case_status/case_status_process.php', headers=headers, cookies=cookies, data=data)
    return response
    pass

def extract_data(html,year,diary):
    bsData = bs(html)
    tbl = bsData.select_one("#collapse1 > div > table")
    # print (tbl.getText())
    rows = tbl.select("tr")
    print (len(rows))
    caseinfo = {}
    caseinfo["year"]=year
    caseinfo["diary"] = diary
    for row in rows:
        key = row.select("td")[0].getText()
        value = row.select("td")[1].getText()
        # print (key,value)
        caseinfo[key]=value

    casesData.append(caseinfo)
    # print (casesData)

    # pass

def save(datapoints):
    pass

def export(df,output="csv"):
    if output=="csv":
        df.to_csv()
for year in years:
    # if year > 2000: break
    for diary in diaries:
        # if diary > 3 :break
        print (year,diary)
        try:
          caseHTML = read_data(diary,year).content
          data = extract_data(caseHTML,year,diary)
        except:
          pass

pd.DataFrame(casesData).to_csv("cases.csv",index=False)

!pip install requests bs4 pandas