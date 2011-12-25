import unittest

from pytimeline import util

class TestUtil(unittest.TestCase):
    def test_set_value_rec(self):
        d = util.set_value_rec({}, ['a'], 123)
        self.assertEqual(d, {'a' : 123})
        d = util.set_value_rec({}, ['a', 'b'], 123)
        self.assertEqual(d, {'a' : {'b' : 123 }})
        d = util.set_value_rec({'key' : 10}, ['a'], 123)
        self.assertEqual(d, {'key' : 10, 'a' : 123})
        d = util.set_value_rec({'key' : 10}, ['a', 'b'], 123)
        self.assertEqual(d, {'key' : 10, 'a' : {'b' : 123 }})
        d = util.set_value_rec({'key' : 10, 'a' : {'key1' : 10 }}, ['a', 'b'], 123)
        self.assertEqual(d, {'key' : 10, 'a' : {'b' : 123, 'key1' : 10}})


if __name__ == '__main__':
    unittest.main()
