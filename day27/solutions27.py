def solution(s):
    answer = []
    a_set = set()
    
    s1 = s.replace('{{','').replace('}}','').split('},{')
    s1.sort(key=lambda x : len(x))

    for i in s1:
        for j in i.split(','):
            j = int(j)
            if j not in a_set:
                a_set.add(j)
                answer.append(int(j))
    return answer
