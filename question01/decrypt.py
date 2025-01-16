"""
HIT137 Assignment 2 Question 1
File: decrypt.py

Provides decryption function as required by Assignment 2 Question 1.
Can test decryption function by running this module directly.
"""

UPPER_A = ord("A")
UPPER_Z = ord("Z")
LOWER_A = ord("a")
LOWER_Z = ord("z")


def decrypt(text="") -> str:
    """
    Decrypts text by shifting each alphabetical character backward by 1 
      character in the alphabet. If the character is 'a' or 'A' it is shifted to 
      'z' or 'Z' respectively.
      Non-alphabetical characters are not changed.

    Parameters:
    text (str): The text to be decrypted

    Returns:
    str: The decrypted text
    """

    decrypted_text = ""  # Stores decrypted text
    for character in text:
        if str.isalpha(character):
            # Wrap-around - Shift first letter of alphabet to last
            # Uppercase 'A'
            if ord(character) == UPPER_A:
                character = chr(UPPER_Z)
            # Lowercase 'a'
            elif ord(character) == LOWER_A:
                character = chr(LOWER_Z)
            else:
                # Decrypt text - shift backward by 1 character
                character = chr(ord(character) - 1)
        decrypted_text += character
    return decrypted_text


def test_decrypt():
    """
    Tests the decrypt() function
    """
    CODED_TEXT = "Uif 1 rvjdl cspxo gpy kvnqt pwfs uif mbaz eph."
    PLAIN_TEXT = "The 1 quick brown fox jumps over the lazy dog."
    print(CODED_TEXT)
    print(decrypt(CODED_TEXT))

    # Test case 1: Empty string
    assert decrypt("") == ""

    # Test case 2: Decrypted coded text should match PLAIN_TEXT
    assert decrypt(CODED_TEXT) == PLAIN_TEXT

    print("All test cases passed!")


def main():
    test_decrypt()


# If this is run as a high level module, run testing function
if __name__ == "__main__":
    main()
