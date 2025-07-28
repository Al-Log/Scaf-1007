from collections import Counter
def solution(clothes):
    c=Counter([a for _, a in clothes ])
    answer=1
    for k in c.values():
        answer*=(k+1)
    return answer-1
