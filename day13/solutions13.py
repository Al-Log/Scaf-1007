import math
def solution(arr):
    lcm = arr[0]
    for k in arr[1:]:
        lcm = lcm * k // math.gcd(lcm, k)
    return lcm
