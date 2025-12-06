# Top Down

def lc3578(nums,k):
        dp=[-1]*len(nums)

        def dfs(i):
            if i==len(nums):return 1
            if dp[i]!=-1:return dp[i]

            r=i+1
            n,N=nums[i],nums[i]
            res=0
            while r<=len(nums):
                res+=dfs(r)
                if r==len(nums):break
                n=min(n,nums[r])
                N=max(N,nums[r])
                if N-n>k:break
                r+=1
            dp[i]=max(1,res)%(10**9+7)
            return dp[i]
        
        return dfs(0) % (10**9+7)


# print(lc3578([9,4,1,3,7],4))
# print(lc3578([3,3,4],0))

## Bottom Up

def lc3578(nums,k):
        dp=[-1]*(len(nums)+1)
        dp[-1]=1

        for i in range(len(nums)-1,-1,-1):
             n,N=nums[i],nums[i]
             r=i+1
             res=0
             while r <=len(nums):
                  res+=dp[r]
                  if r==len(nums):break
                  n=min(nums[r],n)
                  N=max(nums[r],N)
                  if N-n>k:break
                  r+=1
             dp[i]=res  % (10**9+7)
        return dp[0] % (10**9+7)

# print(lc3578([9,4,1,3,7],4))
# print(lc3578([3,3,4],0))