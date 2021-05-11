from repository.folder_collection import FolderCollection


def add_folders(folders):
    FolderCollection.insert_all(folders)


def folder_and_metadata(folders):
    FolderCollection.insert_all(folders)

    for folder in folders:
        folder

def get_folders():
    return FolderCollection.select()
