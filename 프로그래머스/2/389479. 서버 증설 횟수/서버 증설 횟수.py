def solution(players, m, k):
    suver = [0] * 24
    count = 0

    for p in range(len(players)):
        need = players[p] // m
        if need == 0:
            continue
            
        max_current = max(suver[p:p + k])

        if max_current >= need:
            continue

        # 부족한 만큼만 추가
        additional = need - max_current
        count += additional

        # 모든 해당 범위에 해당 서버 수 만큼 반영
        for i in range(p, p + k):
            if i < 24:
                suver[i] += additional

    print(suver)
    return count
