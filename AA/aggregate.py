print('*****************Amortized Analysis (Aggregate Method) for Augmented Stack*****************')
arr = [11,7,8,9,3,2,7,8,5]
print(f'Items Taken: {arr}')
print()
stack = []
total_cost = 0
cost =0
 
 
for i in range(len(arr)):
    if(arr[i]<=len(stack)):
        for j in range(arr[i]):
            if stack:
                stack.pop()
                cost+=1
                total_cost+=1
            else:
                break
        stack.append(arr[i])
        total_cost+=1
        cost+=1
        print(f'{stack} {cost}')
        cost=0
    else:
        stack.append(arr[i])
        total_cost+=1
        cost+=1
        print(f'{stack} {cost}')
        cost=0
 
print()
print(f'Total Cost: {total_cost}')
print(f'Aggregate Cost: {total_cost/len(arr)}')

print()
print()
print('*********************Amortize Analysis: Aggregate Method for Dynamic Tables*********************')
arr = [i for i in range(1,17)]
print(f'arr : {arr}')
size = []
size_len = 1
cost = [1]
cost_count = 1
for i in range(len(arr)):
    if size_len < arr[i]:
        size_len = size_len*2
        size.append(size_len)
    else:
        size.append(size_len)

print(f'sze : {size}')
for i in range(1, len(arr)):
    if arr[i] > size[i-1]:
        cost.append(arr[i])
    else:
        cost.append(1)
print(f'cst : {cost}')

print('Array        Size        Cost')

for i in range(len(arr)):
    print(f'{arr[i]}            {size[i]}           {cost[i]}')

print(f'Ammortized Cost: {sum(cost)}')








