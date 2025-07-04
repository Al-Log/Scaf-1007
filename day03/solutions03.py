def solution(A,B):
    A.sort()
    B.sort(reverse=True)
    sum=0
    for k in range(len(A)):
        sum=sum+A[k]*B[k]
        answer=sum
    return answer
