from collections import deque
from collections import defaultdict

## add each level to the cur buffer then add it to res 
## we then reverse it based on the level (odd or even)

def BTZigzagTraversal(root):
        if not root:return []
        res=[]
        q=deque()
        q.append((0,root))
        while q :
            cur=[]
            size=len(q)
            for _ in range(size):
                level,node=q.popleft()
                cur.append(node.val)
                q.append((level+1,node.left)) if node.left else None
                q.append((level+1,node.right)) if node.right else None
            if level%2==1:res.append(list(reversed(cur)))
            else:res.append(cur)
        return res

## if we solve problem backwards (more convenient in dp) we 
## can move either to top or to left , and hence the recursive formula 
def uniquePathsTwo(n,m):
     dp=[[1]*m for _ in range(n)]
    
     for i in range(1,n):
          for j in range(1,m):
               dp[i][j]=dp[i][j-1]+dp[i-1][j]

     return dp[n-1][m-1]

# print(uniquePathsTwo(3,7))
# print(uniquePathsTwo(3,2))

def pathWithHighestProba(edges,start,end,probabilities ):
    adj=defaultdict(list)

    for i,src,dst in enumerate(edges):
        adj[src].append((i,dst))
        adj[dst].append((i,src))

    visit=set()
    res=-1
    def dfs(node,proba,prev):
         nonlocal res
         if node==end:return proba 
         for index,nei in adj[node]:
              if nei != prev:
                visit.add(nei)
                res=max(dfs(nei,proba*probabilities[index],node),res)
                visit.remove(nei)
    return dfs(start,1,-1)
     