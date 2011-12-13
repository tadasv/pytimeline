import unittest
import pymongo
import datetime

from pytimeline.datapoint import DataPoint
from pytimeline.collection import Collection

class TestCollection(unittest.TestCase):
    def setUp(self):
        self.database = 'test'
        self.collection = 'col'
        self.connection = pymongo.connection.Connection('localhost')

        for i in xrange(10):
            doc = {
                '_dt' : datetime.datetime.today()
            }

            self.connection[self.database][self.collection].insert(doc)


    def tearDown(self):
        self.connection[self.database][self.collection].remove()
        self.connection.disconnect()


    def test_collection(self):
        col = Collection(self.connection[self.database], self.collection)

        for i in col.find():
            self.assertTrue(isinstance(i, DataPoint))


    def test_data_inserts(self):
        col = Collection(self.connection[self.database], self.collection)

        # Test simple data insertion operations
        # DataPoint is only supported data type + lists
        try:
            col.insert({'test' : 123})
            raise Exception('Supposed to fail with type error')
        except TypeError:
            pass

        try:
            col.insert({'test' : 123})
            raise Exception('Supposed to fail with type error')
        except TypeError:
            pass

        dp = DataPoint()
        dp['test'] = 123
        self.assertTrue(col.insert(dp))
        self.assertTrue(col.insert([dp]))



if __name__ == '__main__':
    unittest.main()
