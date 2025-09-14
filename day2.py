class UnionFind: ## every index in the array is an element 
    def __init__(self,n):
        self.parent=[i for i in range(n)]
        self.rank=[1 for _ in range(n)]

    def find(self,p1):
        parent=self.parent

        while p1!=parent[p1]:
            p1=parent[p1]
            parent[p1]=parent[parent[p1]]

        return p1
    
    def union(self,p1,p2):
        p1,p2=self.find(p1),self.find(p2)
        rank=self.rank
        if p1==p2:
            return False
        elif rank[p1]>rank[p2]:
            self.parent[p2]=p1
        else:
            self.parent[p1]=p2
        return True


## if an email appears in         
def accountMerge(accounts):  
    uf=UnionFind(len(accounts))
    emailToAccount={}
    components=len(accounts)

    for i,account in enumerate(accounts):
        for j,email in enumerate(account):
            if j==0:continue
            if emailToAccount.get(email,-1)==-1:
                 emailToAccount[email]=i
            else:
                if uf.union(emailToAccount[email],i):components -= 1
    
    indexInParentToIndexInResult={}
    result=[]
    for email,i in emailToAccount.items():
        parentI=uf.find(i)
        name=accounts[parentI][0]
        if parentI in indexInParentToIndexInResult:
            result[indexInParentToIndexInResult[parentI]].append(email)

        else:
            indexInParentToIndexInResult[parentI]=len(result)
            result.append([name,email])
        

    ## sort result
    for i,r in enumerate(result):
        name=r[0]
        emails=r[1:len(r)]
        emails.sort()
        result[i]=[name]+emails

    return result    


            

# print(accountMerge([["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]))
# print(accountMerge([["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]]))
# print(accountMerge([["David","David0@m.co","David1@m.co"],["David","David3@m.co","David4@m.co"],["David","David4@m.co","David5@m.co"],["David","David2@m.co","David3@m.co"],["David","David1@m.co","David2@m.co"]]))

def sortAnArray(array):

    ## split array until one element remains 
    ## then gradually build the sorted array by 
    ## merging the 2 splitted subarrays
    def mergeSort(l,r):
        if l==r:return [array[l]]

        m=(l+r)//2
        arr1=mergeSort(l,m)
        arr2=mergeSort(m+1,r)

        i,j=0,0
        result=[]
        while i<len(arr1) and j<len(arr2):
            if arr1[i]<arr2[j]:
                result.append(arr1[i])
                i+=1
            else:
                result.append(arr2[j])
                j+=1

        while i<len(arr1):
            result.append(arr1[i])
            i+=1
        while j<len(arr2):
            result.append(arr2[j])
            j+=1
        return result
            

    return mergeSort(0,len(array)-1)

# print(sortAnArray([1,5,6,3,4,8,9,2]))


def findPeakElement(nums):
    l,r=0,len(nums)-1

    ##  if a neighboor element n is greater then cur element , 
    ##  then , since edge elements are considered -infinity,
    ##  its guaranteed that there is a peak element somewhere in the 
    ##  direction of n 
    while l<r:
        m=(l+r)//2
        prev=nums[m-1] if m!=0 else float('-inf') 
        next=nums[m+1] if m!=len(nums) else float('-inf') 
        if prev>=nums[m]:
            r=m-1
        elif next>=nums[m]:
            l=m+1
        else :
            return m
    return l

# print(findPeakElement([1,2,3,1]))
# print(findPeakElement([1,2,1,3,5,6,4]))
from collections import deque

 
def checkBinaryTreeComplete(root):
    
    q=deque()
    q.append(root)
    shouldEnd=False

    ## keep adding children progressively until a "gap" appears (aka a child is missing)
    ## if a node has a children after the gap appears then return False
    ## also return False if a node has a right child but no left child 
     
    while q:
        node=q.popleft()
        if (node.left or node.right) and shouldEnd:return False
        elif not node.left and node.right:return False
        elif (not node.left and not node.right):
            if node.left:q.append(node.left)
            shouldEnd=True
            continue
        elif not node.left or shouldEnd==True:
            return False
        q.append(node.left)
        q.append(node.right)

    return True 
    
