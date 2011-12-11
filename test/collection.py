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


if __name__ == '__main__':
    unittest.main()
