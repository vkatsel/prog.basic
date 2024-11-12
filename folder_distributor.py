import csv
import pickle
import os
from tkinter import filedialog

with open(filedialog.askopenfilename(), 'rb') as file:
    data = pickle.load(file)

path = filedialog.askdirectory() + '/dataset'
os.makedirs(path, exist_ok=True)
for grade in data:
    os.makedirs(path+'/'+str(grade), exist_ok=True)
    for language in data[grade]:
        with open(path+'/'+str(grade)+f'/{language}.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            header = ['Nickname', 'Age', 'Sex']
            writer.writerow(header)
            for student in data[grade][language]:
                writer.writerow(student)