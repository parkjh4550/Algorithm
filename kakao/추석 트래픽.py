# https://programmers.co.kr/learn/courses/30/lessons/17676?language=python3

def log_process(log):
    date = '2016-09-15 '
    data = log.replace(date, '')
    start, sustainment = data.split(' ')

    start = start.replace(':', '')
    start = int(start.replace('.', ''))

    sustainment = sustainment.replace('s', '')
    sustainment = int(float(sustainment) * 1000)

    return start, start +sustainment

def solution(lines):
    start_list, end_list = [], []
    for log in lines:
        start, end = log_process(log)
        start_list.append(start)
        end_list.append(end)

    print(start_list)
    print(end_list)
    task_list = []
    for itr, end in enumerate(end_list):
        num_interval, num_after, num_before = 1 ,1 ,1
        for itr2, start in enumerate(start_list):
            if itr == itr2 : continue
            if start<=end and end<=end_list[itr2]:
                num_after+=1
                num_before+=1
                print(str(itr) + ' interval ->' + str(itr2))
            elif -999 < (end_list[itr2 ] -end) and (end_list[itr2 ] -end) < 0:
                num_before+=1
                print(str(itr) + ' before ->' + str(itr2))
            elif 0< (start - end) and (start - end) < 999:
                num_after += 1
                print(str(itr) + ' after ->' + str(itr2))

        task_list.append(max([num_before, num_after]))
    print(task_list)
    return max(task_list)

input_data = 	["2016-09-15 20:59:57.421 0.351s", "2016-09-15 20:59:58.233 1.181s", "2016-09-15 20:59:58.299 0.8s", "2016-09-15 20:59:58.688 1.041s", "2016-09-15 20:59:59.591 1.412s", "2016-09-15 21:00:00.464 1.466s", "2016-09-15 21:00:00.741 1.581s", "2016-09-15 21:00:00.748 2.31s", "2016-09-15 21:00:00.966 0.381s", "2016-09-15 21:00:02.066 2.62s"]
solution(input_data)