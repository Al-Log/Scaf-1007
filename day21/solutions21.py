from collections import Counter
def solution(topping):
    answer=0
    a=Counter(topping)
    b=set()
    for k in topping:
        a[k]-=1
        if a[k]==0:
            del a[k]
        b.add(k)
        if len(a)==len(b):
            answer+=1
    return answer
