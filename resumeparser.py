from pyresparser import ResumeParser
from pathlib import Path
import os
import pprint
import re
import json

from PyDictionary import PyDictionary
import difflib


for base, _, files in os.walk(Path("C:/Users/Asus/OneDrive/Desktop/credicxo")):
    for Files in files:
        if Files.endswith('.pdf'):
               data = ResumeParser(base+"\\" + Files).get_extracted_data()
               print(Files)
               pprint.pprint(data)
               print("-------------------------------------------------------------------------")
               

y = json.dumps(data)


print('*********************Required Data***************************','\n')

Name = data['name']
First_Name = Name.split()[0]
Last_Name = Name.split()[1]
print("First Name: ",First_Name)
print("Last Name: ",Last_Name)


email_pattern = re.compile(r'[a-zA-Z0-9-\.]+@[a-zA-z-0-9-\.]*\.[a-z]*')
email_matches = email_pattern.finditer(y)
for e in email_matches:
    print(e,'\n')


phone_pattern = re.compile(r'[0-9]{10}')
phone_matches = phone_pattern.finditer(y)
for p in phone_matches:   
    print(p,'\n')



print("Skills: ",data['skills'],data['college_name'],'\n')

print("Education: ", data['degree'],'\n')

print("Experience: ",data['experience'], data['company_names'],'\n')

txt = ' '.join(data['experience'])

languages = re.compile(r'\bHindi\b | \bEnglish\b | \bTamil\b | \bGujrati\b | \bTelugu\b | \bMalayalam\b | \bMarathi\b', flags=re.I | re.X)
print("Languages known: ",languages.findall(txt))

status = re.compile(r'\bSingle\b | \bMarried\b | \bUnmarried\b | \bDivorced\b ', flags=re.I | re.X)
print("Marital Status: ",status.findall(txt))

nationality = re.compile(r'\bIndia\b | \bIndian\b | \bINR\b | \bNon-Indian\b ', flags=re.I | re.X)
print("Nationality: ",nationality.findall(txt))

sex = re.compile(r'\bMale\b | \bFemale\b | \bLGBT\b | \bLGBTQ\b | \bTransGender | \bTrans Gender\b | \bTrans-Gender', flags=re.I | re.X)
print("Gender: ",sex.findall(txt))


bday = difflib.get_close_matches('Birthday', data['experience'])
bbday = ''.join(bday)
if bbday in data['experience']:
    dob = data['experience'].index(bbday)
    print("Date of birth: ",data['experience'][dob+1])







 




