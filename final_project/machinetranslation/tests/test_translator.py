import unittest
from translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):
    def test_english_to_french(self):
        self.assertEqual(english_to_french("the dog"), "Le chien")
        self.assertEqual(english_to_french("the bird"), "L'oiseau")
        self.assertEqual(english_to_french("Hello"), "Bonjour")
        self.assertEqual(english_to_french(None), None)
        
    def test_french_to_english(self):
        self.assertEqual(french_to_english("l'amour"), "Love")
        self.assertEqual(french_to_english("l'enfant"), "The child")
        self.assertEqual(french_to_english("Bonjour"), "Hello")
        self.assertEqual(french_to_english(None), None)

if __name__ == '__main__':
    unittest.main()

