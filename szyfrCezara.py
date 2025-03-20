class CaesarCipher:
    def __init__(self, shift: int):
        if not isinstance(shift, int):
            raise ValueError("Shift must be an integer.")
        self.shift = shift
        self.start_ascii = 32  # Pierwszy drukowalny znak ASCII
        self.end_ascii = 126  # Ostatni drukowalny znak ASCII
        self.range_ascii = self.end_ascii - self.start_ascii + 1

    def _shift_char(self, char: str, shift: int) -> str:
        ascii_code = ord(char)
        if self.start_ascii <= ascii_code <= self.end_ascii:
            new_code = ((ascii_code - self.start_ascii + shift) % self.range_ascii) + self.start_ascii
            return chr(new_code)
        return char  # Nie zmieniamy znaków poza zakresem

    def encrypt(self, text: str) -> str:
        if not isinstance(text, str) or not text:
            raise ValueError("Input must be a non-empty string.")
        return ''.join(self._shift_char(char, self.shift) for char in text)

    def decrypt(self, text: str) -> str:
        if not isinstance(text, str) or not text:
            raise ValueError("Input must be a non-empty string.")
        return ''.join(self._shift_char(char, -self.shift) for char in text)

# Przykładowe użycie:
cipher = CaesarCipher(shift=3)
original_text = "Hello World!"

encrypted_text = cipher.encrypt(original_text)
decrypted_text = cipher.decrypt(encrypted_text)

print(f"Original: {original_text}")
print(f"Encrypted: {encrypted_text}")
print(f"Decrypted: {decrypted_text}")
