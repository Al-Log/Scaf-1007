def solution(elements):
    answer = []
    circle=elements*2
    for i,k in enumerate(elements):
        answer.append(k)
        for a in circle[i+1:i+len(elements)]:
            k+=a
            answer.append(k)
    return len(set(answer))
