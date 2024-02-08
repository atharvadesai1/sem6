print('*****************Amortized Analysis*****************')
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