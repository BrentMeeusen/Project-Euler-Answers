import unittest

from Python.helpers import is_prime, find_first_n_primes


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

        for i, n_i in enumerate(n):
            self.assertEqual(n_i, len(find_first_n_primes(n_i)))
            self.assertEqual(outcomes[i], find_first_n_primes(n_i))


if __name__ == '__main__':
    unittest.main()
