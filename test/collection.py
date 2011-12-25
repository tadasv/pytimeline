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
            col.insert([{'test' : 123}])
            raise Exception('Supposed to fail with type error')
        except TypeError:
            pass

        dp = DataPoint()
        dp['test'] = 123
        dp2 = DataPoint()
        dp2['test2'] = 123
        self.assertTrue(col.insert(dp))
        self.assertTrue(dp['_id'])
        self.assertTrue(col.insert([dp2]))
        self.assertTrue(dp2['_id'])

        # Test update operation
        self.assertRaises(TypeError, col.update, {'test': 123}, {'key': 333})
        col.update({'test': 123}, DataPoint({'test' : 123, 'key' : 'value'}))
        # A bit hacky way to get the updated DataPoint.
        # We have to always make sure that there are no other DataPoints
        # with 'test'==123 since we cannot get back the _id since the
        # manipulate is not supported on DataPoint yet.
        obj = col.find({'test' : 123})[0]
        self.assertEqual(obj['key'], 'value')

        # Test save operation
        self.assertRaises(TypeError, col.save, {'key' : 123})
        self.assertEqual(col.find({'save_test' : 'new_datapoint'}).count(), 0)
        col.save(DataPoint({'save_test' : 'new_datapoint'}))
        results = col.find({'save_test' : 'new_datapoint'})
        self.assertEqual(results.count(), 1)
        tmp_dp = results[0]
        self.assertTrue('_id' in tmp_dp)
        tmp_dp['update_test'] = 123
        col.save(tmp_dp)
        results = col.find({'save_test' : 'new_datapoint'})
        self.assertEqual(results.count(), 1)
        tmp_dp = results[0]
        self.assertEqual(tmp_dp['update_test'], 123)




if __name__ == '__main__':
    unittest.main()
