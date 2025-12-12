import heapq
def lc3433(numberOfUsers,events):
    def parseInt(s):
        return 0 if s=="OFFLINE" else 1
    events.sort(key=lambda x:(int(x[1]),parseInt(x[0])))
    print(events)
    n=numberOfUsers
    scores=[0]*n
    offline=[] ## (id,availableTime)
    offlineSet=set()
    offlineCount=[0]*n
    allCount=0

    for e in events:
        category,time,string=e
        time=int(time)

        if category=="OFFLINE":
            id=int(string)
            heapq.heappush(offline,(time+60,id))
            offlineCount[id]+=1
            offlineSet.add(id)
            continue
        if string=="ALL":
            allCount+=1
            continue
        if string == "HERE":
            ## refresh users status
            while offline and offline[0][0]<=time:
                _,id=heapq.heappop(offline)
                offlineCount[id]-=1
                if offlineCount[id]!=0:continue
                offlineSet.remove(id)
            for i in range(n):
                if i not in offlineSet:
                    scores[i]+=1
            continue

        ## normal ids string
        splitted=string.split()

        for s in splitted:
            id=int(s[2:])
            scores[id]+=1
    
    return [s+allCount for s in scores]


# print(lc3433(2,[["MESSAGE","10","id1 id0"],["OFFLINE","11","0"],["MESSAGE","71","HERE"]]))
print(lc3433(3,[["MESSAGE","1","ALL"],["OFFLINE","66","1"],["MESSAGE","66","HERE"],["OFFLINE","5","1"]]))

         
