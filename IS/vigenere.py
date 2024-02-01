def vigenere(key,plaintext):
    matrix = [[0 for j in range(26)] for i in range(26)]
    letters = 'abcdefghijklmnopqrstuvwxyz'
    k=0
    for i in range(26):
        m=k
        for j in range(26):
            matrix[i][j] = letters[m%26]
            m+=1
        k+=1
    print(f'Matrix:\n {matrix}')
    new_key = ''
    for i in range(len(plaintext)):
        new_key+= key[i%(len(key))]

    cyphertext = ''
    for i in range(len(plaintext)):
        row_index = ord(new_key[i])-97
        col_index = ord(plaintext[i])-97
        cyphertext += matrix[row_index][col_index]
    return cyphertext

print('*****************VIGENERE-CYPHER*****************')
print()
key = input('Enter the Key: ')
plaint_text = input('Enter the Plain Text: ')
cypher_text = vigenere(key,plaint_text)
print('Cypher Text: '+cypher_text)
