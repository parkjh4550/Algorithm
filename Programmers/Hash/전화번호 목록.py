#https://programmers.co.kr/learn/courses/30/lessons/42577
def solution(phone_book):
    answer = True
    phone_book.sort()
    for itr in range(len(phone_book[:-1])):
        if phone_book[itr] == phone_book[itr+1][:len(phone_book[itr])]:
            answer = False
            return answer
    return answer