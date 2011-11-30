import unittest
import pymongo
from pytimeline import session, datapoint


class TestSession(unittest.TestCase):
    def setUp(self):
        self.database = 'test'
        self.collection = 'col'
        self.connection = pymongo.connection.Connection('localhost')

        self.session = session.Session(self.connection)
        self.session.use_collection(self.database, self.collection)

    def tearDown(self):
        self.connection[self.database][self.collection].remove()
        self.connection.disconnect()

    def test_new_data(self):
        # Simple test cases for checking data insertion
        dp1 = datapoint.DataPoint()
        self.session.add(dp1)
        self.session.flush()
        self.assertEqual(self.connection[self.database][self.collection].find().count(), 1)

        # Try adding multiple documents at once
        self.session.add(dp1)
        self.session.add(dp1)
        self.session.flush()
        self.assertEqual(self.connection[self.database][self.collection].find().count(), 3)

if __name__ == '__main__':
    unittest.main()
