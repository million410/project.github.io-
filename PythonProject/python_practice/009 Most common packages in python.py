#python package are a way to organize and structure code by grouping related modules into directories.
#package is essentially a folder that contains an_init_
import os

path = "data/new_folder"

# Check if the folder exists
if os.path.isdir(path):
    print("Path exists.")
else:
    print("Path does not exist.")
    os.makedirs(path, exist_ok=True)
    print("Path created.")

#join paths -------------.
path = "data/new_folder"
new_path = os.path.join(path,"data", "abc")
print(new_path)
print(os.path.isdir(path))

path = "data/new_folder"
list_folder = ['Folder1', 'Folder2', 'Folder3']
for folder in list_folder:
    new_path = os.path.join(path,folder)

    if not os.path.exists(new_path):
        os.makedirs(new_path)
        print('Folder created: {}'.format(new_path))

# Rename files

path = "data/new_folder"

# for folder in os.listdir(path):
#     print(folder)
#     new_folder = folder.replace('Folder1', 'Folder100')
#     os.rename(os.path.join(path, folder), os.path.join(path, new_folder))
#     print('Renamed {} to {}'.format(folder, new_folder))
#

