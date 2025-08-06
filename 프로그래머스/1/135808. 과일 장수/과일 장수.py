def solution(k, m, score):
    score.sort(reverse = True)
    answer = 0
    for i in range(0, len(score) - m + 1, m):
        box = score[i:i+m]
        answer += min(box) * m
    return answer