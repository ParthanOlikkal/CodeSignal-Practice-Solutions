"""
Given an array, index a starts from left and index b starts right to left of the array, our aim is to find the number of
 int(str(a) + str(b)) < k where k is given

 eg; [1,2,3], k = 31
            = 13, 22, 31
            = 2
"""

def countTinyPairs(arr, k):
    i = 0
    j = len(arr)-1
    total = []
    while i < len(arr):
        if int(str(arr[i]) + str(arr[j])) < k:
            total.append(1)
        else:
            total.append(0)
        i += 1
        j -= 1

    #print(total)
    return sum(total)

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    k = int(input())
    print(countTinyPairs(arr,k))