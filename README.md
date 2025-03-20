Caesar Cipher in Python

Opis projektu
Ten projekt zawiera implementację szyfru Cezara na tablicy ASCII z pominięciem pierwszych 32 kodów (znaki niedrukowalne). Dodatkowo, projekt zawiera testy jednostkowe weryfikujące poprawność operacji szyfrowania i deszyfrowania.

Funkcjonalności
Szyfrowanie dowolnego ciągu znaków za pomocą szyfru Cezara.
Deszyfrowanie zaszyfrowanego ciągu znaków.
Obsługa błędnych danych wejściowych (np. wartości inne niż stringi, wartości puste).
Testy jednostkowe w Pythonie weryfikujące poprawność funkcji.

Instalacja
1. Sklonuj repozytorium:

bash
git clone <link_do_repozytorium>

2. Upewnij się, że masz zainstalowanego Pythona w wersji 3.x.
3. Zainstaluj wymagane pakiety:
bash
pip install -r requirements.txt



Jak używać
1. Użyj klasy implementującej szyfr Cezara do szyfrowania lub deszyfrowania ciągów znaków.
2. Aby uruchomić testy jednostkowe, wykonaj:
bash
python -m unittest


Struktura projektu:

ceasar_cipher.py – implementacja szyfru Cezara.
test_ceasar_cipher.py – plik zawierający testy jednostkowe.

## Źródła
- [Testy jednostkowe w Pythonie - jak pisać i optymalizować](https://programistajava.pl/2025/01/03/testy-jednostkowe-w-pythonie-jak-pisac-i-optymalizowac/)
