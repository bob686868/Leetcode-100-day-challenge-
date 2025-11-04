## dynamic programming with 2 variables representing the state : 
## (the index in nums , and k)
# def houseRobber4(nums,k):
#     dp=[[float('inf')]*(k+1) for _ in range(len(nums))]  ## [index of nums][k]

#     def dfs(i,k_left):
#         if k_left==0:return 0
#         if i>=len(nums):
#             return float('inf')
#         if dp[i][k_left]!=float('inf'):
#             return dp[i][k_left]

#         ## take 
#         take=max(dfs(i+2,k_left-1),nums[i])
#         ## skip
#         skip=dfs(i+1,k_left)

#         dp[i][k_left]=min(take,skip)
#         return dp[i][k_left]

#     return dfs(0,k)

## solution 2 

def houseRobber4(nums,k):
    l,r=0,10**9
    res=10**9
    

    while l<=r:
        m=(l+r)//2
        taken=0

        canTake=True
        for n in nums:
            if n<=m and canTake:
                taken+=1
                canTake=False
            else:
                canTake=True

        if taken>=k:
            r=m-1
            res=m
        else:
            l=m+1
    return res


# print(houseRobber4([2,3,5,9],2))
# print(houseRobber4([2,7,9,3,1],2))

import math
def minimumTimeToRepairCars(ranks,cars):
    l,r,res=0,10**14,10**14

    while l<=r:
        m=(l+r)//2

        repaired_cars=0
        for rank in ranks:
            repaired_cars+=math.floor( (m/rank)**0.5 )
        if repaired_cars>=cars:
            res=m
            r=m-1
        else:
            l=m+1

    return res

# print(minimumTimeToRepairCars([4,2,3,1],10))
# print(minimumTimeToRepairCars([5,1,8],6))

def longestNiceSubarray(nums):
    l,r,res=0,0,0

    def isNice():
        for i in range(l,r+1):
            if nums[r+1] & nums[i]!=0:return False
        return True
    
    for l in range(len(nums)):
        while r<len(nums)-1 and isNice():
            r+=1
            res=max(res,r-l+1)
    return res

# print(longestNiceSubarray([1,3,8,48,10]))
# print(longestNiceSubarray([3,1,5,11,13]))

def longest_fibonacci_subarray(nums):
    res=min(2,len(nums))
    l,r=0,1

    while r<len(nums)-1:

        if nums[r+1]==nums[r]+nums[r-1]:
            r+=1
            res=max(res,r-l+1)
        else:
            l=r
            r+=1
    return res

# print(longest_fibonacci_subarray([1,1,1,1,2,3,5,1]))
# print(longest_fibonacci_subarray([5,2,7,9,16]))

def minOpsToMakeOnes(nums):
    res=0
    for i in range(len(nums)-2):

        if nums[i]==0:
            res+=1
            nums[i+1]^=1
            nums[i+2]^=1
    
    if nums[len(nums)-1] == nums[len(nums)-2] == 1:
        return res
    
    return -1
   
    
# print(minOpsToMakeOnes([0,1,1,1,0,0]))
# print(minOpsToMakeOnes([0,1,1,1]))
