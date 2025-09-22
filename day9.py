def spiralMatrix2(n):
    result=[[0]*n for _ in range(n)]
    l,r=0,n-1
    t,b=0,n-1
    cur=1
    while l<=r:
        for i in range(l,r+1):
            result[t][i]=cur
            cur+=1
        t+=1
        for j in range(t,b+1):
            result[j][r]=cur
            cur+=1
        r-=1
        for k in range(r,l-1,-1):
            result[b][k]=cur
            cur+=1
        b-=1
        for i in range(b,t-1,-1):
            result[i][l]=cur
            cur+=1
        l+=1

    return result

# print(spiralMatrix2(3))

## we have to try every possibility of skipping an element , 
## but if elements are equal , no need to try to skip  

## first method : recursion  (TLE)

# def uncrossedLines(arr1,arr2):
#     dp=[[0]*len(arr2) for _ in range(len(arr1))]
#     def dfs(n1,n2):
#         if n1==len(arr1) or n2==len(arr2):
#             return 0
#         if dp[n1][n2]!=0:return dp[n1][n2]
#         if arr1[n1]==arr2[n2]:
#             dp[n1][n2]=1+dfs(n1+1,n2+1)
#         else:
#             dp[n1][n2]=max(dfs(n1+1,n2),dfs(n1,n2+1))
#         return dp[n1][n2]
#     return dfs(0,0)
# print(uncrossedLines([1,4,2],[1,2,4]))
# print(uncrossedLines([2,5,1,2,5],[10,5,2,1,5,2]))

## second method : tabulation 
def uncrossedLines(nums1,nums2):
    n1,n2=len(nums1),len(nums2)
    dp=[[0]*(n2+1) for _ in range(n1+1)]

    for i in range(n1-1,-1,-1):
        for j in range(n2-1,-1,-1):
            if nums1[i]==nums2[j]:
                dp[i][j]=1+dp[i][j+1]
            else:
                dp[i][j]=max(dp[i][j+1],dp[i+1][j])
    return dp[0][0]

# print(uncrossedLines([1,4,2],[1,2,4]))
# print(uncrossedLines([2,5,1,2,5],[10,5,2,1,5,2]))

## classic dp (tabulation)

def solveQuestionsWithBrainPower(questions): ## (score,brainpower)
    dp=[0]*len(questions) ## maximum score achievable from position i 
    for i in range(len(questions)-1,-1,-1):
        score,bp=questions[i]
        dp[i]=max(dp[i+1] if i+1<len(questions) else 0,score+(dp[i+bp+1] if i+bp+1<len(questions) else 0))
    return dp[0]

# print(solveQuestionsWithBrainPower([[3,2],[4,3],[4,4],[2,5]]))
# print(solveQuestionsWithBrainPower([[1,1],[2,2],[3,3],[4,4],[5,5]]))

## TLE 
def numOfGoodStrings(low,high,zeros,ones):
    mod=10**9+7
    dp=[[0]*(high+1) for _ in range(high+1)] ## num of good strings with i zeroes and j ones intially used 
                                             ## row -> num of zeroes 
                                             ## col -> num of ones
    for i in range(high,-1,-1):
        for j in range(high,-1,-1):
            if i+j>high:
                break
            incrementer=1 if low<=i+j<=high else 0
            includeZeroes=dp[i+zeros][j] if i+zeros+j<=high else 0
            includeOnes=dp[i][j+ones] if j+ones+i<=high else 0 
            dp[i][j]=(incrementer+includeZeroes+includeOnes)%mod 
    return dp[0][0]%mod 

# print(numOfGoodStrings(3,3,1,1))
# print(numOfGoodStrings(2,3,1,2))

from collections import defaultdict
# class Node:
#     def __init__(self,char):
#         self.char=char
def evaluateDivision(equations,values,queries):
    adj=defaultdict(list) ## [(dst,multiplier)]

    for i,(e1,e2) in enumerate(equations):
        adj[e1].append((e2,values[i]))
        adj[e2].append((e1,1/values[i]))
    
    result=[]

    def dfs(n,prev,curCost):
        for nei,cost in adj[n]:
            if nei ==prev:continue
            if nei==c2:
                return curCost*cost
            ans=dfs(nei,n,curCost*cost)
            if ans!=-1:
                return ans
        return -1
    for c1,c2 in queries:
        if c1==c2:
            if adj[c1]!=[]:
                result.append(1)
            else:
                result.append(-1)
            continue
        ans=dfs(c1,-1,1)
        result.append(ans)
    return result
            
print(evaluateDivision([["a","b"],["b","c"]],[2.0,3.0],[["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]))
print(evaluateDivision([["a","b"],["b","c"],["bc","cd"]],[1.5,2.5,5.0],[["a","c"],["c","b"],["bc","cd"],["cd","bc"]]))