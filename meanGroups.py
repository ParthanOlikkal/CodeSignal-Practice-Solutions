"""
Given an array which has a group of arrays. Each array of the main array has elements. We have to find the mean of those
array and the indices of the array that as the same mean should be grouped together.

eg: [[0,0,0],[3,3,3],[-1,0,1],[2,4,6]]
    o/p : [[0,2],[1],[3]]
"""

def meanGroup(arr):
    m = []
    for a in arr:
        m.append(mean(a))
    #print(m)

    dic = {}
    for i,v in enumerate(m):
        if v in dic:
            dic[v].append(i)
        else:
            dic[v] = [i]

    #print(dic)

    ans = []
    for k,v in dic.items():
        ans.append(dic[k])

    return ans

def mean(arr):
    return sum(arr)/len(arr)


if __name__ == "__main__":
    n = int(input())
    arr = []
    for i in range(n):
        val = list(map(int,input().split()))
        arr.append(val)

    result = meanGroup(arr)
    print(result)
