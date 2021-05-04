import datetime as date
import json

from json import JSONEncoder


class Folder:
    def __init__(self, directory, status="New"):
        self.directory = directory
        self.status = status
        self.created_date = date.datetime.now()
        self.modified_date = None

    def __hash__(self):
        return hash(self.directory)

    def __eq__(self, other):
        return isinstance(other, Folder) and self.directory == other.directory

    def to_json(self):
        return json.dumps(self.__init__, indent=4, cls=FolderEncoder)


# subclass JSONEncoder
class FolderEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__
