from repository.client import db

collection = db["log"]


class FolderCollection:
    def insert(self):
        ins = collection.insert_one(self)
        return ins

    def insert_all(self):
        ins_all = collection.insert_many(self)
        return ins_all

    def update(self, values=None):
        collection.update_one(self, values)

    def delete(self):
        collection.delete_one(self)

    @staticmethod
    def drop():
        collection.drop()
