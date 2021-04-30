from repository.folder_collection import collection


def add_folders(folders):
    # jsonFolder = [{ "folder": folder, "status": new, "modifyDate": date.datetime.now() }]
    collection.folder.insert_all(folders)

