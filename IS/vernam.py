# Vernam Cipher


plain = "hellorathodtoourfamily"
key = "barcelona"

alphabet = 'abcdefghijklmnopqrstuvwxyz'
def position(s):
    result = []
    for char in s.lower():
        if char in alphabet:
            result.append(alphabet.index(char))
    return result

def vernam_enc(plain,key):
  plain = position(plain)
  key = position(key)
  print(f'plain {plain}')
  print(f'key {key}')
  cipher = []
  cipher_text = ""
  for i in range(len(plain)):
    cipher_bit = plain[i]^key[i%len(key)]
    cipher.append(cipher_bit)
  print(cipher)
  for bits in cipher:
    cipher_text += alphabet[bits%26]
  print(cipher_text)
  return cipher

def vernam_dec(cipher,key):
  key = position(key)
  plain=""
  for i in range(len(cipher)):
    index = (cipher[i]^key[i%len(key)])
    plain+= alphabet[index]
  print(plain)

cipher = vernam_enc(plain,key)
vernam_dec(cipher,key)
