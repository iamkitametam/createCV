import requests
from bs4 import BeautifulSoup
from create_document import *
from utils import *
from tkinter import *
from tkinter.filedialog import askopenfilename
import datetime
from shutil import copyfile
import os
# make correct date function

def make_correct_date_format(s):
    s = s.replace("\xa0"," ")
    s = s.upper()
    s = s.split(" ")
    s = s[0:5]

    if(s[3].__contains__("CURRENTLY")):
        s = s[0:4]
        s[3] = "н.в."
        s = " ".join(s)
    else:
        if(s[4][0]=='2'):
            s[4] = s[4][0:4]
            s = " ".join(s)
        else:
            s = " ".join(s)
            s = s.replace("ПО НАСТОЯЩЕЕ", "н.в.")

    s = s.replace("ЯНВАРЬ ", "01.")
    s = s.replace("ФЕВРАЛЬ ", "02.")
    s = s.replace("МАРТ ", "03.")
    s = s.replace("АПРЕЛЬ ", "04.")
    s = s.replace("МАЙ ", "05.")
    s = s.replace("ИЮНЬ ", "06.")
    s = s.replace("ИЮЛЬ ", "07.")
    s = s.replace("АВГУСТ ", "08.")
    s = s.replace("СЕНТЯБРЬ ", "09.")
    s = s.replace("ОКТЯБРЬ ", "10.")
    s = s.replace("НОЯБРЬ ", "11.")
    s = s.replace("ДЕКАБРЬ ", "12.")

    s = s.replace("JANUARY ", "01.")
    s = s.replace("FEBRUARY ", "02.")
    s = s.replace("MARCH ", "03.")
    s = s.replace("APRIL ", "04.")
    s = s.replace("MAY ", "05.")
    s = s.replace("JUNE ", "06.")
    s = s.replace("JULY ", "07.")
    s = s.replace("AUGUST ", "08.")
    s = s.replace("SEPTEMBER ", "09.")
    s = s.replace("OCTOBER ", "10.")
    s = s.replace("NOVEMBER ", "11.")
    s = s.replace("DECEMBER ", "12.")

    # s = s.replace("20","")

    return s

# ask for html file ###############################################################################

root = Tk()
root.withdraw()
hh_link = askopenfilename()
root.destroy()

# hh_link = "h://Работа/headhunting/createCV/hh_CV_template.html"
# hh_link = "h:\Работа\headhunting\headhunter_software\createCV\htmls\Меклер Евгения Александровна — Product manager (marketing specialist).html"
# hh_link = "h:\Работа\headhunting\createCV\htmls\Янин Роман Александрович — Senior_Group Product _ Marketing Manager (опыт в маркетинге 14 лет).html"
# hh_link = "h:\Работа\headhunting\headhunter_software\createCV\htmls\Дубровская Екатерина Сергеевна — Маркетолог.html"
# hh_link = "h:\Работа\headhunting\headhunter_software\createCV\htmls\Tsentsova Alisa Andreevna — Marketing manager.html"
# print("HELLO!")
# hh_link = ""
# hh_link = input()
# print("Link : ", hh_link)

# copy html to store it ###########################################################################

copyfile(hh_link, "htmls/" + os.path.basename(hh_link))

# begin parsing ###################################################################################

r = open(hh_link,encoding="utf8")
s = BeautifulSoup(r,"html.parser")

try:
    salary = s.findAll("span", {"class": "resume-block__salary resume-block__title-text_salary"})
    salary = salary[0].text.replace("\u2009","").replace("\xa0"," ")
except:
    salary = ""

# jobs ############################################################################################

jobs_return = []
jobs = s.findAll("div",{"itemprop" : "worksFor"})

# for each job
for i in range(0,len(jobs)):
    job = dict.fromkeys(['date', 'name', 'position', 'description', "location", "url"])

    job["date"] = jobs[i].find("div",{"class" : "bloko-column bloko-column_xs-4 bloko-column_s-2 bloko-column_m-2 bloko-column_l-2"}).text
    job["date"] = make_correct_date_format(job["date"])
    job["name"] = jobs[i].findAll("div",{"itemprop" : "name"})[0].text
    job["position"] = jobs[i].findAll("div",{"data-qa" : "resume-block-experience-position"})[0].text
    try:
        job["location"] = jobs[i].findAll("span",{"itemprop" : "addressLocality"})[0].text
    except:
        job["location"] = ""
    try:
        job["url"] = jobs[i].findAll("a",{"itemprop":"url"})[0].text
    except:
        job["url"] = ""

    job["description"] = jobs[i].findAll("div",{"data-qa" : "resume-block-experience-description"})[0].text
    jobs_return.append(job)

# education #######################################################################################

educations_return = []
educations = s.findAll("div",{"data-qa":"resume-block-education"})
# educations = educations[0].findAll("div",{"class" : "resume-block-item-gap"})
educations = educations[0].findAll("div",{"class" : "bloko-columns-row"})
educations = educations[2:]
for i in range(0,len(educations)):
    # educations_return = []
    # educations = s.findAll("div", {"data-qa": "resume-block-education"})
    # # educations = educations[0].findAll("div",{"class" : "resume-block-item-gap"})
    # educations = educations[0].findAll("div", {"class": "bloko-columns-row"})
    # educations = educations[2:]
    education = dict.fromkeys(['date', 'name', 'facultee', "description"])
    education["date"] = educations[i].findAll("div",{"class" : "bloko-column bloko-column_xs-4 bloko-column_s-2 bloko-column_m-2 bloko-column_l-2"})[0].text
    education["name"] = educations[i].findAll("div",{"itemprop" : "name"})[0].text
    education["facultee"] = ""
    education["description"] = educations[i].findAll("div",{"data-qa" : "resume-block-education-organization"})[0].text
    educations_return.append(education)

# additional education ############################################################################

additional_educations_return = []
try:
    additional_educations = s.findAll("div",{"data-qa":"resume-block-additional-education"})
    additional_educations = additional_educations[0].findAll("div", {"class": "resume-block-item-gap"})
    for i in range(0,len(additional_educations)):
        additional_education = dict.fromkeys(['date', 'name', 'position', "description"])
        additional_education["date"] = additional_educations[i].findAll("div",{"class" : "bloko-column bloko-column_xs-4 bloko-column_s-2 bloko-column_m-2 bloko-column_l-2"})[0].text
        additional_education["name"] = additional_educations[i].findAll("div",{"itemprop" : "name"})[0].text
        additional_education["position"] = ""
        additional_education["description"] = additional_educations[i].findAll("div",{"data-qa" : "resume-block-education-organization"})[0].text
        additional_educations_return.append(additional_education)
except:
    print("no additional educations")

# languages #######################################################################################

l = s.findAll("p",{"data-qa":"resume-block-language-item"})
languages = []
for ll in l:
    language = dict.fromkeys((["language", "level"]))
    language["language"] = ll.text.split(" — ")[0]
    language["level"] = ll.text.split(" — ")[1]
    languages.append(language)


# surname, firstname, lastname ####################################################################

try:
    FIO = s.find("h2",{"itemprop":"name"}).text
except:
    FIO = ""

# photo ###########################################################################################

try:
    photo_url = s.find("img",{"class":"resume-photo__image"}).get("src")
    r = requests.get(photo_url)  # create HTTP response object
    with open("imgs/" + FIO.upper() + ".jpg", 'wb') as f:
        f.write(r.content)
    f.close()
except:
    print("no photo")

# birth date ######################################################################################

try:
    birth_date = s.find("meta",{"itemprop":"birthDate"}).get("content")
    birth_date = birth_date.split("-")
    birth_date = birth_date[::-1]
    birth_date = ".".join(birth_date)
except:
    birth_date = ""

try:
    location = s.find("span",{"itemprop":"addressLocality"}).text
except:
    location = ""

# create_CV_using_my_word_template ################################################################

x = datetime.datetime(2020,5,1,0,0,0,0) # till 01.05.2020
y = datetime.datetime.now()
if(x>y):
    create_CV_using_my_word_template(FIO, birth_date, location, languages, salary, jobs_return, educations_return, additional_educations_return)
else:
    print("TRIAL PERIOD EXPIRED!")
