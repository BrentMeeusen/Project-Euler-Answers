import unittest

from Python.helpers import is_prime


class MyTestCase(unittest.TestCase):
    primes = [2, 3, 5, 7, 11, 17, 23, 37, 59, 83]
    non_primes = [4, 6, 8, 10, 20, 25, 36, 82, 84, 87]

    def test_is_prime(self):
        for prime in self.primes:
            self.assertTrue(is_prime(prime))

        for non_prime in self.non_primes:
            self.assertFalse(is_prime(non_prime))


if __name__ == '__main__':
    unittest.main()
