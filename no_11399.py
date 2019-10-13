num_data = int(input())
data = input().split(' ')
print(data)
data = list(map(int, data))
data.sort()
print(data)
sum_time = 0
for itr in range(len(data)):
    sum_time += sum(data[:itr + 1])

print(str(sum_time))
