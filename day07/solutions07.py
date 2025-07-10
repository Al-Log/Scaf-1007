def solution(s):
    answer=[]
    a=0
    b=0

    while s!='1':
        c=s.count('0')
        b+=c
        s=s.replace('0','')
        s=bin(len(s))[2:]
        a+=1

    answer.append(a)
    answer.append(b)
    return answer
