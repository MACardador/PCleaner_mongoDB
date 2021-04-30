from process import get_folder
from service import add_folders

folders = get_folder()
[print(u) for u in folders]

# add folder to database
add_folders(folders)
