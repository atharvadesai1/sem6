import random
 
print("***********HIRING PROBLEM (RANDOMIZE)***********")
print("----------------------------")
print("Cand   IC        HC       TC")
print("----------------------------")
 
candidates = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
interviewed_candidates = []
hired_candidates = []
total_cost = 0
interview_cost = 10
 
for i in range(len(candidates)):
    selected_candidate = random.choice(candidates)
    interviewed_candidates.append(selected_candidate)
    candidates.remove(selected_candidate)
 
 
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