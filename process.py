import os
import re
import win32api
import dto.folder as folder

folders = set()


def get_drives():
    drives = win32api.GetLogicalDriveStrings()
    drives = drives.split('\000')[:-1]
    print(drives)
    return drives


def recursive_folder(directory):
    ignore_folder = re.compile(r"(.*.(sys|Msi|logbin)|Windows|lib|winutils|System Volume Information|\$)", re.IGNORECASE)
    types = re.compile(r'(^.*\.(jpg|gif|jpeg|png)$)', re.IGNORECASE)

    # for directory in directories:
    try:
        # content = ([i for i in os.listdir(directory) if not regex.match(i)])
        directory_list = os.listdir(directory)
        for content in directory_list:
            if not ignore_folder.match(content):
                new = os.path.join(directory, content)
                if os.path.isdir(new):
                    recursive_folder(new)
                elif types.match(new):
                    folders.add(folder.Folder(re.sub(r'[^(\\|/)]+\\?$', '', new)))
    except PermissionError:
        print(f"Access denied to read")


def get_folder():
    for drive in get_drives():
        print(f'Drive -> {drive}')
        recursive_folder(drive)
    return folders
