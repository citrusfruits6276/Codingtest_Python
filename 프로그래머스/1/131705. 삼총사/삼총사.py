def solution(number):
    answer = 0
    length = len(number)
    number = sorted(number)
    for i in range(length - 2):
        for m in range(i + 1, length - 1):
            for j in range(m + 1, length):
                if number[i]+number[m]+number[j] == 0:
                    answer += 1
    
    return answer