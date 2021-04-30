from repository.folder_collection import FolderCollection


def add_folders(folders):
    # jsonFolder = [{ "folder": folder, "status": new, "modifyDate": date.datetime.now() }]
    FolderCollection.insert_all(folders)

