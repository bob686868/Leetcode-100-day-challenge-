import heapq
from collections import defaultdict,deque
from math import ceil

## in a max heap , we store the nodes that have till now the highest proba 
## we can use a greedy approach where we always choose the path with maximum probability 
def pathWithHighestProbaDjisktras(edges,succProb,start,end):
    maxHeap=[]
    adj={}

    for i,(src,dst) in enumerate(edges):
        adj[dst].append((src,succProb[i]))
        adj[src].append((dst,succProb[i]))

    visit=set()
    heapq.heappush(maxHeap,(start,-1))
    while maxHeap:
        node,curCost=heapq.heappop(maxHeap)
        if node==end:return curCost*-1
        visit.add(node)

        for nei,cost in adj[node]:
            if node not in visit:
                heapq.heappush((nei,curCost*cost))
        
    return 0

## we can think of the problem as num of passengers arriving at a node , and we 
## calculate required vehicles 
def minFuelCost(roads,seats):
    adj=defaultdict(list)
    numPassengers=0
    result=0
    visit=set()
    visit.add(0)
    for src,dst in roads:
        adj[src].append(dst)
        adj[dst].append(src)

    def numPassengers(node):
        nonlocal numPassengers
        nonlocal result
        for nei in adj[node]:
            if nei not in visit:
                numPassengers+=1+numPassengers(nei)
                visit.add(nei)

        result+=ceil(numPassengers/seats)
        return numPassengers
    
    numPassengers(0)
    return result

## instead of computing distance from nearest land for every cell , we can 
## do a mutli-source bfs from every cell that is a land 
def minDistance(grid):
    n=len(grid)
    q=deque()
    visit=set()
    directions=[(0,1),(0,-1),(1,0),(-1,0)]
    for i in range(n):
        for j in range(n):
            if grid[i][j]==1:
                q.append((i,j,0))
                visit.add((i,j))
    
    res=0
    while len(visit)<n**2:
        x,y,cost=q.popleft()
        res=cost
        for dx,dy in directions:
            newX,newY=x+dx,y+dy
            if (max(newX,newY)<n and min(newX,newY)>=0 and (newX,newY) not in visit):
                visit.add((newX,newY))
                q.append((newX,newY,cost+1))
                res=cost+1
                if len(visit)==n**2:
                    break
    return res

# print(minDistance([[1,0,1],[0,0,0],[1,0,1]]))
# print(minDistance([[1,0,0],[0,0,0],[0,0,0]]))

## instead of storing the average which requires division operation 
## which is expensive , we will store the required minimum target equal to k * threshold
## initialize a window with size k and increment result when exceeding target 
def numSubarraysOfSizeKAndAvGreaterThenThreshold(nums,k,threshold):

    windowSum=0
    target=k*threshold
    result=0
    for i in range(k):
        windowSum+=nums[i]

    if windowSum >= target:
        result+=1

    for i in range(k,len(nums)):
        windowSum-=nums[i-k]
        windowSum+=nums[i]
        if windowSum>=target:
            result+=1
    return result 

print(numSubarraysOfSizeKAndAvGreaterThenThreshold([2,2,2,2,5,5,5,8],3,4))
print(numSubarraysOfSizeKAndAvGreaterThenThreshold([11,13,17,23,29,31,7,5,2,3],3,5))

def deleteNode(root, key):
        def nodeSearcher(node):
            if not node : return None
            if node.val==key:
                if node.right:
                    successor=getSuccessor(node)
                    node.val=successor
                else:
                    return node.left
            elif node.val>key:node.left=nodeSearcher(node.left) 
            else : node.right = nodeSearcher(node.right) 
            return node
            
        def getSuccessor(node):
            cur=node.right
            prev=node
            while cur.left:
                prev=cur                
                cur=cur.left
            if prev != node :prev.left=prev.left.right
            else:prev.right=prev.right.right
            return cur.val 
        
        newRoot=nodeSearcher(root)
        return newRoot 