import unittest
from szyfrCezara import CaesarCipher  

class TestCaesarCipher(unittest.TestCase):
    def setUp(self):
        self.cipher = CaesarCipher(shift=3)
    
    def test_encrypt_decrypt(self):
        text = "Hello World!"
        encrypted = self.cipher.encrypt(text)
        decrypted = self.cipher.decrypt(encrypted)
        self.assertEqual(decrypted, text)
    
    def test_encrypt(self):
        self.assertEqual(self.cipher.encrypt("abc"), "def")
        self.assertEqual(self.cipher.encrypt("xyz"), "{|}")
    
    def test_decrypt(self):
        self.assertEqual(self.cipher.decrypt("def"), "abc")
        self.assertEqual(self.cipher.decrypt("{|}"), "xyz")
    
    def test_non_string_input(self):
        with self.assertRaises(ValueError):
            self.cipher.encrypt(123)
        with self.assertRaises(ValueError):
            self.cipher.decrypt(123)
    
    def test_empty_string(self):
        with self.assertRaises(ValueError):
            self.cipher.encrypt("")
        with self.assertRaises(ValueError):
            self.cipher.decrypt("")
    
    def test_special_characters(self):
        text = "!@# $%^"
        encrypted = self.cipher.encrypt(text)
        decrypted = self.cipher.decrypt(encrypted)
        self.assertEqual(decrypted, text)

if __name__ == "__main__":
    unittest.main()