def solution(s, skip, index):
    alpha_set = set(skip)
    alpha_dic = [
        chr(i) for i in range(ord("a"), ord("z")+1) if chr(i) not in alpha_set
        ]
    result = ""
    for i in s:
        current_index = alpha_dic.index(i)
        new = (current_index + index) % len(alpha_dic)
        result += alpha_dic[new]
    return result

        