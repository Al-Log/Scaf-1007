def solution(s):
    sum=0
    if s.startswith('(') and s.endswith(')'):
        for k in s:
            if k=='(':
                sum+=1
            elif k==')':
                sum-=1
            if sum<0:
                answer = False
                return answer
        if sum==0:
            answer = True
            return answer
        else:
            answer = False
            return answer
    else:
        answer = False
        return answer
