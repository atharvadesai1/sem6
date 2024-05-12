import math

interview = [70, 70, 30, 10]
exam_rank = [70, 40, 40, 40]
classes = ['not hired', 'hired', 'not hired', 'not hired']

data = {
    'first': [70, 70, 'not hired'],
    'second': [70, 40, 'hired'],
    'third': [30, 40, 'not hired'],
    'fourth': [10, 40, 'not hired'],
}

x = 30
y = 70

distance1 = []
distance2 = []
response = []

for i in range(len(interview)):
    s = (interview[i] - x)**2 + (exam_rank[i] - y)**2
    s = math.sqrt(s)
    distance1.append(s)
    distance2.append(s)

distance2.sort()

for i in range(len(distance1)):
    for j in range(len(distance2)):
        if(distance1[i] == distance2[j]):
            if j == 0:
                response.append(data['first'][2])
            elif j == 1:
                response.append(data['second'][2])
            elif j == 2:
                response.append(data['third'][2])
            elif j == 3:
                response.append(data['fourth'][2])

k = 3
countNH = countH = 0

for i in range(k):
    if response[i] == 'not hired':
        countNH += 1
    else:
        countH += 1

if countNH > countH:
    print('Type for {} and {} will be not hired.'.format(x, y))
else:
    print('Type for {} and {} will be hired.'.format(x, y))
