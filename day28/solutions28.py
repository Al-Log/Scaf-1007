from collections import deque
def solution(cacheSize, cities):
    answer = 0
    cache=deque()
    if not cacheSize:
        return len(cities)*5
    for k in cities:
        k=k.lower()
        if k in cache:
            answer+=1
            cache.remove(k)
            cache.append(k)
        else:
            answer+=5
            if len(cache)>=cacheSize:
                cache.popleft()
                cache.append(k)
            else:
                cache.append(k)
    return answer
