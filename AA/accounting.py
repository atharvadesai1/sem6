n = 10
size  = 1
bal = 0 
ci = 4
 
 
print("Input   Actual Cost      Ci       Bank")
for input in range(1,n+1):
    actual_cost = 0
    if size < input:
        actual_cost += size
        size *= 2
    actual_cost +=1
    bal +=ci - actual_cost 
    print(f'{input}            {actual_cost}           {ci}         {bal}')