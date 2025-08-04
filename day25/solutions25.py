from itertools import permutations
def solution(k, dungeons):
    answer=0
    for i in permutations(dungeons,len(dungeons)):
        ck=k
        c=0
        for d in i:
            a,b=d
            if ck>=a:
                ck-=b
                c+=1
            else:
                break
        answer=max(answer,c)
    return answer
