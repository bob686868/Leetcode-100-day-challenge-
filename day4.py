from collections import defaultdict

## try every combination of zeroes and ones that are valid (index in bounds and we dont exceed m,n)
## use memoization to avoid computing repeated subproblems

def onesAndZeroes(strings,m,n): 
    indexToZeroesAndOnesCounts=defaultdict(lambda: [0,0])  ##[zeroes,ones]

    for i in range(len(strings)):
        for l in strings[i]:
            digit=int(l)
            indexToZeroesAndOnesCounts[i][digit]+=1

    dp=[[[0]*(n+1)]*(m+1) for _ in range(len(strings))] ## (i,m,n) 
    def helper(index,zeroesLeft,onesLeft):
        if zeroesLeft<0 or onesLeft<0:return 0
        if index==len(strings):return 0
        zeroes,ones=indexToZeroesAndOnesCounts[index][0],indexToZeroesAndOnesCounts[index][1]
        dp[index][zeroesLeft][onesLeft]=max(1+helper(index+1,zeroesLeft-zeroes,onesLeft-ones),
                                            helper(index+1,zeroesLeft,onesLeft))

        return dp[index][zeroesLeft][onesLeft]

    return helper(0,m,n)

# print(onesAndZeroes(["10","0001","111001","1","0"],5,3))
# print(onesAndZeroes(["10","0","1"],1,1))


def removeDuplicatesFromSortedArray(array):
    j=1
    for i in range(1,len(array)):
        if array[i]!=array[i-1]:
            array[j]=array[i]
            j+=1
    return j

# print(removeDuplicatesFromSortedArray([1,1,2]))
# print(removeDuplicatesFromSortedArray([0,0,1,1,1,2,2,3,3,4]))

## try every possibility but in an intelligent way(binary search) : 
## if we were able to fit the packages , we try smaller capacity and update result to current capacity 
## if not we increase it 
def minCapacityToShipPackagesWithinKDays(weights,days):
    l,r=max(weights),sum(weights)  ## can put l=max(weights) but it is less efficient (O(n) vs O(log(r-l)))
    if days==1:return r
    def doesFit(capacity):
        curDay,curWeight=1,0
        for w in weights:
            if curWeight+w<=capacity:
                curWeight+=w
            else:
                curWeight=w
                curDay+=1
                if curDay>days:
                    return False
        return True

    result=r
    while l<=r:
        m=(l+r)//2

        fitted=doesFit(m)

        if fitted:
            r=m-1
            result=m
        else:
            l=m+1
    return result

# print(minCapacityToShipPackagesWithinKDays([1,2,3,4,5,6,7,8,9,10],5))
# print(minCapacityToShipPackagesWithinKDays([3,2,2,4,1,4],3))
# print(minCapacityToShipPackagesWithinKDays([1,2,3,1,1],3))

## key observation to make is that since every element is repeated twice and 
## since array is sorted , if left subarray has odd length , then it has the single element
def singleElementInList(nums):
            l,r=0,len(nums)-1
            while l<r:
                m=(l+r)//2
                leftSize=m-1 if nums[m]==nums[m-1] else m
                if m==0 or m==len(nums)-1:return nums[m]
                if nums[m-1]!=nums[m]!=nums[m+1]:return nums[m]
                if leftSize % 2 :
                    r=m-1
                else:
                    l=m+1
            return nums[l]

print(singleElementInList([1,1,2,3,3,4,4,8,8]))
print(singleElementInList([3,3,7,7,10,11,11]))
