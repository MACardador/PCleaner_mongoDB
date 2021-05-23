import os
import re
import win32api
import datetime as date
import cv2


def create_dict(folder: str, file: str, metadata):
    return {
        "folder": folder,
        "file": file,
        "createdDate": date.datetime.now(),
        "metadata": metadata
    }


def metadata(shape, dtype):
    height, width, channel = shape
    return {
        "width": width,
        "height": height,
        "channel": channel,
        "type": dtype
    }


def get_drives():
    drives = win32api.GetLogicalDriveStrings()
    drives = drives.split('\000')[:-1]
    return drives


def recursive_folder(self, folders: list):
    ignore_folder = re.compile(r"(.*.(sys|Msi|logbin)|Windows|lib|winutils|System Volume Information|AppData|\$)",
                               re.IGNORECASE)
    extension = re.compile(r'(s*(bmp|pbm|pgm|ppm|jpeg|jpg|jpe|jp2|tiff|tif)$)', re.IGNORECASE)
    file = re.compile(r'(.*[\\])(.*[.\\]\S*.$)', re.IGNORECASE)
    # for directory in directories:
    try:
        for entry in os.listdir(self):
            if not ignore_folder.match(entry):
                new = os.path.join(self, entry)
                if os.path.isdir(new):
                    recursive_folder(new, folders)
                elif extension.search(new):

                    im = cv2.imread(new)
                    if im is not None:

                        new_dict = create_dict(file.search(new).group(1), file.search(new).group(2),
                                               metadata(im.shape, extension.search(new).group()))
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
