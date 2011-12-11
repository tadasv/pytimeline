import unittest
import pymongo
import datetime
from pytimeline.datapoint import DataPoint
from pytimeline.cursor import Cursor


class TestCursor(unittest.TestCase):
    def setUp(self):
        self.database = 'test'
        self.collection = 'col'
        self.connection = pymongo.connection.Connection('localhost')

        # Insert a few random docs
        for i in xrange(10):
            doc = {
                '_dt' : datetime.datetime.today()
            }

            self.connection[self.database][self.collection].insert(doc)

    def tearDown(self):
        self.connection[self.database][self.collection].remove()
        self.connection.disconnect()

    def test_cursor(self):
        col = self.connection[self.database][self.collection]

        cursor = Cursor(col)

        for i in cursor:
            self.assertTrue(isinstance(i, DataPoint))

        cursor.rewind()
        self.assertTrue(isinstance(cursor[0], DataPoint))

        cursor.rewind()
        for i in cursor[2:5]:
            self.assertTrue(isinstance(i, DataPoint))


if __name__ == '__main__':
        unittest.main()
