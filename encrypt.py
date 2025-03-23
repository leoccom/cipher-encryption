

# Conver Plaintext into Capital Letters
def convert_to_capital(plaintext: str):
    converted_text = ""
    for char in plaintext:
        if char == ' ':
            pass
        elif char.isalpha():
            converted_text += char.upper()
    return converted_text


# Caesar Cipher
def caesar_cipher(capital_plaintext: str, shift: int):
    alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    cipher_text = ""
    for char in capital_plaintext:
        cipher_text += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
    return cipher_text

test_text = "Nice to meet you!"
print(caesar_cipher(capital_plaintext=convert_to_capital(test_text), shift=5))


# Rectangular Transposition - Pad with 'X'
def rectangular_transposition(converted_plaintext: str, keyword: str):
    """
    The keyword should contain at most one of each character (unique characters only).
    """
    n = len(converted_plaintext)
    k = len(keyword)
    if (n % k) != 0: converted_plaintext += (k - (n % k)) * 'X'
    n = len(converted_plaintext)
    
    sorted_keyword = sorted(list(keyword))
    order = [(sorted_keyword.index(char)) for char in keyword]

    rows = [converted_plaintext[i * k : (i + 1) * k] for i in range(n // k)]
    cipher_text = "".join("".join(row[j] for j in order) for row in rows)

    return cipher_text


# Affine Cipher
def affine(converted_plaintext: str):
    pass

# Simple Substitution


# Polylbius Square


# Hill Cipher


# Vignere Cipher


# Playfair Cipher


