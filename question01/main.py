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

UPPER_A = ord("A")
UPPER_Z = ord("Z")
LOWER_A = ord("a")
LOWER_Z = ord("z")


def main():
  """
  This program encrypts text read from a file named 'raw_text.txt' and saves the
  encrypted text to a file named 'encrypted_text.txt'
  """
  INPUT_FILENAME = 'raw_text.txt'
  OUTPUT_FILENAME = 'encrypted_text.txt'
  infile = open(INPUT_FILENAME)
  outfile = open(OUTPUT_FILENAME, "w")
  encrypted_text = ""
  raw_text = ""
  
  # Encrypting algorithm
  # Increment alphabetical characters by 1. If the character is 'z' or 'Z' 
  # increment it to 'a' or 'A'
  # Special characters and numbers remain unchanged

  # ~DEBUG~ Try encrypt() function on empty string - what happens?
  #  - Remove for final version!
  encrypted_text = encrypt("")
  print(f"Encrypted empty string: '{encrypted_text}'")

  # ~DEBUG~ What happens if we don't pass anything to encrypt()?
  #  - Remove for final version!
  encrypted_text = encrypt()
  print(f"Encrypted None: '{encrypted_text}'")
  # Seems the program crashes because no paramter is passed to encrypt()
  
  for line in infile:
    raw_text += line
    encrypted_text += encrypt(line) # Encrypt each line

  infile.close()
  outfile.write(encrypted_text)
  outfile.close()

  # ~DEBUG~ Displaying encrypted text - Remove for final version
  print("Encypted text:")
  print(encrypted_text)

  decrypted_text = decrypt(encrypted_text)
  # ~DEBUG~ Displaying decrypted text - Remove for final version
  print("Decrypted text:")
  print(decrypted_text)

  # ~DEBUG~ compare original and decrypted texts - Remove for final version
  print("Compare original and decrypted texts - same??:")
  print(raw_text ==  decrypted_text)
  # YES!!


# Check that the program is being run directly and not imported as a module.
# See https://docs.python.org/3/library/__main__.html for more information.
if __name__ == "__main__":
  main()
