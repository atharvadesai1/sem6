# RSA
p = 7
q = 11
e = 13
plain = 57
print(f'*******************RSA ALGORITHM*******************')
print()
print(f'p={p} , q={q} , Public Key (e)={13} , Private Key (d)=?')
print(f'Message: {plain}')

n = p*q
phi = (p-1)*(q-1)

for x in range(0,phi):
  if (x*e)%phi == 1:
    d = x
    break
print('Calculating d....')
print(f'Private Key (d)={d}')

def enc(plain,e,n):
  cipher = pow(plain,e,n)
  return cipher


def dec (cipher,d,n):
  plain = pow(cipher,d,n)
  return plain

cipher_text = enc(plain,e,n)
print('Cipher Text: '+ str(cipher_text))
plain_text = dec(cipher_text,d,n)
print('Plain Text: '+ str(plain_text))