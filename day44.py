def lc757(intervals):
        for i,(s,e) in enumerate(intervals):
            intervals[i]=[e,s]
        intervals.sort()
        res=0
        prev1,prev2=-1,-1  ## prev2 < prev1 
        ## we have 3 possibilites : 
        ##   1- both prev picken arent in cur range -> res+=2
        ##   2 -prev2 only isnt in the domain       -> res+=1
        ##   3- both prev values in domain          ->res+=0
        for e,s in intervals:
            if prev1<s and prev2<s:
                res+=2
                prev1=e
                prev2=e-1
            elif prev2<s:
                res+=1
                prev2=e if prev1!=e else e-1
                if prev2>prev1:
                    prev1,prev2=prev2,prev1
        return res

# print(lc757([[1,3],[3,7],[8,9]]))
# print(lc757([[1,3],[1,4],[2,5],[3,5]]))
# print(lc757([[1,2],[2,3],[2,4],[4,5]]))

def lc152(nums):
        globalMax=max(nums)
        intialMax=globalMax
        hasMaxModified=False
        curMin,curMax=1,1
        
        for n in nums:
            tmp=curMin
            curMin=min(1,curMax*n,curMin*n)
            if curMax*n >=1 or tmp*n>=1:
                hasMaxModified=True
            curMax=max(1,curMax*n,tmp*n) 
            if curMax>globalMax:
                globalMax=curMax
        return globalMax if hasMaxModified else intialMax
     
# print(lc152([2,3,-2,4]))
# print(lc152([-2,0,-1]))

def lc153(nums):
     if nums[0]<=nums[-1]:return nums[0]
     n=len(nums)
     l,r=1,n-1

     while l<=r:
          m=(l+r)//2
          if m==n-1:return nums[m]
          if nums[m-1]>nums[m]<nums[m+1]:
               return nums[m]
           ## right sorted portion
          if nums[m]<nums[-1]:
            r=m-1
          else:
               l=m+1
     return nums[m]

# print(lc153([3,4,5,1,2]))
# print(lc153([4,5,6,7,0,1,2]))


def lc417(heights):
     r,c=len(heights),len(heights[0])
     pacific=set()
     atlantic=set()
     dirs=[(0,1),(1,0),(0,-1),(-1,0)]
     def dfs(ocean,x,y):
          stack=[(x,y)]
          while stack:
            x,y=stack.pop()
            for dx,dy in dirs:
                newX,newY=x+dx,y+dy
                if 0<=newX<r and 0<=newY<c and (newX,newY) not in ocean and heights[newX][newY]>=heights[x][y]:
                     ocean.add((newX,newY))
                     stack.append((newX,newY))
     ## pacific
     for i in range(r):
          pacific.add((i,0))
          dfs(pacific,i,0)
     for j in range(c):
          pacific.add((0,j))
          dfs(pacific,0,j)
     ## atltantic
     for i in range(r):
          atlantic.add((i,c-1))
          dfs(atlantic,i,c-1)
     for j in range(c):
          atlantic.add((r-1,j))
          dfs(atlantic,r-1,j)
     res=[]
     for x,y in pacific :
          if (x,y) in atlantic:
               res.append([x,y])

     return res

print(lc417([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]))
print(lc417([[1]]))

from sortedcontainers import SortedList
def lc295():
    class MedianFinder:

        def __init__(self):
            self.nums=SortedList()
            

        def addNum(self, num: int) -> None:
            self.nums.add(num)

        def findMedian(self) -> float:
                nums=self.nums
                half=len(nums)//2
                if len(nums)%2==0:
                    return (nums[half]+nums[half-1])/2
                return nums[half]
