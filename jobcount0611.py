# -*- coding: utf-8 -*-

import time
from flask import Flask
from flask import request,session, redirect, url_for, escape,send_from_directory,jsonify
import json
import requests
import  sys
import urllib
import locale
import urllib.request
import time
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import re

import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

import numpy as np


chrome_options = Options()
chrome_options.add_argument('--headless')

#-----------------------------------------------------------------------------
# Part 1: Webscraping
#-----------------------------------------------------------------------------

indeed = ('https://www.indeed.com/viewjob?cmp=Biocerna-LLC&t=Business+Data+Analyst&jk=d481e2dfb5dbeffa&q=%27+data+analyst+%27&vjs=3')
browser = webdriver.Chrome(executable_path=r'D:\\MY-DOC\\Downloads\\chromedriver_win32\\chromedriver.exe',chrome_options=chrome_options)
browser.get(indeed)
view_page = browser.page_source
job_description = view_page.split("<div id=\"jobDescriptionText\" class=\"jobsearch-jobDescriptionText\">")[1].split("</div>")[0]
job_description = str(job_description)

lines = job_description.split('\n')
y = [ x for x in lines if "<li>" in x ]
indeed_list1 = [x.replace('<li>','') for x in y]
indeed_list1 = [x.replace('</li>','') for x in indeed_list1]
indeed_list1 = [x.replace('\n','') for x in indeed_list1]

#indeed_list1=[]

indeed = ('https://www.indeed.com/viewjob?cmp=Amida-Technology-Solutions&t=Data+Analyst&jk=23e3a6908e398d4a&sjdu=QwrRXKrqZ3CNX5W-O9jEvfjoPjlrjkkqbpAP1tAwhZnPRvtT3gSme7pF_Xte9rt22pWfhbd6QrKXbI2E4Pt3cQ&tk=1ec0pdilm352k000&adid=351774716&pub=4a1b367933fd867b19b072952f68dceb&vjs=3')
browser = webdriver.Chrome(executable_path=r'D:\\MY-DOC\\Downloads\\chromedriver_win32\\chromedriver.exe',chrome_options=chrome_options)
browser.get(indeed)
view_page = browser.page_source
job_description = view_page.split("<div id=\"jobDescriptionText\" class=\"jobsearch-jobDescriptionText\">")[1].split("</div>")[0]
job_description = str(job_description)

lines = job_description.split('\n')
y = [ x for x in lines if "<li>" in x ]
indeed_list2 = [x.replace('<li>','') for x in y]
indeed_list2 = [x.replace('</li>','') for x in indeed_list2]
indeed_list2 = [x.replace('\n','') for x in indeed_list2]

indeed_list = indeed_list1 + indeed_list2


glassdoor = ('https://www.glassdoor.com/job-listing/data-analyst-i-kforce-JV_IC1138644_KO0,14_KE15,21.htm?jl=3582936385&ctt=1591634155080')
browser = webdriver.Chrome(executable_path=r'D:\\MY-DOC\\Downloads\\chromedriver_win32\\chromedriver.exe',chrome_options=chrome_options)
browser.get(glassdoor)
view_page = browser.page_source
job_description = view_page.split("<div class=\"desc css-58vpdc ecgq1xb3\">")[1].split("</div>")[0]
job_description = str(job_description)

lines = job_description.split('\n')
y = [ x for x in lines if "<li>" in x ]
glassdoor_list1 = [x.replace('<li>','') for x in y]
glassdoor_list1 = [x.replace('</li>','') for x in glassdoor_list1]
glassdoor_list1 = [x.replace('\n','') for x in glassdoor_list1]


glassdoor = ('https://www.glassdoor.com/job-listing/python-developer-quotient-JV_IC1153817_KO0,16_KE17,25.htm?jl=2925768510&ctt=1592438154848')
browser = webdriver.Chrome(executable_path=r'D:\\MY-DOC\\Downloads\\chromedriver_win32\\chromedriver.exe',chrome_options=chrome_options)
browser.get(glassdoor)
view_page = browser.page_source
job_description = view_page.split("<div class=\"desc css-58vpdc ecgq1xb3\">")[1].split("</div>")[0]
job_description = str(job_description)

lines = job_description.split('\n')
y = [ x for x in lines if "<li>" in x ]
glassdoor_list2 = [x.replace('<li>','') for x in y]
glassdoor_list2 = [x.replace('</li>','') for x in glassdoor_list2]
glassdoor_list2 = [x.replace('\n','') for x in glassdoor_list2]

glassdoor_list = glassdoor_list1+glassdoor_list2


careerbuilder = ('https://www.careerbuilder.com/job/J3M3N55XGR7RNPPN2KC?ipath=CRJR3')
browser = webdriver.Chrome(executable_path=r'D:\\MY-DOC\\Downloads\\chromedriver_win32\\chromedriver.exe',chrome_options=chrome_options)
browser.get(careerbuilder)
view_page = browser.page_source
job_description = view_page.split("<div class=\"seperate-bottom tab bloc jdp-description-details\" id=\"jdp_description\">")[1].split("<div class=\"col small col-mobile-full seperate-top-border-mobile\" id=\"col-right\" style=\"top: 119px;\">")[0]
job_description = str(job_description)

#print("desc:\n")
#print(job_description)

lines = job_description.split('\n')
y = [ x for x in lines if "<li>" in x ]
careerbuilder_list1 = [x.replace('<li>','') for x in y]
careerbuilder_list1 = [x.replace('</li>','') for x in careerbuilder_list1]

careerbuilder_list1 = str(careerbuilder_list1)

careerbuilder_list1 = careerbuilder_list1.split('\\t')

careerbuilder_list1 = [x.replace('<strong>','') for x in careerbuilder_list1]
careerbuilder_list1 = [x.replace('</strong>','') for x in careerbuilder_list1]
careerbuilder_list1 = [x.replace('<br>','') for x in careerbuilder_list1]
careerbuilder_list1 = [x.replace('</br>','') for x in careerbuilder_list1]
careerbuilder_list1 = [x.replace('</ul>','') for x in careerbuilder_list1]
careerbuilder_list1 = [x.replace('<ul>','') for x in careerbuilder_list1]
#careerbuilder_list1 = [x.replace('\\t','') for x in careerbuilder_list1]
careerbuilder_list1 = [x.replace('\n','') for x in careerbuilder_list1]


careerbuilder = ('https://www.careerbuilder.com/job/J3P04K6BWVRCL38RPN4?ipath=CRJR7')
browser = webdriver.Chrome(executable_path=r'D:\\MY-DOC\\Downloads\\chromedriver_win32\\chromedriver.exe',chrome_options=chrome_options)
browser.get(careerbuilder)
view_page = browser.page_source
job_description = view_page.split("<div class=\"seperate-bottom tab bloc jdp-description-details\" id=\"jdp_description\">")[1].split("</div>")[0]
job_description = str(job_description)


lines = job_description.split('\n')
y = [ x for x in lines if "<li>" in x ]
careerbuilder_list2 = [x.replace('<li>','') for x in y]
careerbuilder_list2 = [x.replace('</li>','') for x in careerbuilder_list2]
careerbuilder_list2 = [x.replace('\n','') for x in careerbuilder_list2]

#print("CB2:\n")
#print(careerbuilder_list2)

careerbuilder_list = careerbuilder_list1+careerbuilder_list2
#print("CB:\n")
#print(careerbuilder_list)


dice = ('https://www.dice.com/jobs/detail/data-scientist-newton-ma-02456/jobtblok/120660356?searchlink=search%2F%3Fq%3Dpython%26countryCode%3DUS%26radius%3D30%26radiusUnit%3Dmi%26page%3D1%26pageSize%3D20%26language%3Den&searchId=ef21db47-12e5-41a8-9fcd-0a4de08337c8')
browser = webdriver.Chrome(executable_path=r'D:\\MY-DOC\\Downloads\\chromedriver_win32\\chromedriver.exe',chrome_options=chrome_options)
browser.get(dice)
view_page = browser.page_source
job_description = view_page.split("<div class=\"highlight-black\" id=\"jobdescSec\">")[1].split("</div>")[0]
job_description = str(job_description)

lines = job_description.split('<li>')
y = [ x for x in lines if "</li><br>" in x ]
y = [ x for x in lines if "<p>" not in x ]
dice_list1 = [x.replace('</li><br>','') for x in y]
dice_list1 = [x.replace('<br>','') for x in dice_list1]
dice_list1 = [x.replace('</br>','') for x in dice_list1]
dice_list1 = [x.replace('</strong>','') for x in dice_list1]
dice_list1 = [x.replace('<strong>','') for x in dice_list1]
dice_list1 = [x.replace('</ul>','') for x in dice_list1]
dice_list1 = [x.replace('<ul>','') for x in dice_list1]
dice_list1 = [x.replace('<li>','') for x in dice_list1]
dice_list1 = [x.replace('</li>','') for x in dice_list1]




#print("Dice:\n")
#print(dice_list1)
'''
dice = ('https://www.dice.com/jobs/detail/python%2C-sql-data-engineer-yoh-%26%2345-a-day-%26-zimmerman-company-dallas-tx-75201/10107614/295724?searchlink=search%2F%3Fq%3Dpython%2520data%26countryCode%3DUS%26radius%3D30%26radiusUnit%3Dmi%26page%3D1%26pageSize%3D20%26language%3Den&searchId=4dd4f821-0c18-4a5a-ae0e-21cc72a3b5d2')
browser = webdriver.Chrome(executable_path=r'D:\\MY-DOC\\Downloads\\chromedriver_win32\\chromedriver.exe',chrome_options=chrome_options)
browser.get(dice)
view_page = browser.page_source
job_description = view_page.split("<div class=\"highlight-black\" id=\"jobdescSec\">")[1].split("#diceSP")[0]
job_description = str(job_description)

lines = job_description.split('<li>')
y = [ x for x in lines if "</li><br>" in x ]
y = [ x for x in lines if "<p>" not in x ]
dice_list2 = [x.replace('</li><br>','') for x in y]
dice_list2 = [x.replace('</b><br><br>','') for x in dice_list2]
dice_list2 = [x.replace('<br><br><b>','') for x in dice_list2]
dice_list2 = [x.replace('</li>','') for x in dice_list2]
dice_list2 = [x.replace('</ul>','') for x in dice_list2]
dice_list2 = [x.replace('<ul>','') for x in dice_list2]
dice_list2 = [x.replace('<b>','') for x in dice_list2]
dice_list2 = [x.replace('</b>','') for x in dice_list2]
dice_list2 = [x.replace('<br>','') for x in dice_list2]
'''
dice_list2=[]
dice_list=dice_list1+dice_list2


job_req_list = indeed_list+dice_list+glassdoor_list+careerbuilder_list

#-----------------------------------------------------------------------------
# Part 2: Data Cleaning
#     Exclude stop words and symbols
#-----------------------------------------------------------------------------

#introduce commas
job_req_list = [x.replace(' ',', ') for x in job_req_list]
job_req_list = [x.replace(',,',',') for x in job_req_list]
job_req_list = [x.replace('.','') for x in job_req_list]

job_req_list = map(str.lower,job_req_list)

exclude_words = [',','and,','in,','to,','as,','for,','from,','of,','on,','or,','that,','the,','to, ','with,','be,','their,','will,','a,','</ul>,','<ul>,','-,','work,','team,','this,','ability,','across,','by,','well,','business,','closely,','teams,','understanding,','is,','an,','list,','through,','tools,','using,','skills,','excellent,','all,','advanced,','apply,','written,','verbal,','role,','are,','building,','opportunities,','demonstrated,','must,','perform,','solid,','strong,','such,','up,','working,','follow,','follows,','define,','diverse,','do,','effective,','has,','have,','high,','include,','inspired,','large,','level,','make,','more,','others,','questions,','related,','you,','create,','required,','skills,','knowledge,','can,','enable,','environment,','expert,','implement,','improvements,','into,','job,','may,','participate,','position,','practices,','principles,','process,','processes,','proficiency,','proficient,','progress,','project,','skills,','understand,','various,','time,','also,','our,','new,']

job_req_list = set(job_req_list)
exclude_words = set(exclude_words)
job_req_list = job_req_list - exclude_words
job_req_list = list(job_req_list)

for i in range(0, len(job_req_list)):
    if(job_req_list[i].startswith(' ,')):
        job_req_list[i].replace(', ','')

temp_list = []
for elem in job_req_list:
    elem_list = elem.split()
    resultwords  = [word for word in elem_list if word not in exclude_words]
    result = ' '.join(resultwords)
    temp_list.append(result)
job_req_list = []
job_req_list = temp_list
temp_list = []

temp = []
for elem in job_req_list:
    temp2 = elem.split(', ') 
    temp.append((temp2))

Output = []
for elem in temp:
    temp3 = []
    for elem2 in elem:
        temp3.append(elem2)
    Output.append(temp3)
job_req_list = []
job_req_list = Output

replace_words = ['analytics','analyzes','analyse','analysis','analytical','analytic']
for item in job_req_list:
    tmp_list = []
    for word in item:
        if word in replace_words:
            item.remove(word)
            item.append("analyze")


te = TransactionEncoder()
te_ary = te.fit(job_req_list).transform(job_req_list)

pd.set_option('display.max_rows', None)

df = pd.DataFrame(te_ary, columns=te.columns_)

#-------------------------------------------------------------------------------------------------
# Part 3: Set support and lift
#-------------------------------------------------------------------------------------------------

#Set minimum threshold (SUPPORT)
frequent_itemsets = apriori(df, min_support=0.05, use_colnames=True)
frequent_itemsets = frequent_itemsets.sort_values('support', ascending=False)
frequent_itemsets.reset_index(drop=True, inplace=True)
#frequent_itemsets = frequent_itemsets.head(50)

#Set minimum threshold (LIFT)
rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1.25)
rules = rules.sort_values('lift', ascending=False)
rules.reset_index(drop=True, inplace=True)

#Set minimum threshold (CONFIDENCE)
conf = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.1)
conf = conf.sort_values('confidence', ascending=False)
conf.reset_index(drop=True, inplace=True)

#-------------------------------------------------------------------------------------------------
#Set minimum threshold (SUPPORT)
frequent_itemsets_2 = apriori(df, min_support=0.04, use_colnames=True)
frequent_itemsets_2 = frequent_itemsets_2.sort_values('support', ascending=False)
frequent_itemsets_2.reset_index(drop=True, inplace=True)
#frequent_itemsets = frequent_itemsets.head(50)

#Set minimum threshold (LIFT)
rules_2 = association_rules(frequent_itemsets_2, metric="lift", min_threshold=1.25)
rules_2 = rules_2.sort_values('lift', ascending=False)
rules_2.reset_index(drop=True, inplace=True)

#Set minimum threshold (CONFIDENCE)
conf_2 = association_rules(frequent_itemsets_2, metric="confidence", min_threshold=0.1)
conf_2 = conf_2.sort_values('confidence', ascending=False)
conf_2.reset_index(drop=True, inplace=True)
#-------------------------------------------------------------------------------------------------
# Part 4: Tag each word/phrase as skill,requirement, or other
#-------------------------------------------------------------------------------------------------

#convert objects to strings
rules["antecedents"] = rules["antecedents"].apply(lambda x: list(x)[0]).astype("string")
rules["consequents"] = rules["consequents"].apply(lambda x: list(x)[0]).astype("string")

#Most common skills and requirements
skills_list = ['analyze','sql','python','visualization','etl','html','css','learning']
req_list = ['bachelor\'s','degree','engineering','years','experience']

#ant will temporarily store each element in the antecedents column
#cons will do the same for consequents
ant = ''
cons = ''

#tag will become the new column 'Tag', which will indicate skill,requirement, or other
tag = []

#Loop through dataframe
for index, row in rules.iterrows():
    ant = row['antecedents']
    cons = row['consequents']
    
    #Do the words appear in the list of skills? Then mark as skill
    if (ant in skills_list or cons in skills_list):
        if (ant != 'experience' and cons != 'experience'):
            tag.append('skill')
        else:
            tag.append('requirement')
    elif (ant in req_list or cons in req_list):
        tag.append('requirement')
    else:
        tag.append('other')
#print(tag)

#Insert the list as a new column in the dataframe
rules.insert(2, "Tag", tag, True)

#------------------------------------------------------------------------------------------
#convert objects to strings
rules_2["antecedents"] = rules_2["antecedents"].apply(lambda x: list(x)[0]).astype("string")
rules_2["consequents"] = rules_2["consequents"].apply(lambda x: list(x)[0]).astype("string")

#Most common skills and requirements
skills_list = ['analyze','sql','python','visualization','etl','html','css','learning']
req_list = ['bachelor\'s','degree','engineering','years','experience']

#ant will temporarily store each element in the antecedents column
#cons will do the same for consequents
ant = ''
cons = ''

#tag will become the new column 'Tag', which will indicate skill,requirement, or other
tag = []

#Loop through dataframe
for index, row in rules_2.iterrows():
    ant = row['antecedents']
    cons = row['consequents']
    
    #Do the words appear in the list of skills? Then mark as skill
    if (ant in skills_list or cons in skills_list):
        if (ant != 'experience' and cons != 'experience'):
            tag.append('skill')
        else:
            tag.append('requirement')
    elif (ant in req_list or cons in req_list):
        tag.append('requirement')
    else:
        tag.append('other')
#print(tag)

#Insert the list as a new column in the dataframe
rules_2.insert(2, "Tag", tag, True)
#------------------------------------------------------------------------------------------
#convert objects to strings
frequent_itemsets["itemsets"] = frequent_itemsets["itemsets"].apply(lambda x: list(x)[0]).astype("string")

#Most common skills and requirements
skills_list = ['analyze','sql','python','visualization','etl']
req_list = ['bachelor\'s','degree','engineering','years','experience']

#ant will temporarily store each element in the antecedents column
#cons will do the same for consequents
item = ''

#tag will become the new column 'Tag', which will indicate skill,requirement, or other
tag = []

#Loop through dataframe
for index, row in frequent_itemsets.iterrows():
    item = row['itemsets']
    
    #Do the words appear in the list of skills? Then mark as skill
    if any(x in item for x in skills_list):
        tag.append('skill')
    elif any(x in item for x in req_list):
        tag.append('requirement')
    else:
        tag.append('other')
#print(tag)

#Insert the list as a new column in the dataframe
frequent_itemsets.insert(2, "Tag", tag, True)

#------------------------------------------------------------------------------------------
#convert objects to strings
frequent_itemsets_2["itemsets"] = frequent_itemsets_2["itemsets"].apply(lambda x: list(x)[0]).astype("string")

#Most common skills and requirements
skills_list = ['analyze','sql','python','visualization','etl']
req_list = ['bachelor\'s','degree','engineering','years','experience']

#ant will temporarily store each element in the antecedents column
#cons will do the same for consequents
item = ''

#tag will become the new column 'Tag', which will indicate skill,requirement, or other
tag = []

#Loop through dataframe
for index, row in frequent_itemsets_2.iterrows():
    item = row['itemsets']
    
    #Do the words appear in the list of skills? Then mark as skill
    if any(x in item for x in skills_list):
        tag.append('skill')
    elif any(x in item for x in req_list):
        tag.append('requirement')
    else:
        tag.append('other')
#print(tag)

#Insert the list as a new column in the dataframe
frequent_itemsets_2.insert(2, "Tag", tag, True)

#------------------------------------------------------------------------------------------
# Part 5: Removing duplicate pairs
#------------------------------------------------------------------------------------------

for index, row in frequent_itemsets.iterrows():
    a = row['itemsets']

    indexNames = frequent_itemsets[ (frequent_itemsets['itemsets'] == a)].index
    indexNames = indexNames.tolist()
    del indexNames[0]
    frequent_itemsets.drop(indexNames , inplace=True)
frequent_itemsets.reset_index(drop=True, inplace=True)

for index, row in frequent_itemsets_2.iterrows():
    a = row['itemsets']

    indexNames = frequent_itemsets_2[ (frequent_itemsets_2['itemsets'] == a)].index
    indexNames = indexNames.tolist()
    del indexNames[0]
    frequent_itemsets_2.drop(indexNames , inplace=True)
frequent_itemsets_2.reset_index(drop=True, inplace=True)

for index, row in rules.iterrows():
    a = row['antecedents']
    c = row['consequents']

    indexNames = rules[ (rules['antecedents'] == a) & (rules['consequents'] == c)].index
    indexNames = indexNames.tolist()
    del indexNames[0]
    rules.drop(indexNames , inplace=True)
rules.reset_index(drop=True, inplace=True)

for index, row in rules_2.iterrows():
    a = row['antecedents']
    c = row['consequents']

    indexNames = rules_2[ (rules_2['antecedents'] == a) & (rules_2['consequents'] == c)].index
    indexNames = indexNames.tolist()
    del indexNames[0]
    rules_2.drop(indexNames , inplace=True)
rules_2.reset_index(drop=True, inplace=True)

#------------------------------------------------------------------------------------------
# Part 6: Write to files:
#------------------------------------------------------------------------------------------

#print (frequent_itemsets.dtypes)
#print(rules)
file2write=open("C:\\python\\frequent_itemsets.txt",'w')
file2write.write(str(frequent_itemsets))
file2write.close()

file2write=open("C:\\python\\rules.txt",'w')
file2write.write(str(rules))
file2write.close()

file2write=open("C:\\python\\conf.txt",'w')
file2write.write(str(conf))
file2write.close()

file2write=open("C:\\python\\frequent_itemsets_2.txt",'w')
file2write.write(str(frequent_itemsets_2))
file2write.close()

file2write=open("C:\\python\\rules_2.txt",'w')
file2write.write(str(rules_2))
file2write.close()

file2write=open("C:\\python\\conf_2.txt",'w')
file2write.write(str(conf_2))
file2write.close()
#print("RULES:\n")
#print (rules.dtypes)
#------------------------------------------------------------------------------------------

#print(indeed_list1)