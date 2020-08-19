"""

given an arr, create another array, b such that the elements are in the order:
b[0] = a[0]
b[1] = a[len(a)-1]
b[2] = a[1]
b[3] = a[len(a)-2]
....

Aim is to find out if the elements in the array b is striclty ascending order

eg: a = [1,3,5,6,4,2]
    b = [1,2,3,4,5,6]
    o/p = True
"""

def alternatingSort(arr):
    b = [0 for i in range(len(arr))]
    i = 0
    j = len(arr)-1
    k = 0

    while i < len(arr)//2:
        b[k] = arr[i]
        b[k+1] = arr[j]
        j -= 1
        i += 1
        k += 2

    if len(arr) % 2 != 0 and b[-1] == 0:
        b[-1] = arr[i]

    #print(b)
    diff = [0 for i in range(len(b)-1)]
    for i in range(1,len(b)):
        d = b[i-1]-b[i]
        diff[i-1] = d

    #print(diff)

    for d in diff:
        if d >= 0:
            return False
    return True


if __name__ == "__main__":
    arr = list(map(int,input().split()))
    print(alternatingSort(arr))