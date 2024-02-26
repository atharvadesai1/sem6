#columnar cypher
 
def texttonumeric(keytext):
    numtext_dict = {}
    numtext = []
    rank = 1
    sort_keytext = ''.join(sorted(keytext))
 
    for elements in sort_keytext:
        numtext_dict[elements] = rank
        rank+=1
   
    for elements in keytext:
        numtext.append(numtext_dict[elements])
   
    return numtext
 
 
key = 'thunder'
text = 'iamveryhappytodaynice'
cyphertext = ''
print('*******************COLUMNAR CIPHER*******************')
print()
print(f'Key: {key}')
print(f'Plain Text: {text}')
 
key_order = texttonumeric(key)
key_order_str = ''
for e in key_order:
    key_order_str+=str(e)
print(f'Key Numeric: {key_order_str}')
 
rows = int(len(text)/len(key))
matrix = [[0 for _ in range(len(key))] for _ in range(rows)]
 
i = 0
for array in matrix:
    for j in range(len(array)):
        array[j] = text[i]
        i+=1
print()
print('Matrix')
print(matrix)
i=0
 
pit =1
for i in range(len(key)):
    index = key_order.index(pit)
    for array in matrix:
        cyphertext+= array[index]
    pit+=1
print()
print(f'Cypher Text: {cyphertext}')