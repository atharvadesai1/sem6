def mapreduce(array):
    entered = []
    mapping = {}
    num = 0

    print(f'Input: {array}')

    #Mapping
    for string in array:
        mapping[num] = {}
        for word in string.split(' '):
            if word not in entered:
                entered.append(word)
                mapping[num][word] = 1
            else:
                mapping[num][word] += 1 
        entered = []
        num+=1

    mapping_list = []
    temp1 = []
    for element in mapping:
        for word in mapping[element]:
            temp1.append((word, mapping[element][word]))
        mapping_list.append(temp1)
        temp1 = []
    print(f'Mapping: {mapping_list}')

    #Shuffling
    shuffling_array = []
    for strings in mapping:
        for word in mapping[strings]:
            shuffling_array.append((word, mapping[strings][word]))
    shuffling = []
    temp = []
    for i in range(len(shuffling_array)):
        if shuffling_array[i] != ('x',-1):
            temp.append(shuffling_array[i])
            shuffling_array[i] = ('x',-1)
            for j in range(len(shuffling_array)):
                if temp[0][0] == shuffling_array[j][0]:
                    temp.append(shuffling_array[j])
                    shuffling_array[j] = ('x',-1)
            shuffling.append(temp)
            temp = []
    print(f'Shuffling: {shuffling}')

    #Reducing:
    reducing = []
    temp2 = []
    for sublist in shuffling:
        length = len(sublist)
        temp2.append((sublist[0][0],length))
        reducing.append(temp2)
        temp2 = []
    print(f'Reducing {reducing}')


    #Output:
    output = []
    for sublist in shuffling:
        length = len(sublist)
        output.append((sublist[0][0],length))
    return output

array = ['this is an apple', 'apple is red in colour']
output = mapreduce(array)
print(f'Output: {output}')



