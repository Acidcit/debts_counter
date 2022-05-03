import pandas as pd
import datetime
import os

print("rhjn")

# получение названий всех файлов с еженедельными дебиторками
file_names = []
with os.scandir('all_weekly_reports') as listOfEntries:
    for entry in listOfEntries:
        if entry.is_file():
            file_names.append(entry.name)
file_names.remove('.DS_Store')

print(file_names)