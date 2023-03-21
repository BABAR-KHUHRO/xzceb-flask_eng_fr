import unittest

from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french("Hello"),"Bonjour")
        # self.assertEqual(english_to_french("Welcome"),"Bienvenue")
        # self.assertEqual(english_to_french("Love"),"Amour")
        self.assertNotEqual(english_to_french("Hello"),("boqour"))
        #self.assertEqual(englishtofrench(""),"error")

class TestFrenchToEnglish(unittest.TestCase):
    def test1(self):
        self.assertEqual(french_to_english("Bonjour"),"Hello")
        self.assertNotEqual(english_to_french("Bonjour"),("Yello"))
        # self.assertEqual(french_to_english("Bienvenue"),"Welcome")
        # self.assertEqual(french_to_english("Amour"),"Love")

unittest.main()