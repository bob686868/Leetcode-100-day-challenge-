def lc3573(prices,k):
    n=len(prices)
    dp=[[[-1]*3  for _ in range(k+1)]for _ in range(n)]

    def dfs(i,k2,isCarrying): ## 0=> short  ; 1=> not carrying ; 2 => normal
        if(i==n and isCarrying!=1) :return float('-inf')
        if k2==0 or i==n:return 0
        if dp[i][k2][isCarrying]!=-1:return dp[i][k2][isCarrying]

        res=dfs(i+1,k2,isCarrying)
        if isCarrying==1:
            normal=-prices[i]+dfs(i+1,k2,2)
            short=prices[i]+dfs(i+1,k2,0)
            res=max(res,normal,short)
        elif isCarrying==0:
            res=max(res,-prices[i]+dfs(i+1,k2-1,1))
        else:
            res=max(res,prices[i]+dfs(i+1,k2-1,1))

        dp[i][k2][isCarrying]=res
        return res

    return dfs(0,k,1)
d
# print(lc3573([1,7,9,8,2],2))
# print(lc3573([12,16,19,19,8,1,19,13,9],3))