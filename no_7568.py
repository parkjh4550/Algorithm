num_human = int(input())
data = [input().split(' ') for i in range(0,num_human)]
#print(data)

rank = []
result = ''
# weight , height
for itr, person in enumerate(data):
    cnt = 0
    for itr2, person2 in enumerate(data):
        if itr==itr2: continue
        if person2[0] > person[0] and person2[1]>person[1]:
            cnt += 1
    rank.append(cnt+1)
    result = result+ ' '+ str(cnt+1)
print(result[1:])
"""
grade = list(set(rank))
for itr, person_rank in enumerate(rank):
    rank[itr] = grade.index(person_rank) +1
    print(rank[itr])
"""