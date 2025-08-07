def solution(a, b):
    dayy = ["THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED"]
    day = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = sum(day[:a-1])
    days += b
    days %= 7
    answer = dayy[days]
    return answer