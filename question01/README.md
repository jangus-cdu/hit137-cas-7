# HIT137 - Group Assignment 2

## CAS Group 7 Members

- Jason Angus - S365855
- Marco Giacomelli - S383510
- Yoana Vasileva - S263707

## Question 1

Create a program that reads the text file “raw_text.txt” , encrypts its contents using a simple encryption method, and writes the encrypted text to a new file “encrypted_text.txt” .

Create a function to decrypt the content, and a function to check the correctness of decrypted text.

### Requirements

- Read contents of text file "raw_text.txt"
- Encrypt text by shifting the letters forward by 1.
- If the letter is 'z' make it 'a' or if the letter is 'Z' make it 'A'
- Special characters, and numbers remain unchanged.
- Write encrypted text to file "encrypted_text.txt"
- Create a function to check correctness of decrypt() function

## Algorithms

### Encryption

- Shift each alphabetical character forward by 1 in the alphabet. If the character is 'z' or 'Z' it is shifted to 'a' or 'A'.

### Decryption

- Decrypt the text by shifting each alphabetical character backward by 1 in the alphabet. If the character is 'a' or 'A' it is shifted to 'z' or 'Z' respectively.

## References

### Python Language References

- [Python documentation](https://docs.python.org/3/)

- [The Python Language Reference](https://docs.python.org/3/reference/index.html)

## Markdown References

### CommonMark Spec

- [CommonMark Spec](https://spec.commonmark.org/)

### GitLab Flavored Markdown

- [GitLab Flavored Markdown (GLFM)](https://docs.gitlab.com/ee/user/markdown.html)
