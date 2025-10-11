def minimum_deletions_to_make_balanced(s):
    dp=[[float('inf')]*2 for _ in range(len(s))]


    def dfs(i,startedChoosingB):
        if i==len(s):return 0
        if dp[i][startedChoosingB]!=float('inf'):return dp[i][startedChoosingB]
        res=0
        if (startedChoosingB and s[i]!="b") \
            or (not startedChoosingB and s[i]!="a"):
            res=1

        c1=dfs(i+1,startedChoosingB)
        c2=float('inf')
        if not startedChoosingB:
            c2=dfs(i+1,True)
        res+=min(c1,c2)

        dp[i][startedChoosingB]=res
        return res
    
    return min(dfs(0,True),dfs(0,False))

# print(minimum_deletions_to_make_balanced("aababbab"))
# print(minimum_deletions_to_make_balanced("bbaaaaabb"))


## there are two ways to join groups of ones :
## first way is to shift them from end to start to fill the gaps(zero values)
## or do the same thing but by looping around the array in a circular way

import heapq

## instead of generating every subquery sum , we can generate them on demand
## to do this we need a minheap that will always add the new potential minimum after we delete the minimum
## aka we dont care to the sum of big subarrays for small input values

def rangesum_of_sorted_subqueries_sum(nums,n,left,right):
    minHeap=[(n,i) for i,n in enumerate(nums)]
    heapq.heapify(minHeap)
    i=1
    res=0

    while i<=right:
        val,index=heapq.heappop(minHeap)
        if i>=left:
            res+=val
        if index+1<n:
            heapq.heappush(minHeap,(val+nums[index+1],index+1))
        i+=1

    return res

# print(rangesum_of_sorted_subqueries_sum([1,2,3,4],4,1,5))
# print(rangesum_of_sorted_subqueries_sum([1,2,3,4],4,3,4))
# print(rangesum_of_sorted_subqueries_sum([1,2,3,4],4,1,10))


## we want the character that is typed the most to be the easiest to type
from collections import Counter
import math
def min_taps_to_type_word2(word):
    count=Counter(word)
    i=1
    taps=0

    for k,v in sorted(count.items(),key=lambda x:x[1],reverse=True):
        taps+=math.ceil(i/8)*v
        i+=1

    return taps



# print(min_taps_to_type_word2("abcde"))
# print(min_taps_to_type_word2("xyzxyzxyzxyz"))
# print(min_taps_to_type_word2( "aabbccddeeffgghhiiiiii"))


def spiral_matrix3(rows,cols,rStart,cStart):
    res=[]
    steps=1
    cur_row,cur_col=rStart,cStart
    res.append([cur_row,cur_col])

    while len(res)<rows*cols:
        ## move right
        for i in range(cur_col+1,min(cur_col+1+steps,cols)):
            if 0<=cur_row<rows and 0<=i<cols:
                res.append([cur_row,i])
        cur_col+=steps
        print(steps)
        ## move down
        for i in range(cur_row+1,min(cur_row+1+steps,rows)):
            if 0<=cur_row<rows and 0<=i<cols:
                res.append([i,cur_col])
        cur_row+=steps

        ## move left
        steps+=1
        for i in range(cur_col-1,max(-1,cur_col-steps-1),-1):
            if 0<=cur_row<rows and 0<=i<cols:
                res.append([cur_row,i])
        cur_col-=steps
        
        ## move up
        for i in range(cur_row-1,max(cur_row-steps-1,-1),-1):
            if 0<=cur_row<rows and 0<=i<cols:
               res.append([i,cur_col])
        cur_row-=steps
        steps+=1

    return res

# print(spiral_matrix3(1,4,0,0))
# print(spiral_matrix3(5,6,1,4))

def combation_sum_2(candidates,target):
    dp=[[None]*(target+1) for _ in range(len(candidates))]
    candidates.sort()
    def dfs(i,k):
        if k==0:return [[]]
        if i>=len(candidates):return None
        if dp[i][k] is not None:return dp[i][k]
        res=[]

        ## take 
        take=[]
        if k-candidates[i]>=0:
            take=dfs(i+1,k-candidates[i])
            if take is not None:
                for t in take:
                    res.append(t+[candidates[i]])
        
        ## skip
        prev_num=candidates[i]
        j=i+1
        while j<len(candidates) and candidates[j]==prev_num:
            j+=1
        
        skip=dfs(j,k)
        if skip is not None:
            for s in skip:
                    res.append(s)
        dp[i][k]=res
        return res
    return dfs(0,target)

print(combation_sum_2([10,1,2,7,6,1,5],8))
print(combation_sum_2([2,5,2,1,2],5))






