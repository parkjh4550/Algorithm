#https://programmers.co.kr/learn/courses/30/lessons/12904?language=python3#

def solution(s):
    answer = []
    if not s: return 0
    if len(s) == 1: return 1
    if len(s) == 2:
        if s[0] != s[1]:
            return 1
        else:
            return 2

    # 1. 각 문자 별로 탐색.
    for itr in range(1, len(s) - 1):
        left, right = itr - 1, itr + 1

        candidate = 1
        # 2. 홀수 팬린드롭
        while left >= 0 and right < len(s):
            if s[left] == s[right]:  # 팬린드롭일 경우
                candidate += 2
                left -= 1
                right += 1
            else:
                break  # 팬린드롭이 아닐 경우

        answer.append(candidate)


        # 3. 짝수 팬린드롭
        left, right = itr - 1, itr + 1
        candidate = 1
        if s[right] == s[itr]:
            candidate += 1
            right += 1
        while left >= 0 and right < len(s):
            if s[left] == s[right]:  # 팬린드롭일 경우
                candidate += 2
                left -= 1
                right += 1
            else:
                break  # 팬린드롭이 아닐 경우

        answer.append(candidate)
    return max(answer)

print(solution("abcdcba"))      #좌우대칭
print(solution("abacde"))       # 문자열 내의 팰린드롭
print(solution("abccba"))       # 좌우 대칭
print(solution("abbbb"))        #짝수 펠린드롭
print(solution(""))             # 문자열 없는 경우
print(solution("ab"))           # 2개 문자열