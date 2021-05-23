from repository.client import db

collection = db["duplicate"]


class DuplicateCollection:
    def create_duplicate_dict(self: str, file2: str, action: str = "need_check"):
        return {
            "file1": self,
            "file2": file2,
            "action": action
        }

    def insert(self):
        ins = collection.insert_one(self)
        return ins

    def update(self, values=None):
        collection.update_one(self, values)

    def delete(self):
        collection.delete_one(self)

    @staticmethod
    def select():
        return collection.find()

    @staticmethod
    def drop():
        collection.drop()
