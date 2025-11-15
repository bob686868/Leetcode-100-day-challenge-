from collections import Counter
def lc45(nums):
    counter=Counter(nums)
    res=[]
    perm=[]
    def backtrack(i):
        nonlocal res
        if i==len(nums):
            res.append(perm.copy())
            return 
        for c in list(counter.keys()):
            perm.append(c)
            counter[c]-=1
            if counter[c]==0:counter.pop(c)

            backtrack(i+1)

            if c not in counter:
                counter[c]=0
            counter[c]+=1
            perm.pop()
    
        
    backtrack(0)
    return res
# print(lc45([1,2,3]))
# print(lc45([0,1]))

## lc46 can be solved using the same code as the above code

def lc47(matrix):
    l,r=0,len(matrix)-1
    t,b=l,r
    while l<r:
        for i in range(r-l):
            upLeft=matrix[t][l+i]
            matrix[t][l+i]=matrix[b-i][l]
            matrix[b-i][l]=matrix[b][r-i]
            matrix[b][r-i]=matrix[t+i][r]
            matrix[t+i][r]=upLeft
        l+=1
        r-=1
        t,b=l,r
    return matrix


# print(lc47([[1,2,3],[4,5,6],[7,8,9]]))
# print(lc47([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]))

from collections import defaultdict
def lc49(strs):
    counts={}

    for s in strs:
        sortedS=str(sorted(s))
        if sortedS not in counts:
            counts[sortedS]=[]
        counts[sortedS].append(s)
    return [counts[k] for k in counts]

# print(lc49(["eat","tea","tan","ate","nat","bat"]))
# print(lc49([""]))

import math
def lc50(x,n):
    dp={0:1,1:x}

    def dfs(i):
        if i in dp:return dp[i]
        dp[i]=dfs(math.floor(i/2))*dfs(math.ceil(i/2))
        return dp[i]
    res=dfs(abs(n))
    return round(res if n>0 else 1/res,10)

# print(lc50(2,10))
# print(lc50(2.1,3))
# print(lc50(2,-2))

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def lc25(head,k):
    cur=head
    dummy=ListNode(0)
    length=0
    ## step 1:compute linked list length
    while cur:
        length+=1
        cur=cur.next

    cur=head
    prevTail=dummy
    for _ in range(length//k):
        i=1
        prev=cur
        firstNode=cur
        cur=cur.next
        while i<k:
            nextNode=cur.next
            cur.next=prev
            prev=cur
            cur=nextNode
            i+=1
        curTail=prev
        print(prevTail.val,curTail.val)
        prevTail.next=curTail
        prevTail=firstNode
    prevTail.next=cur

    return dummy.next

from utils import printLinkedList,buildTestLinkedList

# head=buildTestLinkedList(12)
# head=lc25(head,3)
# printLinkedList(head)

def lc1578(colors,neededTime):
    prevTimeNeeded=-1
    time=0
    for i in range(1,len(colors)):
        if colors[i]!=colors[i-1]:
            prevTimeNeeded=-1
            continue
        if prevTimeNeeded==-1:
            prevTimeNeeded=neededTime[i-1]

        time+=min(neededTime[i],prevTimeNeeded)

        prevTimeNeeded=max(prevTimeNeeded,neededTime[i])
    return time

# print(lc1578("abaac",[1,2,3,4,5]))
# print(lc1578("abc",[1,2,3]))
# print(lc1578("aabaa",[1,2,3,4,1]))




