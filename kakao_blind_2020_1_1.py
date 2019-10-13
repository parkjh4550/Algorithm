#https://tech.kakao.com/2019/10/02/kakao-blind-recruitment-2020-round1/


#1.  problem

def solution(data):
    result = ''
    data_len = len(data)
    max_len = len(data)/2

    for itr in range(max_len):
        slice_len = max_len - itr
        c_index = 0
        tmp = data[:]
        tmp_dict ={}
        while c_index <= (len(tmp)-slice_len):
            sliced = data[c_index:c_index+slice_len]

            find = tmp.find(sliced)
            if find:
                if sliced in tmp_dict:
                    tmp_dict[sliced]


    return result


if __name__ == '__main__':

    test_sample = ['aabbaccc', 'ababcdcdababcdcd', 'abcabcdede', 'abcabcabcabcdededededede', 'xababcdcdababcdcd']

    for sample in test_sample:
        print(solution(sample))