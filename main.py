from process import get_folder
from service import add_folders
import json
import pickle

from json import JSONEncoder


folders = get_folder()
[print(u) for u in folders]

# add folder to database
print(pickle.dumps(folders))
add_folders(folders)
