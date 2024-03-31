def vig_encryption(plaintext, key):
    s = 0
    ciphertext = ''
    while len(plaintext) != len(key):
        key += key[s%len(key)]
        s+=1
    print(f'key {key}')
    for i in range(len(plaintext)):
        m = int(ord(plaintext[i])-97)
        k = int(ord(key[i])-97)
        if m>=0 and k>=0:
            c = (m+k)%26
            c_cip = str(chr(c+97))
            ciphertext += c_cip
        else:
            print('Enter the valid credentials')
            return 0
    return ciphertext

def vig_decryption(ciphertext, key):
    s = 0
    plaintext = ''
    while len(ciphertext) != len(key):
        key += key[s%len(key)]
        s+=1
    print(f'key {key}')
    for i in range(len(ciphertext)):
        c = int(ord(ciphertext[i])-97)
        k = int(ord(key[i])-97)
        if c>=0 and k>=0:
            if (c-k) < 0:
                asset = int((c-k)+26)
                p = asset%26
            else:
                p = int((c-k)%26)
            p_cip = str(chr(p+97))
            plaintext += p_cip
        else:
            print('Enter the valid credentials')
            return 0
    return plaintext


print('************VIGNERE CIPHER ENCRYPTION************')
plainttext = input('Enter the plaintext: ')
key = input('Enter the key: ')

ciphertext = vig_encryption(plainttext,key)
if ciphertext!= 0:
    print(f'Cipher Text: {ciphertext}')
print()
print('************VIGNERE CIPHER DECRYPTION************')
ciphertext = input('Enter the ciphertext: ')
key = input('Enter the key: ')

plainttext = vig_decryption(ciphertext,key)
if plainttext!= 0:
    print(f'Plain Text: {plainttext}')