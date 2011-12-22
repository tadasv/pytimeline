import unittest
import datetime

from pytimeline import naming

class TestNaming(unittest.TestCase):
    def test_name_getters(self):
        self.assertEqual(naming.monthly_name('p', datetime.date(2011, 2, 2)),
                         'p201102')
        self.assertEqual(naming.yearly_name('p', datetime.date(2011, 3, 4)),
                         'p2011')
        self.assertEqual(naming.daily_name('p', datetime.date(2011, 1, 31)),
                        'p2011031')
        self.assertEqual(naming.daily_name('p', datetime.date(2011, 2, 1)),
                        'p2011032')


    def test_name_generators(self):
        self.assertRaises(AssertionError, naming.Generator, "prefix",
                            "", datetime.date.today())
        self.assertRaises(AssertionError, naming.Generator, "prefix",
                            datetime.date.today(), "")
        self.assertRaises(AssertionError, naming.Generator, "prefix",
                            "", datetime.datetime.today())
        self.assertRaises(AssertionError, naming.Generator, "prefix",
                            datetime.datetime.today(), "")


        # Test daily generator
        gen = naming.DailyGenerator("p", datetime.date(2011, 1, 28),
                                         datetime.date(2011, 2, 2))
        names = gen.get_list()
        self.assertEqual(names, [
                            "p2011028",
                            "p2011029",
                            "p2011030",
                            "p2011031",
                            "p2011032",
                            "p2011033",
                        ])


if __name__ == '__main__':
    unittest.main()
