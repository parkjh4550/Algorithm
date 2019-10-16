def solution(triangle):
    answer = 0
    sum = [triangle[0]]
    for itr, numbers in enumerate(triangle[1:]):
        tmp = []
        tmp.append(sum[itr][0] + numbers[0])

        if len(numbers) >= 3:
            print(sum)
            print(numbers[1:-1])
            for itr2, num in enumerate(numbers[1:-1]):
                tmp.append(sum[itr][(itr2) * 2 ] + num)
                tmp.append(sum[itr][(itr2) * 2+1] + num)

        tmp.append(sum[itr][-1] + numbers[-1])
        sum.append(tmp[:])

    return max(sum[-1])


# get all possible case for each line
def solution(triangle):
    answer = 0
    sum = [[triangle[0]]]

    max_value = 0
    for itr, numbers in enumerate(triangle[1:]):
        tmp = []
        tmp.append([sum[itr][0][0] + numbers[0]])
        tmp_max = 0
        if len(numbers) >= 3:
            print(sum)
            print(numbers[1:-1])

            for itr2, num2 in enumerate(numbers[1:-1]):
                tmp2 = []
                print('sum[itr]:', sum[itr])


                for itr3, num3 in enumerate(sum[itr][(itr2)]):
                    tmp2.extend([num3 + num2])
              
                for itr4, num4 in enumerate(sum[itr][(itr2) +1]):
                    tmp2.extend([num4 + num2])
                tmp.append(tmp2[:])
                if max(tmp2)>tmp_max: tmp_max=max(tmp2)

        tmp.append([sum[itr][-1][0] + numbers[-1]])
        sum.append(tmp[:])

        print('tmp : ', tmp)
        if max([tmp[0][0], tmp[0][-1], tmp_max]) > max_value:
            max_value = max([tmp[0][0], tmp[0][-1], tmp_max])

    return max_value

    """    
    max_value = 0
    for line in sum[-1]:
        element_max = max(line)
        if max_value < element_max:
            max_value=element_max
    return max_value
    """


# get only "max" of the possible value for each elements

def solution(triangle):
    answer = 0
    sum = [[triangle[0]]]

    max_value = 0
    for itr, numbers in enumerate(triangle[1:]):
        tmp = []
        tmp.append([sum[itr][0][0] + numbers[0]])
        tmp_max = 0
        if len(numbers) >= 3:
            print(sum)
            print(numbers[1:-1])

            for itr2, num2 in enumerate(numbers[1:-1]):
                tmp2 = []
                print('sum[itr]:', sum[itr])

                for itr3, num3 in enumerate(sum[itr][(itr2)]):
                    tmp2.extend([num3 + num2])

                for itr4, num4 in enumerate(sum[itr][(itr2) + 1]):
                    tmp2.extend([num4 + num2])
                tmp.append([max(tmp2[:])])

        tmp.append([sum[itr][-1][0] + numbers[-1]])
        sum.append(tmp[:])


    return max(sum[-1])

sample =[[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
print(solution(sample))