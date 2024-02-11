
print("***********HIRING PROBLEM (WORST CASE)***********")
print("----------------------------")
print("Cand   IC        HC       TC")
print("----------------------------")
 
candidates = [7,5,1,8,4,0,3,2,9,6]
hired_candidates = []
total_cost = 0
interview_cost = 10 
candidates.sort()
interviewed_candidates = candidates
 
 
max=-1
for i in range(len(interviewed_candidates)):
    hc=0
    if interviewed_candidates[i] > max:
        max=interviewed_candidates[i]
        hired_candidates.append(interviewed_candidates[i])
        hc+=1
    print(f"{interviewed_candidates[i]}      {interview_cost}        {hc*interview_cost}       {interview_cost+(hc*interview_cost)}")
    total_cost+=interview_cost+(hc*interview_cost)
 
print()
print("Interviewed candidates:", interviewed_candidates)
print("Hired candidates:", hired_candidates)
print("Number of candidates hired:", len(hired_candidates))
print("Hiring Cost: ", interview_cost*len(hired_candidates))
print("Firing Cost: ", interview_cost*(len(hired_candidates)-1))
print("Total Cost: ",total_cost)