def solution(arr1, arr2):
    answer=[]
    for k in range(len(arr1)):
        a=[]
        for i in range(len(arr2[0])):
            b=sum(arr1[k][j]*arr2[j][i] for j in range(len(arr2)))
            a.append(b)
        answer.append(a)
    return answer
