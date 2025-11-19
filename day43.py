def lc2154(nums,original):
    nums=set(nums)
    cur=original
    while cur in nums:
        cur*=2
    return cur

# print(lc2154([5,3,6,1,12],3))
# print(lc2154([2,7,9],4))

def lc74(matrix,target):
    t,b=0,len(matrix)

    ## step 1 : binary search by rows
    while t<=b:
        m=(t+b)//2

        first,last=matrix[m][0],matrix[m][-1]
        if first<=target<=last:break
        elif target>last:
            t=m+1
        else:
            b=m-1
    
    ## step 2 : binary search the row
    if not(matrix[m][0]<=target<=matrix[m][-1]):return False

    l,r=0,len(matrix[0])
    while l<=r:
        m2=(l+r)//2
        if matrix[m][m2]==target:return True
        elif matrix[m][m2]>target:r=m2-1
        else:l=m2+1
    if matrix[m][m2]!=target:return False
    else:return True

# print(lc74([[1,3,5,7],[10,11,16,20],[23,30,34,60]],3))
# print(lc74([[1,3,5,7],[10,11,16,20],[23,30,34,60]],13))

def lc128(nums):
    nums=set(nums)
    visited={}  ## maps each element with longest subsequece from it
    def getLongest(n):
        tmpN=n
        length=0
        while n in nums:
            n+=1
            if n in visited:
                length=visited
                break
            visited[n]=float('-inf')  ## to avoid reusing a node that was found in middle of path and thus wont give better result
        length=n-tmpN
        visited[tmpN]=length
        return length
    
    res=1
    for n in nums:
        if n in visited:
            continue
        res=max(res,getLongest(n))
    return res

# print(lc128([100,4,200,1,3,2]))
# print(lc128([0,3,7,2,5,8,4,6,0,1]))
# print(lc128([1,0,1,2]))

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors

def lc133(adjlist):
    n=len(adjlist)
    created=[None]*(n+1)

    for i,a in enumerate(adjlist):
        i2=i+1
        if not created[i2]:created[i2]=Node(i2)
        curNode=created[n]
        for n in a:
            if not created[n]:
                newNode=Node(n)
                created[n]=newNode
            else:
                newNode=created[n]
            if not curNode.neighboors:
                curNode.neighboors=[]
            curNode.neighboors.append(newNode)
    return created[0]

def lc647(s):
    res=len(s)
    ## odd length
    for i,c in enumerate(s):
        l,r=i-1,i+1
        while l>=0 and r<len(s):
            if s[l]!=s[r]:break
            print(l,r)
            res+=1
            l-=1
            r+=1
    ## even length
    for j in range(1,len(s)):
        l,r=j-1,j
        while l>=0 and r<len(s):
            if s[l]!=s[r]:break
            res+=1
            l-=1
            r+=1
    return res

# print(lc647("abc"))
# print(lc647("aaa"))

def lc139(s,wordDict):
    wordDict=set(wordDict)
    dp=[None]*len(s)

    def dfs(i):
        if i==len(s):return True
        if dp[i]!=None:return dp[i]
        curS=""
        for r in range(i,len(s)):
            curS+=s[r]
            if curS in wordDict and dfs(r+1):return True
            
        dp[i]=False
        return dp[i]

    return dfs(0)

# print(lc139("leetcode",["leet","code"]))
# print(lc139("applepenapple",["apple","pen"]))
# print(lc139( "catsandog",["cats","dog","sand","and","cat"]))

def lc141(head):
    cur=head
    visit=set()
    while cur:
        if cur in visit:return True
        visit.add(cur)
        cur=cur.next
    return False

def lc268(nums):
    ## mark visited nums by making the number at their index negative (except for zero and len(nums))
    isNAvailable=False
    for n in nums:
        n=abs(n) if n!=-10**5 else 0
        if n==len(nums):isNAvailable=True
        elif nums[n]==0:
            nums[n]=-10**5
        else:
            nums[n]*=-1
    if not isNAvailable:return len(nums)
    
    for i in range(len(nums)):
        if nums[i]>=0:return i
    
# print(lc268([3,0,1]))
# print(lc268([0,1]))
# print(lc268([9,6,4,2,3,5,7,0,1]))

import math
class DoublyLinkedListNode:
    def __init__(self, val=0, next=None,prev=None):
        self.val = val
        self.next = next 
        self.prev = prev
# def reorderList(head):
#     if not head or not head.next:return head
#     ## step 1: build doubly linked list
#     newHead=DoublyLinkedListNode(1)
#     newHead.next=DoublyLinkedListNode(head.next.val)
#     cur=head.next

#     newCur=newHead.next
#     prev=newHead 
#     length=0
#     while cur:
#         newCur.next=DoublyLinkedListNode(cur.next.val) if cur.next else None
#         newCur.prev=prev
#         prev=newCur
#         cur=cur.next
#         newCur=newCur.next
#         length+=1

#     ## reverse
#     tail=prev
#     left=newHead
#     right=tail

#     for _ in range(math.ceil(length/2)-1):
#         tmpLeft=left.next

#         right.next=left.next
#         left.next=right
#         left=tmpLeft
#         right=right.prev
#     return newHead




        
        

            






