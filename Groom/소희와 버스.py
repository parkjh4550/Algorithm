# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
# 문제 : https://level.goorm.io/exam/49107/%EC%86%8C%ED%9D%AC%EC%99%80-%EB%B2%84%EC%8A%A4/quiz/1
def get_bus_arrival(list_bus_info: list, time_arrive: int):
    list_min_time = []
    for start, period in list_bus_info:
        if start >= time_arrive:
            list_min_time.append(start)
            continue

        time = start
        while True:
            time += period
            if time >= time_arrive:
                break
        list_min_time.append(time)
    return list_min_time


num_bus, time_arrive = list(map(int, input().split()))
list_bus_info = [list(map(int, input().split())) for _ in range(num_bus)]

list_min_time = get_bus_arrival(list_bus_info, time_arrive)
bus_num = list_min_time.index(min(list_min_time)) + 1
print(bus_num)
