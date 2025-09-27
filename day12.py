import math
from collections import defaultdict,deque


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    # check divisors of form 6k ± 1 up to sqrt(n)
    limit = int(math.isqrt(n))
    for i in range(5, limit + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True
def collectorSet(nums):
    
    minNumSet=set()
    def dfs(i): ## i = currentNum to check
        
        if i==len(nums)-1:return remainingNums

        if i not in remainingNums:return dfs(i+1)
        for j in range(i+1,len(nums)):
            if nums[j] in remainingNums and is_prime(nums[j]+nums[i]):
                remainingNums.remove(nums[i])
                res1=dfs(i+1)
                remainingNums.add(nums[i])
                remainingNums.remove(nums[j])
                res2=dfs(i+1)
            if len(res1)>len(res2):return res1
            else : return res2

    remainingNums=set(nums)
    remaining=dfs(0)
    deleted=[]
    for n in nums:
        if n not in remaining:
            deleted.append(n)
    return deleted
# n=int(input())
# nums=list(map(int,input()))
# print(collectorSet(nums))
def minimumTimeToInformAllEmployees(n,headID,managers,informTimes):
        adj=defaultdict(list)

        for i,m in enumerate(managers):
            adj[m].append(i)

        q=deque([headID])
        
        def dfs(employeeID):
            if adj[employeeID]==[]:return 0
            maxTime=float('-inf')
            for e in adj[employeeID]:
                maxTime=max(maxTime,dfs(e))
            return informTimes[employeeID]+maxTime
            
        return dfs(headID)



# print(minimumTimeToInformAllEmployees(1,0,[-1],[0]))  
# print(minimumTimeToInformAllEmployees(6,2,[2,2,-1,2,2,2],[0,0,1,0,0,0]))  

class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None


# def bst2(n):
#     result=set()
#     remainingNums=set(range(1,n+1))

#     def constructor(root,tree,v):
#         if v!=-1:insertNode(v,tree)
#         if len(remainingNums)==0:return result.add(Node(root))
            
#         for v in remainingNums:
#             remainingNums.remove(v)
#             constructor(root,tree,v)
#             remainingNums.add(v)
            
#     def insertNode(val,tree):
#         cur=tree
#         while True:
#             if cur.val<val:
#                 if not cur.right:
#                     cur.right=Node(val)
#                     return True
#                 cur=cur.right
#             else:
#                 if not cur.left:
#                     cur.left=Node(val)
#                     return True
#                 cur=cur.left

            
#     for v in remainingNums:
#         remainingNums.remove(v)
#         constructor(v,Node(v),-1)
#         remainingNums.add(v)
#     return result

# print(bst2(3))
# print(bst2(4))

def minimizeMaximumDifference(nums,p):
    dp=[[float('inf')]*p for _ in range(len(nums))] 
    nums.sort()
    def dfs(i,p):  ## from position i and with p pairs remaining what is the minimum maximum difference (p values in dp range from 0 to p-1)
        if i+1>=len(nums) and p!=0 :return float('inf')
        if p==0 :return 0
        if dp[i][p-1]!=float('inf'):return dp[i][p-1]

        remainingNums=len(nums)-i
        if remainingNums<2*p: return float('inf')
        newDiff=abs(nums[i+1]-nums[i])
        dp[i][p-1]=min(dp[i][p-1],max(newDiff,dfs(i+2,p-1)))
        dp[i][p-1]=min(dp[i][p-1],dfs(i+1,p))

        return dp[i][p-1]
    return dfs(0,p)

print(minimizeMaximumDifference([10,1,2,7,1,3],2))
print(minimizeMaximumDifference([4,2,1,2],1))