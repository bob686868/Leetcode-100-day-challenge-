##  we basically need to look for the largest 
## area from each cell i,j where the matrix ends at (i,j)

def largestSubMatrix(grid):
    r,c=len(grid),len(grid[0])
    prevHeights=[0]*c
    curHeights=[0]*c
    globalMax=0

    for i in range(r):
        for j in range(c):
            curHeights[j]=prevHeights[j]+grid[i][j] if grid[i][j]!=0 else 0
        sortedCurHeights=sorted(curHeights,reverse=True)
        for j in range(c):
            globalMax=max(globalMax,sortedCurHeights[j]*(j+1))
        curHeights=prevHeights
    return globalMax

# print(largestSubMatrix([[0,0,1],[1,1,1],[1,0,1]]))
# print(largestSubMatrix([[1,0,1,0,1]]))

## we compute subproblems defined by the number of combinations
## of numbers that form a valid number 
## the state is defined by n,r,c
def knightDialer(n):
    if n==1:return 10
    dirs = [
    (2, 1), (2, -1),
    (1, 2), (1, -2),
    (-1, 2), (-1, -2),
    (-2, 1), (-2, -1)
]

    dp=[[[-1]*3 for _ in range(4)] for _ in range(n)]
    def isInBounds(r,c):
        return 0<=r<=3 and 0<=c<=2 and (r!=3 or c==1)
    
    def dfs(n,x,y):
        if n==-1:return 1
        if dp[n][x][y]!=-1:
            return dp[n][x][y]

        dp[n][x][y]=0
        for dx,dy in dirs:
            newX,newY=x+dx,y+dy
            if isInBounds(newX,newY):
                dp[n][x][y]+=dfs(n-1,newX,newY)
        return dp[n][x][y]

        
    res=0
    for i in range(4):
        for j in range(3):
            if i!=3 or j==1:
                res+=dfs(n-2,i,j)
    
    return res

# print(knightDialer(1))
# print(knightDialer(2))


## dp state : (n,curSum)
## base case for n==0 and  

def numOfDiceRollsWithTarget(n,k,target):
    if n==1:return 1 if target<=k else 0
    prevDp=[0]*(target+1)
    prevDp[0]=1

    for i in range(1,n+1):
        curDp=[0]*(target+1)
        for j in range(target+1):
            for d in range(1,k+1):
                if j-d<0:break
                curDp[j]+=prevDp[j-d]
        prevDp=curDp

    return prevDp[target]

# print(numOfDiceRollswWithTarget(1,6,3))
# print(numOfDiceRollsWithTarget(2,6,7))

from collections import defaultdict
## no matter what is the number we are trying to eliminate , we just need its frequency 
## then ,we can compute the operations needed for all possible freqs from 0 to max freq
## dp state : num of freq left
def minOperationsToMakeArrayEmpty(arr):
    counter=defaultdict(int)
    for n in arr:   
        counter[n]+=1
    maxFreq=max(counter.values())
    dp=[float('inf')]*(maxFreq+1)
    dp[0],dp[2]=0,1

    for i in range(3,len(dp)):
        dp[i]=1+min(dp[i-2],dp[i-3])

    
    res=0
    for c in counter.values():
        ops=dp[c]
        if ops==float('inf'):return -1
        res+=ops
    return res 

print(minOperationsToMakeArrayEmpty([2,3,3,2,2,4,2,3,4]))
print(minOperationsToMakeArrayEmpty([2,1,2,2,3,3]))
     



        
