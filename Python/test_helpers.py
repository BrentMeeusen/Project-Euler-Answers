import unittest

from Python.helpers import is_prime, find_first_n_primes, find_primes_below_n


class MyTestCase(unittest.TestCase):
    primes = [2, 3, 5, 7, 11, 17, 23, 37, 59, 83]
    non_primes = [4, 6, 8, 10, 20, 25, 36, 82, 84, 87]

    def test_is_prime(self):
        for prime in self.primes:
            self.assertTrue(is_prime(prime))

        for non_prime in self.non_primes:
            self.assertFalse(is_prime(non_prime))

    def test_find_first_n_primes(self):
        n = [0, 1, 2, 5, 10]
        outcomes = [[], [2], [2, 3], [2, 3, 5, 7, 11], [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]]

        for i, outcome in enumerate(outcomes):
            self.assertEqual(n[i], len(find_first_n_primes(n[i])))
            self.assertEqual(outcome, find_first_n_primes(n[i]))

    def test_find_primes_below_n(self):
        n = [2, 3, 8, 16, 20]
        outcomes = [[], [2], [2, 3, 5, 7], [2, 3, 5, 7, 11, 13], [2, 3, 5, 7, 11, 13, 17, 19]]

        for i, outcome in enumerate(outcomes):
            self.assertEqual(outcome, find_primes_below_n(n[i]))


if __name__ == '__main__':
    unittest.main()
