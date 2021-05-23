from repository.client import db
collection = db["files"]


class FilesCollection:
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
    def select():
        return collection.find()

    @staticmethod
    def drop():
        collection.drop()

    @staticmethod
    def get_duplicated_size_and_type():
        pipeline = [
            {
                '$group': {
                    '_id': {
                        'width': '$metadata.width',
                        'height': '$metadata.height',
                        'type': '$metadata.type',
                        'channel': '$metadata.channel'
                    },
                    'count': {
                        '$sum': 1
                    },
                    'results': {
                        '$push': '$$ROOT'
                    }
                }
            },
            {
                '$match': {
                    'count': {
                        '$gte': 2
                    }
                }
            }
        ]

        return list(collection.aggregate(pipeline=pipeline))
