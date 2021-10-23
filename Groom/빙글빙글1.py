# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
# 문제 : https://level.goorm.io/exam/60331/%EB%B9%99%EA%B8%80%EB%B9%99%EA%B8%80-1/quiz/1
def is_valid(point:list, diff:list, matrix_size:int):
    row, col = point
    row_diff, col_diff = diff
    if row + row_diff < 0 or row + row_diff >= matrix_size \
        or col + col_diff < 0 or col + col_diff >= matrix_size:
        return False
    return True
def get_snail_matrix(matrix_size: int):
    snail_matrix = [[0] * matrix_size for _ in range(matrix_size)]
    point = [0, 0]
    number = 1
    diff = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    stage = 0
    while True:
        row, col = point
        snail_matrix[row][col] = number

        current_stage = stage % len(diff)
        row_diff, col_diff = diff[current_stage]

        # Map 범위를 넘어가는지 확인
        if not is_valid(point, [row_diff, col_diff], matrix_size):
            stage += 1
            current_stage = stage % len(diff)
            row_diff, col_diff = diff[current_stage]
            point = [row + row_diff, col + col_diff]
            number+=1
            continue

        if is_valid(point, [row_diff*2, col_diff*2], matrix_size) and snail_matrix[row + row_diff * 2][col + col_diff * 2]:
            stage += 1
            current_stage = stage % len(diff)
            row_diff, col_diff = diff[current_stage]
            if snail_matrix[row + row_diff*2][col + col_diff*2]:
                break
            point = [row + row_diff, col + col_diff]
        else:
            point = [row + row_diff, col + col_diff]
        number+=1
    return snail_matrix

def get_string_matrix(matrix:list):
    string_matrix = ''
    for row in matrix:
        for col in row:
            if col: string_matrix += '#'
            else: string_matrix += ' '
            string_matrix += ' '
        string_matrix += '\n'
    return string_matrix
user_input = int(input())
snail_matrix = get_snail_matrix(user_input)
#print(snail_matrix)
print(get_string_matrix(snail_matrix))
# print ("Hello Goorm! Your input is " + user_input)

# # # # #
#
# # #   #
#       #
# # # # #