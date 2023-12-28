import main
import unittest

class TestPrimeFunctions(unittest.TestCase):

    def test_is_prime(self):
        self.assertFalse(is_prime(1))
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertFalse(is_prime(4))
        self.assertTrue(is_prime(5))
        self.assertFalse(is_prime(9))
        self.assertTrue(is_prime(11))

    def test_get_nth_prime(self):
        self.assertEqual(get_nth_prime(1), 2)
        self.assertEqual(get_nth_prime(2), 3)
        self.assertEqual(get_nth_prime(5), 11)
        self.assertEqual(get_nth_prime(10), 29)
        self.assertEqual(get_nth_prime(20), 71)

    def test_get_nth_prime_invalid_input(self):
        with self.assertRaises(ValueError):
            get_nth_prime(0)

