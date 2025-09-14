
## to efficiently convey that an element appears in our array , we will
## mark number n at index i as visited by making nums[i] negative
## but , as you can tell , the array can contain elements that are already
## negative so we will make them a big integer that we will never mark (aka len(nums)+1)
## Finally , after the marking phase , we can now just loop over array and return first postive 
## element index or len(nums)+1 otherwise   
def firstMissingPositive(nums):
    for i in range(len(nums)):
        if nums[i]<=0:
            nums[i]=len(nums)+1

    for i in range(len(nums)):
        if abs(nums[i])<len(nums)+1:
            if nums[abs(nums[i])-1]>0:
                nums[abs(nums[i])-1]*=-1
    for i in range(len(nums)):
        if nums[i]>0:
            return i+1
    return len(nums)+1

# print(firstMissingPositive([1,2,0]))
# print(firstMissingPositive([3,4,-1,1]))
# print(firstMissingPositive([7,8,9,11,12]))

from collections import defaultdict,deque
import heapq

## find the nodes that have number of nodes equal to the 
## second maximum and look for any pair of disjoined indices
## if we dont find any disjoint pair , we return their sum-1 

def largestRoadRank(n,edges):
    adj=defaultdict(set)

    for src,dst in edges:
        adj[src].add(dst)
        adj[dst].add(src)
    
    maxHeap=[]
    for k,v in adj.items():
        heapq.heappush(maxHeap,(-1*len(v),k))

    val1,key1=heapq.heappop(maxHeap)
    val2,key2=heapq.heappop(maxHeap)

    val1*=-1
    val2*=-1

    if key2 not in adj[key1]:
        return val1+val2
    while len(maxHeap) and maxHeap[0][0]*-1==val2:
        tmpval,tmpkey=heapq.heappop(maxHeap)
        tmpval*=-1
        if tmpkey not in adj[key1] and tmpval not in adj[key2]:
            return val1+val2
    return val1+val2-1


    
# print(largestRoadRank(4,[[0,1],[0,3],[1,2],[1,3]]))
# print(largestRoadRank(5,[[0,1],[0,3],[1,2],[1,3],[2,3],[2,4]]))
# print(largestRoadRank(8,[[0,1],[1,2],[2,3],[2,4],[5,6],[5,7]]))

## to find number of lands that cannot reach the border via other land cells , 
## we can do a dfs from the border nodes and return the number of land cells 
## that were unreached 

def numOfEnclaves(grid):
    visit=set()
    land=0
    directions=[(0,1),(1,0),(-1,0),(0,-1)]
    def inbounds(x,y):
        return 0<=x<=len(grid)-1 and 0<=y<=len(grid[0])-1
    def dfs(x,y):
        nonlocal land 
        land-=1
        for dx,dy in directions:
            newX,newY=x+dx,y+dy
            if not inbounds(newX,newY) or grid[newX][newY]!=1:
                continue
            if (newX,newY) not in visit:
                visit.add((newX,newY))
                dfs(newX,newY)
        
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]==1:
                land+=1
                if ((i,j) not in visit) and (i==0 or i==len(grid)-1 or j==0 or j==len(grid[0])-1):
                    visit.add((i,j))
                    dfs(i,j)
    return land
    
# print(numOfEnclaves([[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]))
# print(numOfEnclaves([[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]))

from math import ceil

## we can minimize the sum by "splitting" the sum of the current subarray
## equally between the elements , looping in forward direction since we cannot
## split nums backward
def minimizeMaximum(nums):
    maxVal=nums[0]
    curSum=nums[0]
    for i in range(1,len(nums)):
        curSum+=nums[i]
        maxVal=max(maxVal,ceil(curSum/(i+1)))
    return maxVal

print(minimizeMaximum([3,7,1,6]))
print(minimizeMaximum([10,1]))