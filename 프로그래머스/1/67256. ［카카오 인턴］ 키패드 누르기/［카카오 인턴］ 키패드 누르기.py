phone = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ["*", 0, "#"]]

def find(i):
    for y in range(4):
        for x in range(3):
            if phone[y][x] == i:
                return x, y

def solution(numbers, hand):
    
    answer = ''
    ly, lx, ry, rx = 3, 0, 3, 2
    
    for i in numbers:
        x, y = find(i)
        if x == 0:
            answer += "L"
            ly = y
            lx = 0
        elif x == 2:
            answer += "R"
            ry = y
            rx = 2
        else:
            if abs(x - lx) + abs(y - ly) > abs(x - rx) + abs(y - ry):
                rx = x
                ry = y
                answer += "R"
            elif abs(x - lx) + abs(y - ly) < abs(x - rx) + abs(y - ry):
                lx = x
                ly = y
                answer += "L"
            elif abs(x - lx) + abs(y - ly) == abs(x - rx) + abs(y - ry):
                if hand == "right":
                    rx = x
                    ry = y
                    answer += "R"
                else:
                    lx = x
                    ly = y
                    answer += "L"
            
    return answer