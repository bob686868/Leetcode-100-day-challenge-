def maxSubsequenceScore(nums1,nums2,k):
    # dp=[[(0,float('inf')) for _ in range(len(nums1))] for _ in range(k)] ## (maxScore,minNum)

    # dp[-1]=(nums1[-1]*nums2[-1],nums2[-1])

    # for i in range(len(nums1)-1,-1,-1):
    #     minNum=min(nums2[i],dp[i+1][1])
    #     candidateScore=((dp[i+1][0]/dp[i+1][1])+nums2[i])*minNum
    #     if candidateScore>dp[i+1][0]:
    #         dp[i]=(candidateScore,minNum)
    #     else:
    #         dp[i]=dp[i+1]
    # return dp[0]
    dp={}
    def dfs(i,numsLeft,minNum):
        if numsLeft==0:return 0
        if i==len(nums1) or numsLeft==0:
            return float('-inf')
        if (i,numsLeft) in dp:
            return dp[(i,numsLeft)]
        newMin=min(minNum,nums2[i])
        
        score1=(((dfs(i+1,numsLeft-1,newMin))/newMin)+nums1[i])*newMin
        score2=dfs(i+1,numsLeft,minNum)

        dp[(i,numsLeft,minNum)]=(max(score1,score2))

        return dp[(i,numsLeft,minNum)]


    return dfs(0,k,float('inf'))

# print(maxSubsequenceScore([1,3,3,2],[2,1,3,4],3))
# print(maxSubsequenceScore([4,2,3,1,1],[7,5,10,9,6],1))

def new21Game(k,maxScore):
    pass 

def stoneGame2(piles):

    dp=[[[0]*2 for _ in range(len(piles))] for _ in range(len(piles))]  ## params : (i,m,isAlicTurn -> 1)

    def dfs(i,isAliceTurn,M):
        if i>=len(piles):return 0
        if dp[i][isAliceTurn][M] !=0 :return dp[i][isAliceTurn][M]
        curSum=0
        for j in range(i,min(i+2*M,len(piles))):
            curSum+=piles[j]
            if isAliceTurn:
                dp[i][isAliceTurn][M]=max(dp[i][isAliceTurn][M],curSum+dfs(j+1,False,max(j-i+1,M)))
            else:
                dp[i][isAliceTurn][M]=min(dp[i][isAliceTurn][M],curSum+dfs(j+1,True,max(j-i+1,M)))
        return dp[i][isAliceTurn][M]

    return dfs(0,True,1)

print(stoneGame2([2,7,9,4,4]))
print(stoneGame2([1,2,3,4,5,100]))