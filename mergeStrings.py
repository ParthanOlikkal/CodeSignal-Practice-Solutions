"""
Given to strings a = "super" and b = "tower" we have to give a new string such that it takes the number of occurence of the letter is the word is taken.
If it is less then that is added to the new string. if both the occurances are looked at then the lexicographical ordering is taken. Else if both the
occurenece and the letter is both the same then the first string is taken
eg: a = super
    b = tower
    o/p : stuoperwer

"""

def mergeStrings(a,b):
    s = ""
    i = 0
    j = 0
    while i < len(a) and j < len(b):
        if a.count(a[i]) > b.count(b[j]) or (a.count(a[i]) == b.count(b[j]) and a[i] > b[j]):
            s += b[j]
            j += 1
        else:
            s += a[i]
            i += 1
    print(i,j)
    if i != len(a):
        s += a[i:]
    if j != len(b):
        s += b[j:]
    return s


if __name__ == "__main__":
    a = input()
    b = input()
    print(mergeStrings(a,b))