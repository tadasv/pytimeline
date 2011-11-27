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


class TestDataPointContainer(unittest.TestCase):
    def test_container(self):
        """ Test container, add/remove etc. """
        dpcontainer = datapoint.DataPointContainer()
        self.assertEqual(len(dpcontainer), 0)

        try:
            dpcontainer.append(1)
        except TypeError:
            pass

        dp = datapoint.DataPoint()
        dpcontainer.append(dp)
        self.assertEqual(len(dpcontainer), 1)

        try:
            dpcontainer.insert(1, 1)
        except TypeError:
            pass

        dpcontainer.insert(1, datapoint.DataPoint())
        self.assertEqual(len(dpcontainer), 2)

        dpcontainer.clear()
        self.assertEqual(len(dpcontainer), 0)


    def test_iterator(self):
        dpcontainer = datapoint.DataPointContainer(cast_to_dict=False)
        l = [
            datapoint.DataPoint(),
            datapoint.DataPoint(),
            datapoint.DataPoint()
        ]

        for i in l:
            dpcontainer.append(i)

        for i in range(len(dpcontainer)):
            self.assertEqual(l[i], dpcontainer[i])


        counter = 0
        for i in dpcontainer:
            counter += 1
        self.assertEqual(counter, 3)


if __name__ == '__main__':
    unittest.main()
