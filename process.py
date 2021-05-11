import os
import re
import win32api
import datetime as date
import cv2

from bson import ObjectId

PROCESS_DATE = date.datetime.now()


def create_dict(directory: str, metadata, status: str = "New"):
    return {
        "directory": directory,
        "status": status,
        "createdDate": PROCESS_DATE,
        "modifiedDate": None,
        "metadata": metadata
    }


def metadata(width, height, dtype):
    return {
        "width": width,
        "height": height,
        "size": width * height,
        "type": dtype
    }


def get_drives():
    drives = win32api.GetLogicalDriveStrings()
    drives = drives.split('\000')[:-1]
    return drives


def recursive_folder(self, folders: list):
    ignore_folder = re.compile(r"(.*.(sys|Msi|logbin)|Windows|lib|winutils|System Volume Information|\$)",
                               re.IGNORECASE)
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
                    im = cv2.imread(new)
                    h, w, _ = im.shape
                    new_dict = create_dict(re.sub(r'[^(\\|/)]+\\?$', '', new), metadata(w, h, "REgezx para saber a extensao"))

                    if new_dict not in folders:
                        folders.append(new_dict)

    except PermissionError:
        print(f"Access denied to read")


def get_folders(drive):
    print(f" Drive -> {drive}")
    folders = list()
    recursive_folder(drive, folders)
    # check async process in python, could be done separate process for each drive

    return folders
