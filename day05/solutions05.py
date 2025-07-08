def solution(n):
    answer=1
    h=[]
    if n==1 or n==2:
            return answer
    else:
        for k in range(1,(n//2)+2):
            h.append(k)
            if sum(h)>n:    
                while sum(h)>n:
                    h.pop(0)
            if sum(h)==n:
                answer+=1
    return answer
