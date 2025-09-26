## classical dp problem :
## - we store the following state : (row , position1,position2)
## - the small caveat is that when position1 == position2 we give the profit for one robot only
def cherryPickup2(grid):
    r,c=len(grid),len(grid[0])
    dp=[[[-1]*c for _ in range(c)]for _ in range(r)]
    def dfs(i,j1,j2):
        if i==r:return 0
        if dp[i][j1][j2]!=-1:return dp[i][j1][j2]
        for d1 in range(-1,2):
            for d2 in range(-1,2): 
                if not j1+d1<c or not j2+d2<c or not min(j1+d1,j2+d2)>=0 :
                    continue
                rowScore=(grid[i][j1]+grid[i][j2]) if (j1!=j2) else grid[i][j1] 
                dp[i][j1][j2]=max(dp[i][j1][j2],rowScore+dfs(i+1,d1+j1,d2+j2))
        return dp[i][j1][j2]

    return dfs(0,0,c-1)

# print(cherryPickup2([[3,1,1],[2,5,1],[1,5,5],[2,1,1]]))
# print(cherryPickup2([[4,1,5,7,1],[6,0,4,6,4],[0,9,6,3,5]]))

import heapq

## greedy algo : to get the best result , we should 
## shoot the arrow at the end of the ballon range 
## So , it is convenient to sort by smaller end value so that we can always pick
## the ballon that has the lowest end and thus cannot be skipped since later ballons wont consider it 
def minimumNumberOfArrowsToPopBallons(ballons):
    sortedBallons=[(x2,x1) for x1,x2 in ballons] ## sort from smallest to largest xEnd then xStart
    heapq.heapify(sortedBallons)

    result=0
    while sortedBallons:
        result+=1
        xEnd,_=heapq.heappop(sortedBallons)
        while sortedBallons:
            x2,x1=heapq.heappop(sortedBallons)
            if not xEnd>=x1:
                heapq.heappush(sortedBallons,(x2,x1))
                break
    return result

# print(minimumNumberOfArrowsToPopBallons([[10,16],[2,8],[1,6],[7,12]]))
# print(minimumNumberOfArrowsToPopBallons([[1,2],[3,4],[5,6],[7,8]]))

class UnionFind:
    def __init__(self,length):
        self.parent=[i for i in range(length)]
        self.ranks=[1 for _ in range(length)]

    def find(self,i1):
        parent=self.parent
        cur=i1
        while parent[cur]!=cur:
            cur=parent[cur]
            parent[cur]=parent[parent[cur]]
        return cur 
    
    def union(self,n1,n2):
        p1,p2=self.find(n1),self.find(n2)
        if p1==p2:return False
        ranks=self.ranks
        parent=self.parent

        if ranks[p2]>ranks[p1]:
            parent[p1]=p2
            ranks[p2]+=ranks[p1]

        else:
            parent[p2]=p1
            ranks[p1]+=ranks[p2]
        return True

## greedy algo : add the edge with the smallest weight 
## everytime and then check if this edge doesnt create a cycle 
def minCostToConnectAllPoints(points):
    edges=[]
    uf=UnionFind(len(points))
    for i in range(len(points)):
        for j in range(i+1,len(points)):
            x1,y1=points[i]
            x2,y2=points[j]
            edges.append((abs(x2-x1)+abs(y2-y1),i,j))

    heapq.heapify(edges)
    result=0
    unions=0
    while unions<len(points)-1 and edges:
        cost,i,j=heapq.heappop(edges)
        if uf.union(i,j):
            result+=cost
            unions+=1

    return result

# print(minCostToConnectAllPoints([[0,0],[2,2],[3,10],[5,2],[7,0]]))
# print(minCostToConnectAllPoints([[3,12],[-2,5],[-4,1]]))

## greedy algo : start with the elements with capital 0 and place their profits in a maxHeap
## everytime we update our curProfit , we update our available capitals 
## thus , it is convenient to place the capitals in a minHeap with their profits to then add the profits to the maxHeap
       
def ipo(k,w,profits,capital):
    curProfits=w
    picked=0
    minCapital=[(c,p) for p,c in zip(profits,capital)]
    heapq.heapify(minCapital)
    maxProfits=[]
    
    while True:

        ## step 1: add every available element to the profits  
        while minCapital:
            c,p=heapq.heappop(minCapital)
            if c>curProfits:
                heapq.heappush(minCapital,(c,p))
                break
            heapq.heappush(maxProfits,-p)
        
        if not maxProfits or picked==k:
            break

        ## step 2: gain every profit available 
        p=heapq.heappop(maxProfits)
        curProfits-=p  ## p is negative 
        picked+=1


    return curProfits
            
# print(ipo(2,0,[1,2,3],[0,1,1]))       
# print(ipo(3,0,[1,2,3],[0,1,2]))   

from collections import defaultdict
def designUnderGroundSystem():
    class UnderGroundSystem:
        
        def __init__(self):
            self.stationsToTimes=defaultdict(list) ## (startStation,endStation) -> times
            self.checks=defaultdict(int)   ## id : (arrivalTime,stationName)

        def checkIn(self,id,stationName,t):
            self.checks[id]=(t,stationName)

        def checkOut(self,id,stationName,t):
            oldTime,oldStationName=self.checks[id]
            self.stationsToTimes[(oldStationName,stationName)].append(oldTime-t)
        def getAveragetime(self,startStation,endStation):
            return sum(self.stationsToTimes[(startStation,endStation)])/len(self.stationsToTimes[(startStation,endStation)])

def detonateMaxNumOfBombs(bombs):
    def isInBombRadius(x1,y1,r,x2,y2):
        return (x1-x2)**2+(y1-y2)**2<=r**2

    def dfs(x,y,r):
        score=0
        for i in range(len(bombs)):
            x1,y1,r1=bombs[i]
            if i not in detonated and isInBombRadius(x,y,r,x1,y1):
                detonated.add(i)
                score+=1+dfs(x1,y1,r1)   
        return score
    result=1
    for i,(x,y,r) in enumerate(bombs):
        detonated=set()
        detonated.add(i)
        result=max(result,1+dfs(x,y,r))
        detonated.remove(i)
    return result

print(detonateMaxNumOfBombs([[2,1,3],[6,1,4]]))
print(detonateMaxNumOfBombs([[1,1,5],[10,10,5]]))
print(detonateMaxNumOfBombs([[1,2,3],[2,3,1],[3,4,2],[4,5,3],[5,6,4]]))

    


