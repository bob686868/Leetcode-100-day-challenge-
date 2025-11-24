def lc1018(nums):
        res=[]
        cur=0

        for n in nums:
            cur<<=1
            cur+=n
            res.append(not cur%5)
        return res

# print(lc1018([0,1,1]))
# print(lc1018([1,1,1]))

def lc98(root):
        def dfs(node,minNum,maxNum):
                if not node:return True
                if node.val<=minNum or node.val>=maxNum:return False

                return dfs(node.left,minNum,node.val) and dfs(node.right,node.val,maxNum)
                
                
        return dfs(root,float('-inf'),float('inf'))

def lc226(root):
        def dfs(node):
            if not node:return None
            tmp=node.left
            node.left=dfs(node.right)
            node.right=dfs(tmp)
            return node
        return dfs(root)

def lc100(p,q):
       def dfs(r1,r2):
              if not r1 and not r2:return True
              if not r1 or not r2:return False
              if r1.val!=r2.val:return False

              return dfs(r1.left,r2.left) and dfs(r1.right,r2.right)
              
       return dfs(p,q)

def lc104(root):
       def dfs(node):
              if not node:return 0
              
              return 1+max(dfs(node.left),dfs(node.right))
       return dfs(root)

def lc230(root,k):
        k2=0
        def dfs(node):
            if not node:return None
            nonlocal k2
            
            left=dfs(node.left)
            if left is not None:return left

            k2+=1
            if k2==k:return node.val
            
            right=dfs(node.right)
            if right is not None:return right

        return dfs(root)

from collections import deque
def lc102(root):
        if not root:return []
        res=[]
        q=deque()
        q.append(root)

        while q:
                subRes=[]

                for _ in range(len(q)):
                        node=q.popleft()
                        if node.left:q.append(node.left)
                        if node.right:q.append(node.right)
                        subRes.append(node.val)
                res.append(subRes)

        return res

# def lc1143(s1,s2):
#        dp=[[-1]*len(s2) for _ in range(len(s1))]

#        def dfs(i,j):
#               if i>=len(s1) or j>=len(s2):
#                      return 0
#               if dp[i][j]!=-1:return dp[i][j]

#               if s1[i]==s2[j]:
#                      dp[i][j]=1+dfs(i+1,j+1)
#                      return dp[i][j]
#               dp[i][j]=max(dfs(i+1,j),dfs(j+1,i))
#               return dp[i][j]
#        return dfs(0,0)

def lc1143(s1,s2):
       dp=[[0]*(len(s2)+1) for _ in range(len(s1)+1)]

       for i in range(len(s1)-1,-1,-1):
              for j in range(len(s2)-1,-1,-1):
                     if s1[i]==s2[j]:
                            dp[i][j]=1+dp[i+1][j+1]
                     else:
                            dp[i][j]=max(dp[i+1][j],dp[i][j+1])
       return dp[0][0]

# print(lc1143("abcde","ace"))
# print(lc1143("abc","abc"))

def lc125(s):
        l,r=0,len(s)-1

        while l<=r:
                
                while l<len(s) and not s[l].isalnum() :
                        l+=1
                if l==len(s):return True
                while not s[r].isalnum():
                        r-=1
                if not s[l].lower()==s[r].lower():return False
                l+=1
                r-=1
        return True

# print(lc125("A man, a plan, a canal: Panama"))
# print(lc125("race a car"))
from collections import Counter

def lc242(s,t):
       if len(s)!=len(t):return False
       c1=Counter(s) 
       c2=Counter(t) 

       return all(c1[c]==c2[c] for c in c1)

# print(lc242("anagram","nagaram"))
# print(lc242("rat","car"))

       

