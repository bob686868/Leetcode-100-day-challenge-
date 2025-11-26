def lc2453(grid,k):
    m,n=len(grid),len(grid[0])
    dp=[[[None]*k for _ in range(n)] for _ in range(m)]

    def dfs(i,j,remainder):
        if i==m-1 and j==n-1:
            if remainder==grid[i][j]%k:return 1
            else:return 0
        if i>=m or j>=n:return 0
        if dp[i][j][remainder]!=None:return dp[i][j][remainder]

        dp[i][j][remainder]=dfs(i+1,j,(remainder-grid[i][j])%k)+dfs(i,j+1,(remainder-grid[i][j])%k)

        return dp[i][j][remainder]
    res=dfs(0,0,0)
    return res

# print(lc2453([[5,2,4],[3,0,5],[0,7,2]],3))
# print(lc2453([[0,0]],5))
# print(lc2453([[7,3,4,9],[2,3,6,2],[2,3,7,0]],1))


