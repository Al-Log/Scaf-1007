def solution(s):
    answer = 0
    a=[]
    for k in s:
        if a and a[-1]==k:
            a.pop()
        else:
            a.append(k)
    if len(a)==0:
        answer=1
    return answer
