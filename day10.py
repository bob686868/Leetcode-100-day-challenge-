import heapq
def maxSubsequenceScore(nums1,nums2,k):
    sortedNums=sorted([(n2,n1) for n1,n2 in zip(nums1,nums2)],reverse=True)

    score=0
    minNumsToRemove=[]
    for i in range(k):
        n2,n1=sortedNums[i]
        heapq.heappush(minNumsToRemove,n1)
        score+=n1
    score*=sortedNums[k-1][0]
    maxScore=score
    for i in range(k,len(sortedNums)):
        ## remove old element
        minNum=heapq.heappop(minNumsToRemove)
        score/=sortedNums[i-1][0]
        score-=minNum

        ## add new element
        n2,n1=sortedNums[i]
        heapq.heappush(minNumsToRemove,n1)
        score+=n1
        score*=n2   
        maxScore=max(maxScore,score) 
    return maxScore   

# print(maxSubsequenceScore([1,3,3,2],[2,1,3,4],3))
# print(maxSubsequenceScore([4,2,3,1,1],[7,5,10,9,6],1))

from collections import deque
## general plan : to calculate probability ,we need favorable cases and total cases 
## to compute favorable cases , we substract (totalPossibilites starting from n =0)from possibilitesGreaterThanN
def new21Game(n,k,maxPts):
    if k+maxPts<n or k==0 :return 1
    totalPossibilites=deque([1 for _ in range(maxPts)])  ## for i > k => possibilities=1
    possibilitiesGreaterThanN=0

    ## step 1 : initialize the possibilitesGreaterThanN
    if n>k:possibilitiesGreaterThanN=1

    for i in range(k,-1,-1):
        newEntry=0
        for j in range(maxPts):
            newEntry+=totalPossibilites[j]
        totalPossibilites.appendleft(newEntry)
        if i==n+1:possibilitiesGreaterThanN=totalPossibilites[0]
        totalPossibilites.pop()
    return possibilitiesGreaterThanN/totalPossibilites[0]

# print(new21Game(10,1,10))
# print(new21Game(6,1,10))
# print(new21Game(21,17,10))

        

def stoneGame2(piles):

    dp=[[[-1]*2 for _ in range(len(piles))] for _ in range(len(piles))]  ## params : (i,m,isAlicTurn -> 1)

    def dfs(i,isAliceTurn,M):
        if i>=len(piles):return 0
        if dp[i][isAliceTurn][M] !=0 :return dp[i][isAliceTurn][M]
        curSum=0
        for j in range(i,min(i+2*M,len(piles))):
            curSum+=piles[j]
            if isAliceTurn:
                dp[i][isAliceTurn][M]=max(dp[i][isAliceTurn][M],curSum+dfs(j+1,False,max(j-i+1,M)))
            else:
                dp[i][isAliceTurn][M]=min(dp[i][isAliceTurn][M],dfs(j+1,True,max(j-i+1,M)))
        return dp[i][isAliceTurn][M]

    return dfs(0,True,1)

print(stoneGame2([2,7,9,4,4]))
print(stoneGame2([1,2,3,4,5,100]))