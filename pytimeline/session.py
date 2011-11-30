import pymongo
from datapoint import DataPointContainer


class Session(object):
    def __init__(self, connection):
        """
        :param: connection: instance of pymongo Connection

        """
        if not isinstance(connection, pymongo.connection.Connection):
            raise TypeError('connection must be an instance of pymongo.connection.Connection')
        self._connection = connection
        self._database = None
        self._collection = None
        # A list of objects that we want to add to the database
        self._modified_objects = DataPointContainer(cast_to_dict=True)


    def use_collection(self, database, collection):
        """
        :param: database: string, database name
        :param: collection: string, collection name

        """
        self._database = self._connection[database]
        self._collection = self._database[collection]


    def add(self, obj):
        """
        :param: obj: object to add, instance of DataPoint

        """
        self._modified_objects.append(obj)


    def flush(self):
        """
        Writes changes to the database

        """
        self._collection.insert(self._modified_objects)
        self._modified_objects.clear()
