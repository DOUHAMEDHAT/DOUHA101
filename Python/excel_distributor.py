#!/usr/bin/env python
# coding: utf-8

# In[1]:

# Importing the needed modules:
import os
import shutil
import pandas as pd
import gspread
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from google.oauth2.service_account import Credentials
Tk().withdraw();

# In[2]:

#Access google-account and download the file-data:
path = 'c:credentials_json.json'
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

credentials = Credentials.from_service_account_file(path, scopes=scope)
gcc = gspread.authorize(credentials)
sh = gcc.open_by_key('"spreadsheet_id"')

with pd.ExcelWriter('datasources.xlsx', engine='xlsxwriter') as writer:
    for i, worksheet in enumerate(sh.worksheets()):
        da = sh.get_worksheet(i)
        df = pd.DataFrame(da.get_all_values(), columns=da.get_all_values()[0]).drop([0])
        df.to_excel(writer, index = False, engine = 'xlsxwriter', sheet_name = da.title)

file_path = os.getcwd() + '\\datasources.xlsx'

# Uploading the datasources.xlsx file to python:
main_file = pd.ExcelFile(file_path)

#filter the needed sources/tabs from file:
sheet_names = [f for f in main_file.sheet_names if f != '']

# Importing the list of filter ids then clean it:
partners = input("Please enter the filters-id seperated by comma").replace(" ", "");
if filters[-1] == ',':
    filters = filters[:-1]
    filters = list(set(filters.replace(" ", "").split(',')))
else:
    filters = list(set(filters.replace(" ", "").split(',')))
print("The TOP filters are: ", filters);


# In[3]:

# Manipulating the directory for creating and closing:
try:
    os.chdir('C:Desktop')
    try:
        os.mkdir(os.getcwd()+"\\files")
        os.chdir(path = os.getcwd()+"\\files")
    except:
        print("Desktop directory is created but files folder not mapped, kindly check")
except:
    print("Desktop directory not mapped, kindly check");


# In[4]:

# Main code: Creating file for each filter with their specific data in folder named as files:
files = []
for filter in filters:
    file_name = "Monthly_Performance_Report("+ str(filter) + ").xlsx"
    file = pd.ExcelWriter(file_name, engine='xlsxwriter')
    files.append(file_name)
    for sheet_name in sheet_names:
        sheet = pd.read_excel(main_file, sheet_name)
        sheet = sheet[sheet['id_filter'] == int(filter)]
        sheet.to_excel(file, index = False,engine = 'xlsxwriter', sheet_name = sheet_name)
    file.save()
    file.close()

# Closing the folder directory.
os.chdir('C:Desktop')
shutil.make_archive('all_filtersd_files', 'zip', 'files');
