def solution(sides):
    a = max(sides)
    b = min(sides)
    c = a + b - 1
    d = c - a
    return d + b