"""
We are developing a custom Hashmap that has 4 functions, insert, addToValue, addToKey and get.
    insert x y : inserts x to the hashmap with x as the key and y as the value
    addToValue x : adds x to all the values in the hashmap
    addToKey x : adds x to all the keys in the hashmap
    get x : returns the value of the key x in the hashmap

Our aim is to find the total sum of all the get's in the hashmap
"""

def customHashMap(queryType, query):
    dic = {}
    ele = []
    ans = 0

    for q in range(len(queryType)):
        if queryType[q] == 'insert':
            dic[query[q][0]] = query[q][1]
            ele.append(query[q][0])

        elif queryType[q] == "addToValue":
            val = query[q][0]
            for k,v in dic.items():
                dic[k] += val

        elif queryType[q] == "addToKey":
            key = query[q][0]
            new_dic ={}
            val = []
            ele = [e + key for e in ele]
            for i,v in dic.items():
                val.append(dic[i])
            for i,v in zip(ele,val):
                dic[i] = v

        elif queryType[q] == "get":
            ans += dic[query[q][0]]

    #print(ans, dic, ele)
    return ans

if __name__ == "__main__":

    queryType = []
    query = []
    q = int(input())
    for i in range(q):
        qu = input()
        queryType.append(qu)
    for i in range(q):
        qy = list(map(int,input().split()))
        query.append(qy)

    #print(queryType)
    #print(query)
    print(customHashMap(queryType,query))
