def solution(s):
    s.lower()
    b=s.split(' ')
    c=[]
    for k in b:
        c.append(k.capitalize())
    answer=' '.join(c)
    return answer
