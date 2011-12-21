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


if __name__ == '__main__':
    unittest.main()
