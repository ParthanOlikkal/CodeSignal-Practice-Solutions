# eg: [10,2]
"""
[10,2]  = 1010 + 102 + 210 + 22
        = (10*10**2 + 10)+ (10*10**1 + 2) + (2*10**2 + 10) + (2 * 10**1 + 2)
        = (10 + 2) + (10 *(10**2 + 10**1)) + (10 + 2) + (2*(10**2 + 10**1))
        = sum(arr) * len(arr) + [el* sum of tens to the power of len of each element for el in arr]
"""

def concatentationsSum(arr):
    sumofPowers = sum([10**len(str(el)) for el in arr])
    return sum([el * sumofPowers for el in arr]) + (sum(arr) * len(arr))


if __name__ == "__main__":
    arr = list(map(int,input().split()))
    total = concatentationsSum(arr)
    print(total)