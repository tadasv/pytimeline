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

        try:
            dp['_dt'] = 'invalid'
        except TypeError:
            pass

        dt = datetime.datetime.today()
        dp['_dt'] = dt
        self.assertTrue(isinstance(dp['_dt'],
                        datetime.datetime))

        self.assertEqual(dp['_dt'], dt)
        dpdict = dp.to_dict()
        self.assertEqual(dpdict['_dt'], dt)

        del dp['_dt']
        dpdict = dp.to_dict()
        self.assertTrue(isinstance(dpdict['_dt'], datetime.datetime))


if __name__ == '__main__':
    unittest.main()
