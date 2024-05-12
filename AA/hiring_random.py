import random

candidates = [1, 6, 18, 32, 14, 45, 31, 28, 64, 52, 81, 22, 35, 77, 47]
hired_candidates = []
fired_candidates = [] 
interview_cost = 10
total_cost = 0

print('-------------------------------')
print('Cand      IC      HC      TC')
print('-------------------------------')

max = -1
for _ in range(len(candidates)):
    hc = 0
    selected_candidate = random.choice(candidates)
    if selected_candidate > max:
        if max!=-1:
            fired_candidates.append(max)
        hired_candidates.append(selected_candidate)
        max = selected_candidate
        hc += 1
    candidates.remove(selected_candidate)
    total_cost += interview_cost + (hc*interview_cost)
    print(f'{selected_candidate}         {interview_cost}       {hc*interview_cost}       {interview_cost + (hc*interview_cost)}')

print(f'List of Hired candidates till now: {hired_candidates}')
print(f'Total Hiring Cost: {len(hired_candidates)*interview_cost}')
print(f'List of Fired Candidates: {fired_candidates}')
print(f'Total Firing Cost: {len(fired_candidates)*interview_cost}')
print(f'Current Hired Assistant: {max}')
print(f'Total Cost: {total_cost}')


