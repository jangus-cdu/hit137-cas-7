"""
HIT137 Assignment 2 Question 1
File: encrypt.py

Provides encryption function as required by Assignment 2 Question 1.

"""

UPPER_A = ord("A")
UPPER_Z = ord("Z")
LOWER_A = ord("a")
LOWER_Z = ord("z")

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

def test_encrypt():
  """
  Tests the encrypt() function
  """
  pass

def main():
  test_encrypt()

# If this is run as a high level module, run testing function
if __name__ == "__main__":
  main()
