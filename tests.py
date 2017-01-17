import unittest

from GeneratingPrimeNumbers import prime_generator

class PrimesFunctionTestCase(unittest.TestCase):
    def test_negative_input(self):
        with self.assertRaises(ValueError):
            prime_generator(-5)

    def test_output_is_list(self):
        self.assertIsInstance(prime_generator(10), list)

    def test_two_is_prime(self):
        self.assertIn(2, prime_generator(10))

    def test_one_not_prime(self):
        self.assertNotIn(1, prime_generator(8))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            prime_generator("string")

    def test_correct_output(self):
        self.assertEqual(prime_generator(5), [2, 3, 5])

if __name__ == '__main__':
    unittest.main()
