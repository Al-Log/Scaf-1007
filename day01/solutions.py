def solution(s):
    a=s.split()
    b=[int(b) for b in a]
    answer = f'{min(b)} {max(b)}'            
    return answer
