import re
import os
import shutil


# Selective Copy
def selective_copy():
    new_folder = input('New Folder')
    try:
        os.makedirs(new_folder)
    except FileExistsError:
        print('This directory already exists.\n'
              'Your files will be placed in ' + new_folder)
    new_file_path = os.path.abspath(new_folder)
    while True:
        try:
            pull_directory = input(
                'Where do you want to extract your files from?\n')
            os.chdir(pull_directory)
            path = os.getcwd()
            break
        except FileNotFoundError:
            print('Please type in a full path to the directory')

    type_of_file = input('What type of files do you want to copy?\n')
    pdf_regex = re.compile(('.' + type_of_file + '$'), re.I)

    i = 0
    for folder_name, subfolders, filenames in os.walk(path):
        for filename in filenames:
            if pdf_regex.search(filename):
                print('FILE INSIDE ' + folder_name + ': ' + filename)
                file_path = folder_name + '\\' + filename
                shutil.copy(file_path, new_file_path)
                i += 1
    if i > 1:
        print('Files were successfully copied into %s ' % new_folder)
    else:
        print('There were no files to copy')


# Filling in the Gaps

def filling_gaps():
    path = os.getcwd()
    prefix_regex = re.compile(r'(\d{,3})')
    i = 1
    for file in os.listdir():
        search_file = prefix_regex.search(file)
        if search_file:
            old_path = os.path.abspath(file)
            new_name = search_file.group(1)+str(i).zfill(3)+'.txt'
            new_path = os.path.join(path, new_name)
            i = + 1
            shutil.move(old_path, new_path)

# Delete Unneeded  File


def del_file():
    import os
    while True:
        try:
            dir_search = input(
                'Please type in the path.\n')
            os.chdir(dir_search)
            dir_search = os.path.abspath('.')
            print('Searching ' + dir_search + '...')
            break
        except FileNotFoundError:
            print('Path not found')

    for folder_name, subfolders, filenames in os.walk('.'):
        for filename in filenames:
            filename = os.path.join(folder_name, filename)
            size = os.path.getsize(filename)
            if size > 100000000:
                print(os.path.abspath(filename) + ' - ' + str(size))

    print('Done.')


if __name__ == '__main__':
    selective_copy()
