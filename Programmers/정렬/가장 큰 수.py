# https://programmers.co.kr/learn/courses/30/lessons/42746#qna
def solution(numbers):
    if len(set(numbers)) == 1 and numbers[0] == 0:
        return '0'
    def fill_number(number, length):
        # 자릿수 변경하는 함수
        filled_number = ''
        while True:
            filled_number += number
            if len(filled_number) > length:
                break
        return filled_number[:length]

    max_length = len('1000')
    # filled_numbers = [[ 자릿수 변경 후 숫자, 자릿 수 변경 전 숫자], ... ]
    filled_numbers = [[int(fill_number(str(n), max_length)), n] for n in numbers]
    filled_numbers = sorted(filled_numbers, reverse=True, key=lambda x: x[0])
    answer = ''.join([str(n[1]) for n in filled_numbers])

    return answer

if __name__ == '__main__':
    print(solution([6, 10, 2]), "6210")
    print(solution([42, 33, 76]), "764233")
    print(solution([4, 40]), "440")
    print(solution([3, 30, 34, 5, 9]), "9534330")
    print(solution([40, 403]), '40403')
    print(solution([0, 0, 0]), '0')
    print(solution([383, 38]), "38383")
    print(solution([838, 83]), "83883")
    print(solution([11, 11]), "1111")
