import unittest
import pymongo

from pytimeline.database import Database
from pytimeline.collection import Collection

class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.database = 'test'
        self.connection = pymongo.connection.Connection('localhost')


    def tearDown(self):
        self.connection.disconnect()


    def test_database(self):
        db = Database(self.connection, self.database)

        self.assertTrue(isinstance(db.col, Collection))


if __name__ == '__main__':
    unittest.main()
