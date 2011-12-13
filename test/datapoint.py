import unittest
import datetime
from pytimeline import datapoint


class TestDataPoint(unittest.TestCase):

    def test_constructors(self):
        dt = datapoint.DataPoint()
        self.assertTrue('_dt' in dt)

        test_dict = {
            'key1' : 123,
            'key2' : 'abc'
        }

        dt = datapoint.DataPoint(test_dict)
        self.assertEqual(dt['key1'], test_dict['key1'])
        self.assertEqual(dt['key2'], test_dict['key2'])
        self.assertTrue('_dt' in dt)

        # Test datapoint from dict with invalid
        # datetime field
        test_dict['_dt'] = 'invalid'
        self.assertRaises(TypeError, datapoint.DataPoint, test_dict)

        # Test datapoint with valid datetime
        test_dict['_dt'] = datetime.datetime.today()
        dt = datapoint.DataPoint(test_dict)


    def test_data_access(self):
        dp = datapoint.DataPoint()

        # Checks for invalid timestamp key values
        # work only in constructors. Checks are not performed
        # at __setitem__ due to the possibility of nested timestamp.
        # However, the timestamp check will be perfoemd when converting
        # DataPoint to dict before pushing it to mongodb.
        dp['_dt'] = 'invalid'
        try:
            dp.to_dict()
            raise Exception('Supposed to raise TypeError')
        except TypeError:
            pass

        dt = datetime.datetime.today()
        dp['_dt'] = dt
        self.assertTrue(isinstance(dp['_dt'],
                        datetime.datetime))

        self.assertEqual(dp['_dt'], dt)
        dpdict = dp.to_dict()
        self.assertEqual(dpdict['_dt'], dt)

        # Test nested time stamps




if __name__ == '__main__':
    unittest.main()
