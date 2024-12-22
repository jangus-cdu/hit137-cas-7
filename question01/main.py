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
UPPER_A = ord("A")
UPPER_Z = ord("Z")
LOWER_A = ord("a")
LOWER_Z = ord("z")
ASCII_OFFSET = abs(UPPER_Z-UPPER_A)


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
  
  # First attempt at encrypting text
  # Encrypting algorithm
  # Increment alphabetical characters by 1. If the character is 'z' or 'Z' 
  # increment it to 'a' or 'A'
  # Special characters and numbers remain unchanged
  for line in infile:
    for character in line:
      if str.isalpha(character):
        # Uppercase Letters
        if ord(character) >= UPPER_A and ord(character) <= UPPER_Z:
          offset = ((ord(character) - UPPER_A) + 1) % 26
          character = chr(UPPER_A + offset)
        # Lowercase Letters
        elif ord(character) >= LOWER_A and ord(character) <= LOWER_Z:
          offset = ((ord(character) - LOWER_A) + 1) % 26
          character = chr(LOWER_A + offset)
      encrypted_text += character

  print("Encypted text:")
  print(encrypted_text)

  # ~DEBUG~ Displaying ASCII values  
  print(f"UPPER_A: {UPPER_A}")
  print(f"UPPER_Z: {UPPER_Z}")
  print(f"LOWER_A: {LOWER_A}")
  print(f"LOWER_Z: {LOWER_Z}")
  print(f"ASCII_OFFSET: {ASCII_OFFSET}")
  

# Check that the program is being run directly and not imported as a module.
# See https://docs.python.org/3/library/__main__.html for more information.
if __name__ == "__main__":
  main()
