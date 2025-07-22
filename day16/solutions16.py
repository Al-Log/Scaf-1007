import math
def solution(n, a, b):
    g = 0
    for i in range(int(math.log2(n))):
        g += 1
        a = (a + 1) // 2
        b = (b + 1) // 2
        if a == b:
                return g
