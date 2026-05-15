# How to work with Text,CSV and JSON Files.
filename = 'example.text'

# with open(filename, 'a') as f:
#     f.write("Hello World\n")
#     f.write("Hello World\n")
#     f.write("Hello World\n")

#write file------------

# import os
# filename = 'example.text'
# if not os.path.exists(filename):
#     with open(filename, 'w') as f:
#         f.write('hello\n')
#         f.write('hello\n')
#         f.write('hello\n')
#         f.write('hello\n')
#         f.write('hello\n')
#         f.write('hello\n')
# else:
#     with open(filename, 'r') as f:
#         print('File exists.')
#         print(f.read())

# ||


# 1 Working with Text Files(.txt)----------
# Mode----------------Meaning
# 'r'-----------------Read
# 'w'-----------------Write
# 'a'-----------------Append(Add at end)
# 'r+'----------------Read & write
# filename = 'example.text'
# with open(filename, 'r') as f:
#     print(f)
'more practice'
# with open(filename, 'r') as f:
#     for line in f:
#         print(line.strip())
# with open(filename, 'r') as f:
#     first_line = f.readline()
#     second_line = f.readline()
#     print(second_line)
with open(filename, 'w') as f:
    f.write('more practice\n')
    f.write('practice 1\n')
    f.write('practice 2\n')
    f.write('practice 3\n')
    f.write('practice 4\n')
with open(filename, 'a') as f:
    f.write('practice 5\n')
    f.write('practice 6\n')

# 2️⃣ Working with CSV Files (.csv)
# CSV = Comma-Separated Values, it used for table like Exel, data analysis and etc...
import csv
# with open("data.csv", "w", newline="") as f:
#     writer = csv.writer(f)
#     writer.writerow(["name", "age", "city"])
#     writer.writerow(["Million", 18, "Addis"])
'reading and writing csv data'
# with open('data.csv', 'r') as f:
#     reader = csv.reader(f)
#     for row in reader:
#         print(row)
# data = [
#     ['Ebba', '17', 'shagger'],
#     ['Zerihun', '19', 'shagger'],
#     ['Zedo', '19', 'Tafo']
# ]
# with open('data.csv', 'a', newline = '') as f:
#     writer = csv.writer(f)
#     writer.writerows(data)
'⭐ Read CSV as dictionary (VERY useful)'
# with open('data.csv', 'r') as f:
#     reader = csv.DictReader(f)
#     for row in reader:
#         print(row['name'], row['age'])
'3️⃣ Working with JSON Files (.json)'
import json

# writing json file
# student = {
#     "name": "Million",
#     "age": 18,
#     "skills": ["Python", "HTML"]
# }
#
# with open('data.json', 'w') as f:
#     json.dump(student, f, indent=4)
#
# # Reading JSON file---------
# with open('data.json', 'r') as f:
#     data = json.load(f)
#     print(data)

with open('data.json', 'r') as f:
    data = json.load(f)
data['skills'].append('C++')
with open("data.json", "w") as f:
    json.dump(data, f, indent=4)
