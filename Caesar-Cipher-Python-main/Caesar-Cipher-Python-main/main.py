alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd',
    'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
    't', 'u', 'v', 'w', 'x', 'y', 'z'
]
#monem
import art

print(art.logo)


def encrypt(text, shift):
  cipher_text = ""
  for letter in text:
    if letter not in alphabet:
      cipher_text += letter
    else:
      pos = alphabet.index(letter) + shift
      cipher_text += alphabet[pos]
  print(f"the encoded text is: {cipher_text}\n")


def decrypt(text, shift):
  cipher_text = ""
  for letter in text:
    if letter not in alphabet:
      cipher_text += letter
    else:
      pos = alphabet.index(letter) + 26 - shift
      cipher_text += alphabet[pos]
  print(f"the decoded text is: {cipher_text}\n")


continuee = True
while continuee:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n\n")
  text = input("\nType your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  if direction == "encode":
    encrypt(text, shift)
  if direction == "decode":
    decrypt(text, shift)
  ask = input("Do You Want to Continue(Y/N): \n").lower()
  if ask == 'n':
    continuee = False
    print("\nGoodBye")
  elif ask == 'y':
    continuee = True
