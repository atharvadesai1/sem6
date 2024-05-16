print('******************DEFFIE-HELLMAN KEY EXCHANGE******************')
print()
print('Bob and Alice mutually decides two large prime numbers:')
g = int(input('Enter value of prime number g: '))
n = int(input('Enter value of prime number g: '))
print(f'g = {g} and n = {n}')
print(f'Alice and Bob uses private key x and y respectively')
x = 5 #x is the private key of bob
y = 9 #y is the private key of alice

A = pow(g,x,n) #this will be send to bob
print(f'Alice sends publically A={A} to Bob')
B = pow(g,y,n) #this will be send to alice
print(f'Alice sends publically B={B} to Bob')     

#Now Bob recieves B from Alice
k1 = pow(B,x,n)
#Now Alice recieves A from Bob
k2 = pow(A,y,n)

print(f'K1 = {k1}')
print(f'K2 = {k2}')

if k1 == k2:
    print(f'Since K1 equals K2 thus Bob and Alice will share the key {k1}')
else:
    print(f'Since K1 is not equal to K2 thus they cannot perform operation using these keys')
print()