def playfare(key,plaintext):
    letters = 'abcdefghiklmnopqrstuvwxyz'
    rows = 5
    cols = 5
    cyphertext = ''
    matrix = [[0 for j in range(cols)] for i in range(rows)]

    k=0 
    m=0 
    for i in range(5):
        for j in range(5): 
            if(k<=4):
                matrix[i][j] = key[k]
                k+=1
            else:
                while letters[m] in key:
                    m+=1  
                matrix[i][j] = letters[m]
                m+=1
                
    print('Matrix Converted '+str(matrix))

    def find_indices(matrix, element):
        for i, row in enumerate(matrix):
            for j, value in enumerate(row):
                if value == element:
                    return i, j
        return None

    if(len(plaintext)%2!=0):
            plaintext+=plaintext+'x'

    for i in range(len(plaintext)-1):
        if(plaintext[i]==plaintext[i+1]):
            plaintext+= plaintext[:i]+'q'+plaintext[i+1:]+'q'

    for i in range(0,len(plaintext),2):
        i1,j1 = find_indices(matrix, plaintext[i])
        i2,j2 = find_indices(matrix, plaintext[i+1])
        if(i1==i2):
            cyphertext += matrix[i1][(j1+1)%cols] + matrix[i2][(j2+1)%cols]
        if(j1==j2):
            cyphertext += matrix[(i1+1)%rows][j1] + matrix[(i2+1)%rows][j2]
        if(i1!=i2 and j1!=j2):
            cyphertext += matrix[i1][j2] + matrix[i2][j1]

    return cyphertext

print('*****************PLAYFARE-CYPHER*****************')
print()
key = input('Enter the Key: ')
plaint_text = input('Enter the Plain Text: ')
cypher_text = playfare(key,plaint_text)
print('Cypher Text: '+cypher_text)
    