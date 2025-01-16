"""
Group Name: CAS/DAN 07
Group Members:
Jason Angus - S365855
Marco Giacomelli - S383510
Yoana Vasileva - S263707

HIT137 Assignment 2 Question 1
File: main.py

This program uses a simple encryption method to encrypt the contents of a text 
file and writes the encrypted text to a new file.
"""

from encrypt import encrypt
from decrypt import decrypt


def main():
    """
    This program encrypts text read from a file named 'raw_text.txt' and saves the
    encrypted text to a file named 'encrypted_text.txt'
    """
    RAW_TEXT_FILE = 'raw_text.txt'
    ENCRYPTED_TEXT_FILE = 'encrypted_text.txt'
    infile = open(RAW_TEXT_FILE)
    encrypted_text = ""
    raw_text = ""

    # Encrypting algorithm
    # Increment alphabetical characters by 1. If the character is 'z' or 'Z'
    # increment it to 'a' or 'A'
    # Special characters and numbers remain unchanged

    # Read raw text from file line by line
    for line in infile:
        raw_text += line
        encrypted_text += encrypt(line)  # Encrypt each line

    infile.close()

    # Write the encrypted text to a file
    outfile = open(ENCRYPTED_TEXT_FILE, "w")
    outfile.write(encrypted_text)
    outfile.close()

    # Now check that we can decrypt the encrypted text correctly
    # raw_text has the plain unencrytpted text from the raw_text.txt file
    # encrypted_text has the encrypted copy of raw_text

    decrypted_text = decrypt(encrypted_text)
    if decrypted_text == raw_text:
        print("The decrypted text matches the original raw text.")
    else:
        print("The decrypted text does not match the original raw text.")


# Check that the program is being run directly and not imported as a module.
# See https://docs.python.org/3/library/__main__.html for more information.
if __name__ == "__main__":
    main()
