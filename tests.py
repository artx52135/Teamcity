import PrimeNumber
import unittest

class TestPrimeFunctions(unittest.TestCase):

    def test_is_prime(self):
        self.assertFalse(is_prime(9))

    def test_get_nth_prime(self):
        self.assertEqual(get_nth_prime(2), 3)


    def test_get_nth_prime_invalid_input(self):
        with self.assertRaises(ValueError):
            get_nth_prime(0)

