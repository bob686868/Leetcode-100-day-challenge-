def lc3190(nums):
    res=0
    for n in nums:
        res+=min(n%3,3-n%3)
    return res

def lc297(): ## using preorder 
    class TreeNode(object):
        def __init__(self, x):
            self.val = x
            self.left = None
            self.right = None

    class Codec:

        def serialize(self, root):
            if not root:return "None"

            return str(root.val)+","+self.serialize(root.left)+","+self.serialize(root.right)
            
        def deserialize(self, data):
            data=data.split(",")
            i=0
            def dfs():
                nonlocal i
                if  i>=len(data) or data[i]=="None" :
                    i+=1
                    return None
                newNode=TreeNode(data[i])
                i+=1
                newNode.left=dfs()
                newNode.right=dfs()
                
                return newNode
            return dfs()
        

def lc200(grid):
    r,c=len(grid),len(grid[0])
    res=0
    directions=[(1,0),(0,1),(-1,0),(0,-1)]
    visit=set()

    def dfs(i,j):
        stack=[(i,j)]
        visit.add((i,j))
        while stack:
            x,y=stack.pop()
            for dx,dy in directions:
                newX,newY=x+dx,y+dy
                if 0<=newX<r and 0<=newY<c and grid[newX][newY]=="1" and (newX,newY) not in visit:
                    stack.append((newX,newY))
                    visit.add((newX,newY))

    for i in range(r):
        for j in range(c):
            if grid[i][j]=="1" and (i,j) not in visit:
                res+=1
                dfs(i,j)
    return res

# print(lc200([
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]))
# print(lc200( [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]))

def lc206(head):
    if not head or not head.next:return head
    cur,prev=head.next,head
    head.next=None


    while cur:
        nextNode=cur.next
        cur.next=prev
        prev=cur
        cur=nextNode
    return prev

def lc79(board,word):
    r,c=len(board),len(board[0])
    directions=[(1,0),(0,1),(-1,0),(0,-1)]
    visit=set()
    def dfs(x,y,i):
       nonlocal visit
       if i==len(word):return True
       if board[x][y]!=word[i]:return False
       for dx, dy in directions:
           newX,newY=x+dx,y+dy
           if 0<=newX<r and 0<=newY<c and (newX,newY) not in visit:
               visit.add((newX,newY))
               if dfs(newX,newY,i+1):
                 return True
       return False
           
       
    for i in range(r):
        for j in range(c):
            visit=set()
            if board[i][j]==word[0] and dfs(i,j,0):
                return True
    return False

# print(lc79([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],"ABCCED"))
# print(lc79([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],"SEE"))
# print(lc79([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],"ABCB"))

from collections import defaultdict
def lc207(numCourses,prerequisites):
    nei=defaultdict(set)
    for src,dst in prerequisites:
        nei[src].add(dst)

    dp=[None]*numCourses
    def dfs(i):
        if dp[i]!=None:return dp[i]

        dp[i]=False
        for n in nei[i]:
            print(n)
            if not dfs(n):
                return False
        dp[i]=True
        return dp[i]
    for i in range(numCourses):
        if not dfs(i):
            return False
    return True

# print(lc207(2,[[1,0]]))
# print(lc207(2,[[1,0],[0,1]]))

##                      TLE
# def lc300(nums):
#     dp={}
#     res=0
#     def dfs(i,prev):
#         if i==len(nums):return 0
#         if (i,prev) in dp:return dp[(i,prev)]
#         skip=dfs(i+1,prev)
#         take=0
#         if nums[i]>prev:
#             take=1+dfs(i+1,nums[i])
        
#         dp[(i,prev)]=max(skip,take)
#         return dp[(i,prev)]

#     for i in range(len(nums)):
#         res=max(res,dfs(i,float('-inf')))

#     return res


def lc300(nums):
    dp=[1]*len(nums) ## lis starting at i and including nums[i]
    dp[-1]=1

    for i in range(len(nums)-2,-1,-1):
        for j in range(i+1,len(nums)):
            if nums[i]<nums[j]:
                dp[i]=max(dp[i],1+dp[j])
    print(dp)
    return max(dp)
        

# print(lc300([10,9,2,5,3,7,101,18]))
# print(lc300([1,3,6,7,9,4,10,5,6]))

def lc338(n): ## computes the num of 1's in O(1)
    res=[-1]*(n+1)
    res[0]=0


    for i in range(1,n+1):
        res[i]=res[i//2]+(i%2)
    return res

# print(lc338(2))
# print(lc338(5))

from collections import Counter
def lc76(s,t):
    counterS=defaultdict(int)
    counterT=Counter(t)
    need=len(counterT)
    resR,resL=float('inf'),0
    r=0  ## not including the char at r itself

    for l in range(len(s)-len(t)+1):
        while r<len(s) and need>0:
            char=s[r]
            r+=1
            if char in counterT:
                counterS[char]+=1
                need-=(counterS[char]==counterT[char])
        if need==0 and r-l<resR-resL:
            resL,resR=l,r

        oldChar=s[l]
        if oldChar in counterT:
            need+=(counterS[oldChar]==counterT[oldChar])
            counterS[oldChar]-=1
    return s[resL:resR] if resR!=float('inf') else ""

# print(lc76("ADOBECODEBANC","ABC"))
# print(lc76("a","a"))
# print(lc76("a","aa"))