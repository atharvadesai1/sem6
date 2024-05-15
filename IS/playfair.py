def playfair(key,plaintext):
    letters = 'abcdefghiklmnopqrstuvwxyz'
    rows = 5
    cols = 5
    cyphertext = ''
    matrix = [[0 for _ in range(cols)] for _ in range(rows)]
    k=0 
    m=0 
    for i in range(5):
        for j in range(5): 
            if(k<=len(key)-1):
                matrix[i][j] = key[k]
                k+=1
            else:
                while letters[m] in key:
                    m+=1  
                matrix[i][j] = letters[m]
                m+=1        

    print('Matrix Converted ')
    for row in matrix:
        print(str(row)) 
    
    def find_indices(matrix, element):
        for i, row in enumerate(matrix):
            for j, value in enumerate(row):
                if value == element:
                    return i, j
        return None
    
    if(len(plaintext)%2!=0):
            plaintext+='x'

    for i in range(0,len(plaintext),2):
        if(plaintext[i]==plaintext[i+1]):
            plaintext = plaintext[:i+1]+'q'+plaintext[i+1:]+'q'
    print('Plain Text After Tranformation: '+plaintext)

    for i in range(0,len(plaintext),2):
        i1,j1 = find_indices(matrix, plaintext[i])
        i2,j2 = find_indices(matrix, plaintext[i+1])
        if(i1==i2): #same row
            cyphertext += matrix[i1][(j1+1)%cols] + matrix[i2][(j2+1)%cols]
        if(j1==j2): #same column
            cyphertext += matrix[(i1+1)%rows][j1] + matrix[(i2+1)%rows][j2]
        if(i1!=i2 and j1!=j2):
            cyphertext += matrix[i1][j2] + matrix[i2][j1]

    return cyphertext

print('*****************PLAYFAIR-CYPHER (ENCRYPTION)*****************')
print()
key = input('Enter the Key: ')
plaint_text = input('Enter the Plain Text: ')
cypher_text = playfair(key,plaint_text)
print('Cypher Text: '+cypher_text)
