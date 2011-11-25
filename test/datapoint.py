import unittest
import datetime
from pytimeline import datapoint


class TestIntegerDateTime(unittest.TestCase):
    def test_conversion(self):
        d1 = datetime.datetime(2011, 11, 11, 11, 11, 11)
        id1 = datapoint.IntegerDateTime(2011, 11, 11, 11, 11, 11)
        self.assertEqual(d1, id1.to_datetime())

        id2 = datapoint.IntegerDateTime()
        id2.from_datetime(d1)
        self.assertEqual(d1, id2.to_datetime())


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
        test_dict['_dt'] = datapoint.IntegerDateTime()
        dt = datapoint.DataPoint(test_dict)


    def test_data_access(self):
        dp = datapoint.DataPoint()

        try:
            dp['_dt'] = 'invalid'
        except TypeError:
            pass

        idt = datapoint.IntegerDateTime()
        dp['_dt'] = idt
        self.assertTrue(isinstance(dp['_dt'],
                        datapoint.IntegerDateTime))

        self.assertEqual(dp['_dt'], idt)
        dpdict = dp.to_dict()
        self.assertEqual(dpdict['_dt'], long(idt))

        del dp['_dt']
        dpdict = dp.to_dict()
        self.assertTrue(isinstance(dpdict['_dt'], long))


if __name__ == '__main__':
    unittest.main()
