def lc944(strs):
    deleted=0
    for i in range(len(strs[0])):
        for j in range(1,len(strs)):
            if ord(strs[j][i])<ord(strs[j-1][i]):
                deleted+=1
                break
    return deleted

# print(lc944(["cba","daf","ghi"]))
# print(lc944(["a","b"]))

def lc2092(n,meetings,firstPerson):
        meetings.sort(key=lambda m:m[2])
        persons={0,firstPerson}
        curTimeHashMap={}
        prevTime=-1

        def propagate(x):
            persons.add(x)
            visit.add(x)
            if x not in curTimeHashMap :return 
            for nei in curTimeHashMap[x]:
                if nei not in visit:
                    propagate(nei)

        for x,y,time in meetings:
            if time!=prevTime:
                visit=set()
                for p in curTimeHashMap:
                    if p not in persons:continue
                    propagate(p)
                curTimeHashMap.clear()
            if x in persons or y in persons:
                persons.update([x,y])
            if x not in curTimeHashMap:
                curTimeHashMap[x]=[]
            if y not in curTimeHashMap:
                curTimeHashMap[y]=[]
            curTimeHashMap[x].append(y)
            curTimeHashMap[y].append(x)
            prevTime=time
        visit=set()
        for p in curTimeHashMap:
            if p not in persons:continue
            propagate(p)
        return list(persons)

# print(lc2092(6,[[1,2,5],[2,3,8],[1,5,10]],1))
# print(lc2092(4,[[3,1,3],[1,2,2],[0,3,3]],3))
# print(lc2092(5,[[3,4,2],[1,2,1],[2,3,1]],1))

def lc3652(prices,strategy,k):
    curProfit=0

    ## intialize first window
    for i in range(k//2,k):
        curProfit+=prices[i]
    for i in range(k,len(prices)):
        curProfit+=prices[i]*strategy[i]

    ## original
    original=0
    for i in range(len(prices)):
        original+=prices[i]*strategy[i]
    res=max(original,curProfit)

    ## slide the window
    for i in range(k,len(prices)):
        curProfit+=strategy[i-k]*prices[i-k]

        curProfit-=prices[i-k//2]

        curProfit-=strategy[i]*prices[i]
        curProfit+=prices[i]
        print(curProfit)
        res=max(res,curProfit)

    return res

# print(lc3652([4,2,8],[-1,0,1],2))
# print(lc3652([5,4,3],[1,1,0],2))
# print(lc3652([4,7,13],[-1,-1,0],2))

        
