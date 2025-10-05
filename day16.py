## we know that the priority to make a number smallest is to manipulate its most significant digits 
## thus , we can be greedy and only remove numbers when that removal will make the 
## corresponding digit at the cur position smaller 
## we know that removing any of the digits in the stack (mono increasing) will make the correspding digit bigger 
## so if the code stops and we have removals left , then we choose to remove the last digits 

def remove_k_digits(num,k):
    stack=[]

    for n in num:
        while stack and n<stack[-1] and k>0:
            stack.pop()
            k-=1
        stack.append(n)

    return "".join(stack[:len(num)-k]).lstrip("0")

# print(remove_k_digits("1432219",3))
# print(remove_k_digits("10200",1))


## try each car as the bottleneck and look for the cars that bumped into it

def carFleet(target,position,speed):
    pws=[(position[i],speed[i]) for i in range(len(position))]
    pws.sort(reverse=True)
    prevTime=(target-pws[0][0])/pws[0][1]
    fleet=1
    for i in range(1,len(pws)):
        p,s=pws[i]
        time=(target-p)/s
        if time>prevTime:
            fleet+=1
            prevTime=time
    return fleet

# print(carFleet(12,[10,8,0,5,3],[2,4,1,1,3]))
# print(carFleet(10,[3],[3]))
# print(carFleet(100,[0,2,4],[4,2,1]))

## we can try every minimum value as the start of a subarray
## the subarray can be extended until a smaller element is found , so using a stack is convenient 
## specifically , since we pop elements greater than the new value to add , the stack will be mono increasing

def max_subarray_min_product(nums):
    stack=[(nums[0],0)]
    res=nums[0]**2
    prefixSum=[0]

    for n in nums:
        prefixSum.append(prefixSum[-1]+n)

    for i,n in enumerate(nums):
        if i==0:continue
        pos=i
        while stack and n<stack[-1][0]:
            num,pos=stack.pop()
            res=max(res,num*(prefixSum[i]-prefixSum[pos]))
        stack.append((n,pos))

    while stack:
        num,pos=stack.pop()
        res=max(res,num*(prefixSum[-1]-prefixSum[pos]))
    return res

# print(max_subarray_min_product([1,2,3,2]))
# print(max_subarray_min_product([2,3,3,1,2]))
# print(max_subarray_min_product([3,1,5,6,4,2]))

class MinStack:

    def __init__(self):
        self.stack=[]
        self.minimums=[]

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.minimums.append(min(val,self.minimums[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.minimums.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minimums[-1]

from collections import defaultdict,deque
def min_height_tree(n,edges):
        if not edges:return [0]
        nei=defaultdict(list)
        degrees=[0]*n
        remain=n

        for s,d in edges:
            nei[s].append(d) 
            nei[d].append(s)
            degrees[s]+=1
            degrees[d]+=1
        
        q=deque([i for i in range(n) if degrees[i]==1])
        
        while remain>2:
            for i in range(len(q)):
                n=q.popleft()
                for i in nei[n]:
                    degrees[i]-=1
                    if degrees[i]==1:
                        q.append(i)
                remain-=1
        return list(q)

# print(min_height_tree(4,[[1,0],[1,2],[1,3]]))
# print(min_height_tree(6,[[3,0],[3,1],[3,2],[3,4],[5,4]]))

def generate_parantheses(n):
    dp=[[[] for _ in range(n+2)] for _ in range(2*n+1)]
    def dfs(c,delta):
        if dp[c][delta]!=[]:return dp[c][delta]
        if c==0 and delta==0:return [""]
        if c==0 :return []

        res1=[]
        res2=[]
        if delta>0:
            res1=dfs(c-1,delta-1)
        if delta<n:
            res2=dfs(c-1,delta+1)
        res1=[")" + s for s in res1]
        res2=["(" + s for s in res2]
                
        dp[c][delta]=res1+res2
        return dp[c][delta]
        
    return dfs(2*n,0)

# print(generate_parantheses(2))
# print(generate_parantheses(3))

## we need to try every largest area that include heights[i]
## for that , we need to know the next smaller height for which we cannot expand further
## so , it is useful to use a monotonic increasing stack

def largestRectangleHistogram(heights):
        stack=[]
        res=0
        heights.append(-1)

        for i,h in enumerate(heights):
            i_prev=i
            while stack and h<stack[-1][0]:
                h_prev,i_prev=stack.pop()
                res=max(res,(i-i_prev)*h_prev)
            stack.append((h,i_prev))
        return res

# print(largestRectangleHistogram([2,1,5,6,2,3]))
# print(largestRectangleHistogram([2,4]))

## we need an efficient way to know the longest contiguous subarray ending at index i 
## so , we can along our way compute a mapping of the difference between count of zeroes and 
## ones and map it to its smallest index

def contiguousArray(nums):
    diffToIndex={0:-1}
    delta=0
    res=0

    for i,n in enumerate(nums):
        delta+=(1 if n==1 else -1)
        prefix_index=diffToIndex.get(delta,i)
        res=max(res,i-prefix_index)
        if diffToIndex.get(delta,-2)==-2:
            diffToIndex[delta]=i
    
    return res
# print(contiguousArray([0,1]))
# print(contiguousArray([0,1,0]))
# print(contiguousArray([0,1,1,1,1,1,0,0,0]))

## try every subarray ending at index i , and add to the result all the 
## subarrays that have sum equal to the needed difference between cur sum and target 

def binary_subarray_with_sum(nums,target):
    sumToCount=defaultdict(int)
    sumToCount[0]=1
    res=0
    cur_sum=0

    for n in nums:
        cur_sum+=n
        res+=sumToCount[cur_sum-target]
        sumToCount[cur_sum]+=1

    return res

# print(binary_subarray_with_sum([1,0,1,0,1],2))
# print(binary_subarray_with_sum([0,0,0,0,0],0))

    


     

        





