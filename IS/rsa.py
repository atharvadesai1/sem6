import math
 
def findinge(fi):
    num = 2
    while num< fi:
        if math.gcd(num,fi)==1:
            return num
        else:
            num+=1
    return 1
   
def findingd(e,fi):
    # (e*d)mod(fi) == 1
    d = 1
    while d*e > fi:
        d+=1

    while True:
        if (d*e)%fi == 1:
            return d
        else:
            d+=1

print('**************RSA ALGORITHM**************')
p = 41
q = 44
m =12
print()
print(f'Message Data: {m}')
n = p*q
fi = (p-1)*(q-1)
e = findinge(fi)
d = findingd(e,fi)
print(f'Sender Key (e) {e}')
print(f'Reciever Key (d) {d}')

encrypted = (m**e)%n
print(f'Message Encrypted: {encrypted}')

msg_recieved = encrypted

decrypted = (msg_recieved**d)%n
print(f'Message Decrypted: {decrypted}')