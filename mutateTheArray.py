"""
Given an array, create another array such that b[1] = arr[0] + arr[1] + arr[2]. If there are no usable elements, put them as 0

eg: [4,0,5,-2,1]
    o/p : [4,9,3,4,-1]

"""

def mutateTheArray(arr):
    temp = arr
    temp.insert(0,0)
    temp.insert(len(arr),0)
    #print(temp)
    b = [0 for i in range(len(temp)-2)]

    for i in range(len(temp)-2):
        b[i] += temp[i] + temp[i+1] + temp[i+2]

    #print(b)
    return b

if __name__ == "__main__":
    arr = list(map(int,input().split()))
    print(mutateTheArray(arr))