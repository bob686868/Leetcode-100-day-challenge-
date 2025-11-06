def cutIntoSections(n,rectangles):

    ## 1- try horizontal cuts
    horizontalEnds=[(rectangles[i][1],rectangles[i][3]) for i in range(len(rectangles))]
    horizontalEnds.sort()
    curEnd=horizontalEnds[0][1]
    numSections=1

    for i in range(1,len(horizontalEnds)):
        start,end=horizontalEnds[i]
        if start>=curEnd:
            numSections+=1
            curEnd=end
            if numSections==3:
                return True
        else:
            curEnd=max(curEnd,end)

    ## try vertical cuts
    verticalEnds=[(rectangles[i][0],rectangles[i][2]) for i in range(len(rectangles))]
    verticalEnds.sort()
    curEnd=verticalEnds[0][1]
    numSections=1

    for i in range(1,len(verticalEnds)):
        start,end=verticalEnds[i]
        if start>=curEnd:
            numSections+=1
            curEnd=end
            if numSections==3:
                return True
        else:
            curEnd=max(curEnd,end)
    return False

# print(cutIntoSections(5,[[1,0,5,2],[0,2,2,4],[3,2,5,3],[0,4,4,5]]))
# print(cutIntoSections(4,[[0,0,1,1],[2,0,3,4],[0,2,2,3],[3,0,4,3]]))

import heapq
from collections import defaultdict
def numberOfWayToArriveAtDestination(n,roads):
    adj=defaultdict(list)
    for src,dst,w in roads:
        adj[src].append((dst,w))
        adj[dst].append((src,w))
    minCost=float('inf')
    minHeap=[(0,0)] ## (curCost,curNode)
    best=[float('inf')]*n
    numWays=[1]*n
    best[0]=0

    while minHeap:
        curCost,curNode=heapq.heappop(minHeap)
        if curCost>minCost:
            break
    
        if curNode==n-1:
            minCost=curCost
        
        for nei,w in adj[curNode]:
            newCost=curCost+w
            if newCost==best[nei]:
                numWays[nei]+=numWays[curNode]
            elif newCost<best[nei]:
                best[nei]=newCost
                numWays[nei]=numWays[curNode]
                heapq.heappush(minHeap,(newCost,nei))
    return numWays[n-1]

# print(numberOfWayToArriveAtDestination(7,[[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]))
# print(numberOfWayToArriveAtDestination(2,[[1,0,10]]))

def minOpsToMakeUniValued(grid,x):
    sortedArr=[]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            sortedArr.append(grid[i][j])
    
    sortedArr.sort()
    res=0
    target=sortedArr[len(sortedArr)//2]
    for n in sortedArr:
        diff=abs(target-n)
        if diff%x:
            return -1
        res+=diff//x
    return res

# print(minOpsToMakeUniValued([[2,4],[6,8]],2))
# print(minOpsToMakeUniValued([[1,5],[2,3]],1))

import math
# def minIndexOfAValidSplit(nums):
#     dominantNum,count=0,0
#     ## determine dominant element
#     for n in nums:
#         if n != dominantNum:
#             count-=1
#             if count<0:
#                 dominantNum=n
#                 count=1
#         else:count+=1
    
#     ## sliding window : look for the first window where the dominant num 
#     ## is also dominant in that left portion 
#     ## the first solution for will guarantee us that the same dominant num is also 
#     ## dominant in the right portion (since there is only one dominant element)

#     countLeft=0
#     print(dominantNum)
#     for i in range(len(nums)):
#         countLeft+=(nums[i]==dominantNum)
#         print(countLeft)
#         if countLeft>math.floor((i+1)/2):
#             return i
    
#     return -1

from collections import Counter
from sortedcontainers import SortedList
def minIndexOfAValidSplit(nums):
    dominantNum,count=0,0
    ## determine dominant element
    for n in nums:
        if n != dominantNum:
            count-=1
            if count<0:
                dominantNum=n
                count=1
        else:count+=1
    
    countLeft=defaultdict(int)
    countRight=defaultdict(int)
    for n in nums:
        if n==dominantNum:
            countRight[n]+=1

    for i in range(len(nums)):
        n=nums[i]
        if n==dominantNum:
            countLeft[n]+=1
            countRight[n]-=1
        if countLeft[n]>(i+1)//2 and countRight[n]>(len(nums)-1-i)//2:
            return i
    return -1

# print(minIndexOfAValidSplit([2,1,3,1,1,1,7,1,2,1]))

def maxNumOfPtsFromQueries(grid,queries):
    ## map each query to its orginal index
    queryToIndex=defaultdict(list)
    for i,q in enumerate(queries):
        queryToIndex[q].append(i)
    queries.sort()
    minHeap=[(grid[0][0],0,0)] ## (value,r,c)
    curScore=0
    result=[0]*len(queries)
    visit={(0,0)}
    dirs=[(0,1),(1,0),(0,-1),(-1,0)]


    for q in queries:
        while minHeap:
            val,x,y=heapq.heappop(minHeap)
            if val>=q:
                heapq.heappush(minHeap,(val,x,y))
                break
            curScore+=1
            for dx,dy in dirs:
                newX,newY=x+dx,y+dy
                if not (0<=newX<=len(grid)-1) or not (0<=newY<=len(grid[0])-1):continue                
                if (newX,newY) not in visit:
                    visit.add((newX,newY))
                    heapq.heappush(minHeap,(grid[newX][newY],newX,newY))

        result[queryToIndex[q][-1]]=curScore
        queryToIndex[q].pop()

    return result

# print(maxNumOfPtsFromQueries([[1,2,3],[2,5,7],[3,5,1]],[5,6,2]))
# print(maxNumOfPtsFromQueries([[5,2,1],[1,1,2]],[3]))

def partitionLabels(s):
    lastCount=defaultdict(int)
    for i,c in enumerate(s):
        lastCount[c]=i
    i=0
    result=[]
    while i < len(s):
        start=i
        shiftTo=lastCount[s[i]]
        while i<=shiftTo:
            shiftTo=max(shiftTo,lastCount[s[i]])
            i+=1
        if i==start:break
        result.append((i-start))  
    return result

# print(partitionLabels("ababcbacadefegdehijhklij"))  
# print(partitionLabels("eccbbbbdec"))  

def powerGridMaintenance(c,connections, queries):
    class UnionFind:
        def __init__(self):
            self.parent=[-1]
            self.rank=[0 for _ in range(c+1)]
            self.minEls=[SortedList([i]) for i in range(c+1)]
            for i in range(c):
                self.parent.append(i+1)

        def find(self,n):
            parent=self.parent
            while n!=parent[n]:
                n=parent[n]
                parent[n]=parent[parent[n]]

            return n
        
        def union(self,n1,n2):
            parent,rank,minEls=self.parent,self.rank,self.minEls
            p1,p2=self.find(n1),self.find(n2)

            if p1==p2:return False
            elif rank[p1]>rank[p2]:
                parent[p2]=p1
                rank[p1]+=1
                minEls[p1].update(minEls[p2])  ## add every element of the first sortedList to the second one 
                minEls[p2].clear()
            else :
                parent[p1]=p2
                rank[p2]+=1
                minEls[p2].update(minEls[p1])  ## add every element of the first sortedList to the second one 
                minEls[p1].clear()
            return True
        def disable(self,n1):
            p1=self.find(n1)
            self.minEls[p1].remove(n1)

    uf=UnionFind()
    for src,dst in connections:
        uf.union(src,dst)

    disabled=[False]*(c+1)
    result=[]
    for qn,q in queries:
        if qn==2:
            if disabled[q]:continue
            disabled[q]=True
            uf.disable(q)
        else:
            if not disabled[q]:
                result.append(q)
                continue
            p=uf.find(q)
            minElArr=uf.minEls[p]
            if not minElArr:
                result.append(-1)
                continue
            minEl=minElArr[0]
            result.append(minEl)
    return result

# print(powerGridMaintenance(5,[[1,2],[2,3],[3,4],[4,5]],[[1,3],[2,1],[1,1],[2,2],[1,2]]))
# print(powerGridMaintenance(3,[],[[1,1],[2,1],[1,1]]))

