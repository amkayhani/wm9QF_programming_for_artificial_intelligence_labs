import unittest

class TestCountVowels(unittest.TestCase):
    def test_consonants(self):
        self.assertEqual(count_vowels("rhythm"), 0)

    def test_all_vowels(self):
        self.assertEqual(count_vowels("aeiou"), 5)

if __name__ == "__main__":
    unittest.main()