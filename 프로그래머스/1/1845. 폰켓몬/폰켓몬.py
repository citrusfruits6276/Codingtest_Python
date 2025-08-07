def solution(nums):
    t = set(sorted(nums))
    if len(t) < len(nums)//2:
        answer = len(t)
    else:
        answer = len(nums)//2
    return answer