def solution(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    a,b=0,1
    for k in range(2,n+1):
        a,b=b,a+b
    answer=b%1234567
    return answer
