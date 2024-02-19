counter = [0]
prev = 0

print('Sr.no           Actual Cost     Potential       Ammortized Cost Counter')
for x in range(20):
    actual_cost = 0 
    if counter[-1] == 0:
        counter[-1] = 1
        actual_cost+=1
    else:
        index = -1
        while counter[index] == 1:
            counter[index] = 0
            index-=1
            actual_cost+=1
            if index < -len(counter):
                break
        if index < -len(counter):
            counter = [1] + counter
        else:
            counter[index] = 1
        actual_cost+=1
    potential = counter.count(1)
    ammortized_cost = actual_cost + potential - prev
    print(f'{x+1}\t\t{actual_cost}\t\t{potential}\t\t{ammortized_cost}\t\t{counter}')
    prev = potential

