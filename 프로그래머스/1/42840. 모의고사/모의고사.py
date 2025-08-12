def solution(answers):
    scores = [0] * 3
    nodap = [
    [1, 2, 3, 4, 5],
    [2, 1, 2, 3, 2, 4, 2, 5],
    [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]
    result = []
    
    for i, answer in enumerate(answers):
        for j, nod in enumerate(nodap):
            if answer == nod[i % len(nod)]:
                scores[j] += 1
    max_scores = max(scores)
    
    for i, score in enumerate(scores):
        if score == max_scores:
            result.append(i+1)
    
    return result