# Loading the needed packages:
import pandas as pd
import numpy as np
import os
import zipfile as zf
from tkinter import Tk
from tkinter.filedialog import askopenfilename

# Creating the folder directory for files-extraction:
path = os.getcwd() + '\\files'
try:
    os.mkdir(path)
except FileExistsError:
    print('Folder is already created')

# Selecting the ZIP folder and extract the files:
Tk().withdraw()
try:
    file_name = askopenfilename()
    with zf.ZipFile(file_name, 'r') as files:
        files.extractall(path)
except FileNotFoundError:
    print('File is not selected, try to run again')

# Changing the directory and list the files:
os.chdir(path)
files_name = os.listdir(path)

# Loading the CSV files to dataframes:
files = {}
for i in files_name:
    if i.split('.')[-1] == 'csv':
        x = i.split('.csv')[0]
        files[x] = i
        for k,v in files.items():
            globals()[k] = pd.DataFrame(pd.read_csv(v))
