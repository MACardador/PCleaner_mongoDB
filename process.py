import os
import re
import win32api
import dto.folder as folder
import pickle
import jsonpickle


def get_drives():
    drives = win32api.GetLogicalDriveStrings()
    drives = drives.split('\000')[:-1]
    print(drives)
    return drives


def recursive_folder(self, folders):
    ignore_folder = re.compile(r"(.*.(sys|Msi|logbin)|Windows|lib|winutils|System Volume Information|\$)", re.IGNORECASE)
    types = re.compile(r'(^.*\.(jpg|gif|jpeg|png)$)', re.IGNORECASE)

    # for directory in directories:
    try:
        # content = ([i for i in os.listdir(directory) if not regex.match(i)])
        directory_list = os.listdir(self)
        for entry in directory_list:
            if not ignore_folder.match(entry):
                new = os.path.join(self, entry)
                if os.path.isdir(new):
                    recursive_folder(new, folders)
                elif types.match(new):
                    folders.add(folder.Folder(re.sub(r'[^(\\|/)]+\\?$', '', new)))
    except PermissionError:
        print(f"Access denied to read")


def get_folders():
    folders = set()
    for drive in get_drives():
        print(f'Drive -> {drive}')
        recursive_folder(drive, folders)

    return jsonpickle.encode(folders)
