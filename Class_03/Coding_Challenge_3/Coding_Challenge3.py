# Task 1. Simple directory tree
#
# Replicate this tree of directories and subdirectories:
#
# ├── draft_code
# |   ├── pending
# |   └── complete
# ├── includes
# ├── layouts
# |   ├── default
# |   └── post
# |       └── posted
# └── site
#
#     Using os.system or os.mkdirs replicate this simple directory tree.
#     Delete the directory tree without deleting your entire hard drive.

import os
os.mkdir('Task1') #I create this additional folder, so it will be easier to delete it later with 'import shutil'

os.mkdir('Task1/Draft_code')
os.mkdir('Task1/Draft_code/Pending')
os.mkdir('Task1/Draft_code/Complete')

os.mkdir('Task1/Includes')

os.mkdir('Task1/Layouts')
os.mkdir('Task1/Layouts/Default')
os.mkdir('Task1/Layouts/Post')
os.mkdir('Task1/Layouts/Post/Posted')

os.mkdir('Task1/Site')

import shutil
shutil.rmtree('Task1')

# Task 2
# 2. Push sys.argv to the limit
#
# Construct a rudimentary Python script that takes a series of inputs as a command from a bat file using sys.argv, and does something to them. The rules:
#
#     Minimum of three arguments to be used.
#     You must do something simple in 15 lines or less within the Python file.
#     Print or file generated output should be produced.

import sys
input_name = str(input("Hi, I am YX Corp, what is your name? "))

print(f'Oh hello {input_name} nice to meet you')
print(f'tell me {input_name} what is your gender?')

while True:
    input_gender = input("Please enter your gender (Male/Female): ")
    if input_gender.lower() == 'male':
        print(f'well hello sir')
        break
    elif input_gender.lower() == 'female':
        print(f'well hello miss')
        break
    else:
        print(f'Invalid response, try again')

input_age = int(input(f"How old are you {input_name}? "))
if input_age > 30:
    print(f'because you are {input_age} years old, you might be wiser than I thought')
else:
    print(f'{input_age} ?, really ? quite young, better go travel before 30')

result = ("Basic information of our user" +'\n'+
          "Name: " + str(input_name) +'\n'
          +"Age: "+ str(input_age) +'\n'
          +"Gender: "+ str(input_gender))

with open("Client_Information.txt", "w") as f:
    f.write(str(result))
print(result)

# 3. Working with CSV
#
# Using the Atmospheric Carbon Dioxide Dry Air Mole Fractions from quasi-continuous daily measurements at Mauna Loa, Hawaii dataset, obtained from here (https://github.com/datasets/co2-ppm-daily/tree/master/data).
#
# Using Python (csv) calculate the following:
#
#     Annual average for each year in the dataset.
#     Minimum, maximum and average for the entire dataset.
#     Seasonal average if Spring (March, April, May), Summer (June, July, August), Autumn (September, October, November) and Winter (December, January, February).
#     Calculate the anomaly for each value in the dataset relative to the mean for the entire time series.
#
import csv
import math
# #
years = []
CO2 = []

with open("CO2.txt") as co2_value:
    csv_reader = csv.reader(co2_value, delimiter=',')
    line_count= 0

    for row in csv_reader:
        if line_count == 0
            print ({', '. join(row)})
            line_count += 1
        else:
            print

print(len(years))
print(len(CO2))

import csv

rows = []
with open("CO2.txt", "r") as f:
        reader = csv.reader(f)
        next(reader) # skip the header row
        for row in reader:
            rows.append(row)

            file = open("CO2.txt", "r")
            file_contents = file.readlines()
            counter = 1
            for i in file_contents:
                print(str(counter) + ": " + i.rstrip())  # .rstrip() removes new line characters i.e. \n
                counter = counter + 1
            file.close()
