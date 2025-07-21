def solution(n, words):
    answer = []
    a=[]
    a.append(words[0])
    for k in words[1:]:
        a.append(k)
        if a.count(k)==2 or a[-2][-1]!=k[0]:
            b=len(a)%n
            if b==0:
                b=n
            c=len(a)//n
            if len(a)%n!=0:
                c+=1
            break
        else:
            b=0
            c=0
    answer.append(b)
    answer.append(c)
    return answer
