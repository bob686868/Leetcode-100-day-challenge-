import math

## just try each number as the "a" value and check if the needed difference is n**2 where n is an integer
def sum_of_square_numbers(c):

    for i in range(math.floor(c**0.5)+1):
        if (c-i**2)**0.5==math.floor((c-i**2)**0.5): 
            return True
    return False

# print(sum_of_square_numbers(5))
# print(sum_of_square_numbers(3))

## the best time to not get grumpy is when there is maximum customers
## and the minutes are contiguous so we are looking for the max window of size minutes 
def grumpy_bookstore_owner(customers,grumpy,minutes):
    max_l,l=0,0
    cur_sum,max_sum=0,0


    for i in range(minutes):
        cur_sum+=customers[i]*grumpy[i]

    max_sum=cur_sum
    while l+minutes<len(customers):
        cur_sum-=customers[l]*grumpy[l]
        cur_sum+=customers[l+minutes]*grumpy[l+minutes]
        l+=1
        if cur_sum>max_sum:
            max_l=l
            max_sum=cur_sum

    for i in range(max_l,max_l+minutes):
        grumpy[i]=0

    score=0
    for i in range(len(customers)):
            score+=customers[i]*(-grumpy[i]+1)

    return score 

# print(grumpy_bookstore_owner([1,0,1,2,1,1,7,5],[0,1,0,1,0,1,0,1],3))
# print(grumpy_bookstore_owner([1],[0],1))

from collections import defaultdict

## we can save work by computing the number of odd nums in each subarray starting from index 0
## then , we check how many odd nums we need to remove , and add to result the number of subarrays that we 
## can remove (having odd number count = oddCount-k)
def count_number_of_nice_subarrays(nums,k):
    oddCounter=defaultdict(int)
    oddCounter[0]=1
    res=0
    oddCount=0

    for n in nums:
        if n%2:
            oddCount+=1
        res+=oddCounter[oddCount-k]
        oddCounter[oddCount]+=1
    return res

# print(count_number_of_nice_subarrays([1,1,2,1,1],3))
# print(count_number_of_nice_subarrays([2,4,6],1))
# print(count_number_of_nice_subarrays([2,2,2,1,2,2,1,2,2,2],2))

from collections import deque
def max_sliding_window(nums,k):
    result=[]
    q=deque([(nums[0],0)]) ## monotonic decreasing q storing (val,index)


    for i in range(1,k):
        while q and q[-1][0]<=nums[i]:
            q.pop()
        q.append((nums[i],i))
    result.append(q[0][0])

    for i in range(k,len(nums)):
        while q and (q[-1][0]<=nums[i]):
            q.pop()
        if q and q[0][1]<=i-k:
            q.popleft()
        q.append((nums[i],i))
        print(q)
        result.append(q[0][0])
    return result

# print(max_sliding_window([1,3,-1,-3,5,3,6,7],3))
# print(max_sliding_window([1],1))
# print(max_sliding_window([1,3,1,2,0,5],3))
            


    


    


