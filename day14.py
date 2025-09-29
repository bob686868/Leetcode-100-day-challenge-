import heapq
from collections import defaultdict
## main thing to notice is that the effort of a path wont decrease 
## thus the local minimum is the same as global minimum and djiktra is applicable \

def pathWithMinimumEffort(heights):
    def inBounds(x,y):
        return 0<=x<r and 0<=y<c
    r,c=len(heights),len(heights[0])
    minHeap=[(heights[0][0],0,0)] ## (effort,x,y)
    dirs=[(0,1),(1,0),(-1,0),(0,-1)]
    efforts=[[float('inf')]*c for _ in range(r)]
    efforts[0][0]=0

    while True:
        effort,x,y=heapq.heappop(minHeap)
        if x==r-1 and y==c-1:
            return effort
        for dx,dy in dirs:
            newX,newY=x+dx,y+dy
            if not inBounds(newX,newY):
                continue
            newEffort=max(effort,abs(heights[newX][newY]-heights[x][y]))
            if newEffort<efforts[newX][newY]:
                efforts[newX][newY]=newEffort
                heapq.heappush(minHeap,(newEffort,newX,newY))
     
# print(pathWithMinimumEffort([[1,2,2],[3,8,2],[5,3,5]]))
# print(pathWithMinimumEffort([[1,2,3],[3,8,4],[5,3,5]]))

def maximumStringChain(words):
    groups=defaultdict(list)
    wordToIndex=defaultdict(int)
    dp=[-1]*len(words)
    for i,w in enumerate(words):
        groups[len(w)].append(w)
        wordToIndex[w]=i

    def dfs(prevWord):
        indexOfWord=wordToIndex[prevWord]
        if dp[indexOfWord]!=-1:return dp[indexOfWord]
        best= 1
        for w in groups[len(prevWord)+1]:
            i,j=0,0
            while i<len(prevWord) and j<len(w):
                if prevWord[i]==w[j]:
                    i+=1
                    j+=1
                else:
                    j+=1
            if i==len(prevWord):
                    best=max(best,1+dfs(w))
        dp[indexOfWord]=best
        return dp[indexOfWord] 
    for w in words:
            indexOfWord=wordToIndex[w]
            if dp[indexOfWord]==-1:
                dp[indexOfWord]=max(dp[indexOfWord],dfs(w))
    return max(dp)

# print(maximumStringChain(["a","b","ba","bca","bda","bdca"]))
# print(maximumStringChain(["xbc","pcxbcf","xb","cxbc","pcxbc"]))

def champagneTower(poured,query_row,query_glass):
    if query_glass==0 and query_row==0:return min(poured,1)
    prev=[poured]
    cur=[]
    r=2
    while True:
        for c in range(r):
            glass1=prev[c] if c!=r-1 else 0
            glass2=(prev[c-1] if c>0 else 0)
            cur.append(max((glass1-1)/2,0)+max((glass2-1)/2,0))
            if r-1==query_row and c==query_glass:return min(cur[c],1)
        r+=1
        prev=cur
        cur=[]

# print(champagneTower(1,1,1))            
# print(champagneTower(2,1,1)) 

## problem is trivial since the colors taken do not get replaced by the next colors
def removeColoredPiecesIfBothNeiAreSameColor(colors):
    alice,bob=0,0
    i=1
    while i<len(colors)-1:
        if colors[i-1]==colors[i]==colors[i+1]=='A':
            alice+=1        
        elif colors[i-1]==colors[i]==colors[i+1]=='B':
            bob+=1

            i+=1
    return alice>bob           


# print(removeColoredPiecesIfBothNeiAreSameColor("AAABABB"))
# print(removeColoredPiecesIfBothNeiAreSameColor("AA"))

## recursively return the flattened sublist
def flattenList(arr):

    def flatten(subarr):
        if type(subarr)==int:return [subarr]
        result=[]
        for a in subarr:
            buffer=flatten(a)
            for n in buffer:
                result.append(n)
        return result

    return flatten(arr)

# print(flattenList([[1,1],2,[1,1]]))
# print(flattenList([1,[4,[6]]]))

def sumOfAbsoluteValuesInASortedArr(nums):
    initialSum=0
    for n in nums:
        initialSum+=n-nums[0]
    
    sums=[initialSum]
    prevDiff=initialSum
    for i in range(1,len(nums)):
        diffWithPrevElement=nums[i]-nums[i-1]
        delta1=(len(nums)-i-1)*diffWithPrevElement
        prevDiff-=(delta1 if delta1>0 else 0)
        delta2=(i-1)*diffWithPrevElement
        prevDiff+=(delta2 if delta2>0 else 0 )
        sums.append(prevDiff)
    return sums
print(sumOfAbsoluteValuesInASortedArr([2,3,5]))
print(sumOfAbsoluteValuesInASortedArr([1,4,6,8,10]))
