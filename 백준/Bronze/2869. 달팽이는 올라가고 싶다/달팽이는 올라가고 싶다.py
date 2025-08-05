a, b, v = map(int, input().split())

up = v - b
climb = a - b
day = up // climb
if up % climb != 0:
    day += 1

print(day)
    