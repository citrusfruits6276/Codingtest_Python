def solution(numbers):
    my_set = set()
    for i in range(len(numbers)):
        for d in range(i + 1, len(numbers)):
            my_set.add(numbers[i] + numbers[d])
    sorted_list = sorted(list(my_set))
    
    return sorted_list