def solution(progresses, speeds):
    answer=[]
    a=list(progresses)
    b=list(speeds)
    c=[]
    d=0
    for k in range(len(a)):
        while a[k]<100:
            a[k]+=b[k]
            d+=1
        c.append(d)
        d=0
    e=c[0]
    f=1
    for i in c[1:]:
        if i <= e:
            f+=1
        else:
            answer.append(f)
            f=1
            e = i
    answer.append(f)
    return answer
