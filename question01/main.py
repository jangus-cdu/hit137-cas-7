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

  # ~DEBUG~ Displaying ASCII values - Remove for final version
  # print(f"UPPER_A: {UPPER_A}")
  # print(f"UPPER_Z: {UPPER_Z}")
  # print(f"LOWER_A: {LOWER_A}")
  # print(f"LOWER_Z: {LOWER_Z}")


  
def encrypt(text="") -> str:
  """
  Encrypts text by shifting each alphabetical character forward by 1 in the 
  alphabet. If the character is 'z' or 'Z' it is shifted to 'a' or 'A'.
  Non-alphabetical characters are not changed.

  Parameters:
  text (str): The text to be encrypted

  Returns:
  str: The encrypted text
  """
  encrypted_text = "" # For storing encrypted text
  for character in text:
      # Check for alphabetical character 
      if str.isalpha(character):
        # Wrap-around - Shift last letter of alphabet to first
        # Uppercase 'Z'
        if ord(character) == UPPER_Z:
          character = chr(UPPER_A)
        # Lowercase 'z'
        elif ord(character) == LOWER_Z:
          character = chr(LOWER_A)
        else:
          # Basic encryption - shift forward by 1 character
          character = chr(ord(character) + 1)
      encrypted_text += character
  return encrypted_text

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
    decrypted_text = "" # Stores decrypted text
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



# Check that the program is being run directly and not imported as a module.
# See https://docs.python.org/3/library/__main__.html for more information.
if __name__ == "__main__":
  main()
