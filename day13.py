def searchRotatedSortedArray(arr, val) :
        ## step 1 : search for the pivot
    if len(arr)==1:return 0 if arr[0] ==val else -1  
    def searchForPivot(arr):
        l,r=0,len(arr)-1
        while l<r:
            m=(l+r)//2
            if m==0 :return 0
            if arr[m-1]<=arr[m]>arr[m+1]:
                return m
            elif arr[m]>arr[-1]:
                l=m+1
            else:
                r=m-1
        return m 
                
    pivot=searchForPivot(arr) if arr[-1]<arr[0] else 0 ## if array is not rotated then the pivot should be last element 
    print(pivot)
    ## step 2 : choose the range 
    ## if smaller then last element ( greatest element in the right sorted portion) , then look at the left
    ## else look at the right 

    if arr[-1]==val:return len(arr)-1
    elif arr[-1]<val:
        l,r=0,pivot-1
    else:
        l,r=pivot,len(arr)-1
    ## step 3 : binary search in that chosen range
    if r<0 :r=0
    while l<=r:
        m=(l+r)//2
        if arr[m] == val:
            return m
        elif arr[m]>val:
            r=m-1
        else:
            l=m+1
    return -1

# print(searchRotatedSortedArray([1,3],1))
# print(searchRotatedSortedArray([2,5,6,0,0,1,2],3))

def checkIfThereIsValidPartitionForTheArray(arr):
        
        dp=[-1 for _ in range(len(arr))]

        def dfs(i):
            if i ==len(arr):return True
            if dp[i]!=-1:return dp[i]
            if i==len(arr)-1:return False

            ## 2 elements
            if arr[i]==arr[i+1]:dp[i]=dfs(i+2)
            if dp[i]==True:return True
            ## 3 elements
            if i==len(arr)-2:return dp[i]==True

            if arr[i]==arr[i+1]==arr[i+2]:
                dp[i]=dfs(i+3)
            if dp[i]==True:return True

            elif arr[i]==arr[i+1]-1==arr[i+2]-2:
                dp[i]=dfs(i+3)
            return dp[i]==True

        return dfs(0)

# print(checkIfThereIsValidPartitionForTheArray([4,4,4,5,6]))
# print(checkIfThereIsValidPartitionForTheArray([1,1,1,2]))

def maxLengthOfPairChain(pairs):
    pairs.sort(key=lambda p:p[1])
    score=0
    prevEnd=float('-inf')
    for s,e in pairs:
        if s>prevEnd:
            score+=1
            prevEnd=e
    return score

# print(maxLengthOfPairChain([[1,2],[2,3],[3,4]]))
# print(maxLengthOfPairChain([[1,2],[7,8],[4,5]]))

def minPenaltyForShop(customers):
    enteringAfterI=[0 for _ in range(len(customers)+1)] ## if we closed at last index -> entering = 0
    notEnteringBeforeI=[0 for _ in range(len(customers)+1)] ## if we closed at first index -> leaving = 0
    result=float('inf')
    index=0

    enteringAfterI[-2]=1 if customers[-1]=='Y' else 0
    for i in range(len(customers)-2,-1,-1):
        incrementer=1 if customers[i] == 'Y' else 0
        enteringAfterI[i]=enteringAfterI[i+1]+incrementer

    notEnteringBeforeI[1]=1 if customers[0]=='N' else 0
    for j in range(2,len(customers)+1):
        incrementer=1 if customers[j-1]=='N' else 0 
        notEnteringBeforeI[j]=notEnteringBeforeI[j-1]+incrementer

    print(enteringAfterI)
    print(notEnteringBeforeI)
    for k in range(len(customers)+1):
        penalty=enteringAfterI[k]+notEnteringBeforeI[k]
        if penalty<result:
            result=penalty
            index=k

    return index

# print(minPenaltyForShop("YYNY"))
# print(minPenaltyForShop("YYYY"))
# print(minPenaltyForShop("NNNNN"))

def extraCharactersInAString(s,words):
    dp=[float('inf') for _ in range(len(s)+1)]
    dp[-1]=0

    def dfs(i):
        if dp[i]!=float('inf'):
            return dp[i]
        for w in words:
            if s.startswith(w,i):
                dp[i]=min(dp[i],dfs(i+len(w)))
        dp[i]=min(dp[i],1+dfs(i+1))
        return dp[i]
    return dfs(0)

# print(extraCharactersInAString("leetscode",["leet","code","leetcode"]))
# print(extraCharactersInAString("sayhelloworld",["hello","world"]))

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def splitLinkedList(elements,k):
        n=0
        cur=elements
        while cur!=None:
            n+=1
            cur=cur.next
        elementPerPart=n//k
        result=[]
        extras=n%k

        i=0
        pointer=elements
        while i<n:
            limit=elementPerPart + (1 if extras>0 else 0)
            if limit>0:
                root=pointer
                pointer=pointer.next
                limit-=1
                i+=1
            extras-=1
            cur=root
            prev=pointer
            for _ in range(limit):
                cur.next=pointer
                i+=1
                cur=cur.next
                prev=pointer
                pointer=pointer.next
            if prev:prev.next=None
            result.append(root)
        while len(result)<k:
            k.append(None)
        return result

# print(splitLinkedList([1,2,3],5))
# print(splitLinkedList([1,2,3,4,5,6,7,8,9,10],3))

from collections import Counter
def minimumDeletionsToMakeCharFreqUnique(chars):
    counter=Counter(chars)
    counts=set()
    result=0
    for k,v in counter.items():
        initalCount=v
        count=v
        while count in counts and count>=0:
            count-=1
        counts.add(count)
        if count==-1:return -1 
        result+=(initalCount-count)
    return result

print(minimumDeletionsToMakeCharFreqUnique("aab"))
print(minimumDeletionsToMakeCharFreqUnique("aaabbbcc"))
print(minimumDeletionsToMakeCharFreqUnique("ceabaacb"))
    