# filename = 'newone.txt'
# with open(filename, 'w') as f:
#     f.write('John\n')
#     f.write('Kamal\n')
#     f.write('Ephrem\n')
#
# names = ['Ismael', 'Raphael', 'henry']
# with open(filename, 'a') as f:
#     for name in names:
#         f.write(name + '\n')
'CSV file'
# import csv
#
#
# rows = [
#     ['Million', '10A', '92', '3'],
#     ['Ebba', '10A', '94', '1'],
#     ['Ephrem', '10B', '89', '4'],
#     ['Monera', '10A', '93', '2']
# ]
#
# filename = 's_data.csv'
# with open(filename, 'w', newline='') as f:
#     writer = csv.writer(f)
#     writer.writerow(['Name', 'Grade', 'Score', 'Rank'])
#     for row in rows:
#         writer.writerow(row)
# with open(filename, 'r') as f:
#     reader = csv.reader(f)
#     for row in reader:
#         print(row)
# with open(filename, 'r') as f:
#     reader = csv.DictReader(f)
#     for row in reader:
#         print(row['Name'], row['Rank'])
'JSON File'

import json
#
# student_info = {
#     'name':'Emanuel',
#     'age':21,
#     'fans': ['Messi', 'Ronaldo', 'Mr.Beast'],
#     'skills': ['Engineer', 'HTML']
# }
#
# filename = 'student_i.json'
# with open(filename, 'w') as file:
#     json.dump(student_info, file, indent=4)
#
#
# student_info['skills'].append('CSS')
# student_info['name'] = 'Million'
# with open(filename, 'w') as file:
#     json.dump(student_info, file, indent=4)
with open('student_i.json', 'r') as f:
    # contents = f.read()
    contents = json.load(f)
    print(contents)