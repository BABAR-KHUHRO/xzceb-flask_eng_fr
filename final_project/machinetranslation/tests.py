import unittest

from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french("Hello"),"Bonjour")
        self.assertEqual(english_to_french("Welcome"),"Bienvenue")
        self.assertEqual(english_to_french("Love"),"Amour")
        self.assertNotEqual(english_to_french(" "),"error")

class TestFrenchToEnglish(unittest.TestCase):
    def test1(self):
        self.assertEqual(french_to_english("Bonjour"),"Hello")
        self.assertEqual(french_to_english("Bienvenue"),"Welcome")
        self.assertNotEqual(french_to_english(" "),"error")

unittest.main()