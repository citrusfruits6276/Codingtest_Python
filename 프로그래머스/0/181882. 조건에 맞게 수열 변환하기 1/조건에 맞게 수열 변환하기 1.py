def solution(arr):
    arry = []
    for i in arr:
        number = arr.index(i)
        if i >= 50 and i % 2 == 0:
            i /= 2
            arry.append(i)
        elif i < 50 and i % 2 == 1:
            i *= 2
            arry.append(i)
        else:
            arry.append(i)
    return arry