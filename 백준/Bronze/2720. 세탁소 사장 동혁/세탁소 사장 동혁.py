case = int(input())

def mm(money):
    a = money // 25
    money %= 25
    b = money // 10
    money %= 10
    c = money // 5
    money %= 5
    d = money // 1
    return int(a), int(b), int(c), int(d)

for i in range(case):
    money = float(input())
    a, b, c, d = mm(money)
    
    print(f"{a} {b} {c} {d}")