import heapq

## we are tryiing to use ladders for the biggest differences
## so, we want an algo that simlulates the furthest place we can reach without ladders
## when we cannot travel any further , we replace the highest difference with a ladder 
def furthest_building_reach(heights,bricks,ladders):
        i=0
        biggest_deltas=[]
        
        while i<len(heights)-1:
            delta=heights[i+1]-heights[i]
            i+=1
            if delta<=0:continue
            bricks-=delta
            heapq.heappush(biggest_deltas,-delta)
            if bricks<0:
                if ladders==0:return i-1
                max_delta=-1*heapq.heappop(biggest_deltas) if biggest_deltas else 0
                bricks+=max_delta
                ladders-=1

        return i

# print(furthest_building_reach([4,2,7,6,9,14,12],5,1))
# print(furthest_building_reach([4,12,2,7,3,18,20,3,19],10,2))

## dp[i] = largest divisible subset that include index i 
## we save the result of subproblems and return the largest length result

def largest_divisible_subset(nums):
     dp=[0 for _ in range(len(nums))]
     nums.sort()

     def dfs(i):
        if i==len(nums):return []
        if dp[i]!=0:
             return dp[i]
        result=[]      
        for j in range(i+1,len(nums)):
             if nums[j]%nums[i]==0:
                  take=dfs(j)
                  if len(take)>len(result):
                       result=take
        take = [nums[i]] + result    # only extend with divisible children
        dp[i] = take
        return dp[i]

     for j in range(len(nums)):
          dp[j]=dfs(j) 
     res=dp[0]
     for d in dp:
          if len(d)>len(res):
               res=d
     return res
# print(largest_divisible_subset([1,2,3]))
# print(largest_divisible_subset([1,2,4,8]))

def longest_ideal_subsequence(s,k):
   dp= [1]*len(s)

   for i in range(len(s)-2,-1,-1):
        for j in range(i+1,len(s)):
             if abs(ord(s[j])-ord(s[i]))<=k:
                  dp[i]=max(dp[i],1+dp[j])
   return max(dp)
         
## recursive (tle)

# def longestIdealString( s, k) :
#         dp= [0]*len(s) 

#         def dfs(i):
#                 if dp[i]!=0:return dp[i]

#                 res=0
#                 for j in range(i+1,len(s)):
#                     if abs(ord(s[i])-ord(s[j]))<=k:
#                         res=max(res,dfs(j))
#                 dp[i]=1+res
#                 return dp[i]
        
#         for j in range(len(s)):
#                 dfs(j)
                
#         return max(dp)

# print(longest_ideal_subsequence("acfgbd",2))
# print(longest_ideal_subsequence("abcd",3))

## we cant predict the future so we have to try every possible path
## dp will not be useful since we will have to use a bitmask that will have up to 2**n states which uses so much memory
def path_with_max_gold(grid):
     r,c=len(grid),len(grid[0])
     dirs=[(1,0),(0,1),(-1,0),(0,-1)] 
     visit=set()
     res=0
     def dfs(x,y):
          gold=grid[x][y]
          for dx,dy in dirs:
               newX,newY=x+dx,y+dy
               if 0<=newX<r and 0<=newY<c and (newX,newY) not in visit and grid[newX][newY]!=0:
                    visit.add((newX,newY))
                    gold=max(gold,grid[x][y]+dfs(newX,newY))
                    visit.remove((newX,newY))
          return gold
          
     for i in range(r):
          for j in range(c):
               if grid[i][j]==0:continue
               visit.add((i,j))
               res=max(res,dfs(i,j)) 
               visit.remove((i,j))
     return res        
     
# print(path_with_max_gold([[0,6,0],[5,8,7],[0,9,0]]))
# print(path_with_max_gold([[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]))

from collections import deque
def safest_path(grid):
     r,c=len(grid),len(grid[0])
     if grid[0][0]==1:return 0
     ## step 1 : multisource bfs to precompute safeties for every cell

     visit=set() 
     safeties=[[0]*c for _ in range(r)]
     dirs=[(1,0),(0,1),(-1,0),(0,-1)] 
     q=deque()

     for i in range(r):
          for j in range(c):
               if grid[i][j]==1:
                    q.append((i,j,0)) ## (row,column,safety)
                    visit.add((i,j))
    
     while len(visit)<r*c:
         x,y,safety=q.popleft()
         for dx,dy in dirs:
              newX,newY=x+dx,y+dy
              if 0<=newX<r and 0<=newY<c and (newX,newY) not in visit:  
                   visit.add((newX,newY))
                   safeties[newX][newY]=safety+1
                   q.append((newX,newY,safety+1))

     ## step 2 : do djisktras but looking for max instead of minimum

     maxHeap=[(-safeties[0][0],0,0)]
     res=safeties[0][0]
     visit={(0,0)}
     while True:
          safety,x,y=heapq.heappop(maxHeap)
          safety*=-1
          res=min(res,safety) 
          for dx,dy in dirs:
               newX,newY=x+dx,y+dy
               if 0<=newX<r and 0<=newY<c and (newX,newY) not in visit:
                    print(newX,newY)
                    if (newX,newY)==(r-1,c-1):
                         return min(res,safeties[r-1][c-1])
                    visit.add((newX,newY))
                    heapq.heappush(maxHeap,(-safeties[newX][newY],newX,newY))

# print(safest_path([[1,0,0],[0,0,0],[0,0,1]]))
# print(safest_path([[0,0,1],[0,0,0],[0,0,0]]))
# print(safest_path([[0,0,0,1],[0,0,0,0],[0,0,0,0],[1,0,0,0]]))

def delete_leaves_with_given_value(root,target):
     def dfs(cur):
          if not cur.left and not cur.right and cur.val==target:return None
          if cur.left:
            cur.left=dfs(cur.left)
          if cur.right:
            cur.right=dfs(cur.right)
          if not cur.left and not cur.right and cur.val==target:
               return None
          return cur
     return dfs(root)


def house_robber(nums):
     dp=[0 for _ in range(len(nums))]

     for i in range(len(nums)-1,-1,-1):
        dp[i]=dp[i+1] if i+1<len(nums) else 0
        dp[i]=max(nums[i]+ (dp[i+2] if i+2 < len(nums) else 0 )
                    ,dp[i])     
     return dp[0] 
   
# print(house_robber([1,2,3,1]))  
# print(house_robber([2,7,9,3,1]))  

def min_falling_path_sum(matrix):
     r,c=len(matrix),len(matrix[0])
     prevDp=matrix[-1]
     dp=[float('inf')]*c
     dirs=[1,0,-1]
     for i in range(r-2,-1,-1):
        for j in range(c):
            for dx in dirs:
                dp[j]=min(dp[i],matrix[i][j]+ (prevDp[i+dx] if 0<=i+dx<c else float('inf')))
             
        prevDp=dp
     return min(prevDp)

# print(min_falling_path_sum([[2,1,3],[6,5,4],[7,8,9]]))
# print(min_falling_path_sum([[-19,57],[-40,-5]])

          