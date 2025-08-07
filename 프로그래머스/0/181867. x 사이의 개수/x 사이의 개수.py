def solution(myString):
    answer = []
    sanswer = myString.split("x")
    for i in sanswer:
        answer.append(len(i))
    return answer