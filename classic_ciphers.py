"""
Add Decrypting Option - as a keyword in functions (e.g. decrypt=True)
"""

# Convert plaintext into capital letters and remove space.
def convert_to_capital(plaintext: str):
    converted_text = ""
    for char in plaintext:
        if char == ' ':
            pass
        elif char.isalpha():
            converted_text += char.upper()
    return converted_text


# Caesar Cipher
def caesar_cipher(capital_plaintext: str, shift: int): # caesar_cipher("NICETOMEETYOU", 5)
    alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    cipher_text = ""
    for char in capital_plaintext:
        cipher_text += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
    return cipher_text



# Rectangular Transposition - Pad with 'X'
def rectangular_transposition(converted_plaintext: str, keyword: str): # rectangular_transposition("HELLOWORLD", "CAT")
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
def affine(converted_plaintext: str, key: tuple): # affine("AFFINECIPHER", (17, 20))
    alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    key_a = key[0]
    key_b = key[1]

    cipher_text = ""
    for char in converted_plaintext:
        new_char = chr(((ord(char) - ord('A')) * key_a + key_b) % 26 + ord('A'))
        cipher_text += new_char
    
    return cipher_text



# Simple Substitution
def simple_substitution(converted_plaintext: str, key: str): # The key should have a length of 26. (Contain all alphabets)
    alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    substitution = {}
    for i, alphabet in enumerate(alphabets):
        substitution[alphabet] = key[i]
    
    cipher_text = ""
    for char in converted_plaintext:
        new_char = substitution[char]
        cipher_text += new_char
    
    return cipher_text


# Polybius Square
def polybius_square(converted_plaintext: str):
    pass

# Hill Cipher


# Vignere Cipher
def vignere(converted_plaintext: str, key: str):
    key = convert_to_capital(key)
    order = [ord(char) - ord('A') for char in key]

    cipher_text = ""
    order_repeated = (order * (len(converted_plaintext) // len(order) + 1))[:len(converted_plaintext)]
    for i, char in zip(order_repeated, converted_plaintext):
        new_char = chr((ord(char) - ord('A') + i) % 26 + ord('A'))
        cipher_text += new_char
    
    return cipher_text


    


# Playfair Cipher


