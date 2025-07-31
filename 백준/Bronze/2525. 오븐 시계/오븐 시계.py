a, b = map(int, input().split())
c = int(input())

time = (a * 60) + b + c
h = time // 60 % 24
m = time % 60

print(h, m)