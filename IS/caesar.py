# Caesar
offset = 3
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
plain = "MEETMEAFTERTHETOGAPARTY"

def enc(plain,offset):
  cipher = ""
  for bits in plain:
    cipher += alphabet[(alphabet.index(bits)+3)%26]
  return cipher

def dec (cipher,offset):
  plain = ""
  for bits in cipher:
    plain +=alphabet[(alphabet.index(bits)-3)%26]
  return plain

cipher = enc(plain,offset)
print(cipher)
plain_text = dec(cipher,offset)
print(plain_text)