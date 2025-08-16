def solution(i, j, k):
    answer = 0
    for m in range(i, j+1):
            answer += str(m).count(str(k))
    return answer