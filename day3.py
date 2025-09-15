from math import ceil
class Node :
    def __init__(self,val,isLeaf):
        self.val=val
        self.isLeaf=isLeaf
        self.topLeft=None
        self.topRight=None
        self.bottomLeft=None
        self.bottomRight=None

## simply check if every value is same in a subgrid
## -> if yes then insert this as a leaf
## -> if not then recursively add childrens 

def constructQuadTree(grid):

    def helper(t,b,l,r):
        if l==r or t==b:return grid[t][l]
        isSame=True
        
        firstVal=grid[t][l]
        for i in range(t,b+1):
            for j in range(l,r+1):
                if grid[i][j]!=firstVal:
                    isSame=False
                    break
        if isSame:
            return Node(firstVal,True)
        else:
            node=Node(firstVal,False)
            midRow=(t+b)//2
            midCol=(l+r)//2
            node.topLeft=helper(t,midRow,l,midCol)
            node.topRight=helper(t,midRow,midCol,r)
            node.bottomLeft=helper(midRow,b,l,midCol)
            node.bottomRight=helper(midRow,b,midCol,r)
            return node
    return helper(0,len(grid),0,len(grid))


## store first state (first is greater or less than next) 
## use that state along with difference in index to determine if there is a violation 
## if so , we can safely set our startIndex to the last violation since every subarray that contain the prev element
## will also result in a violation 
def longestTurbulentSubArray(array):
    if len(array)==1:return 1 
    res=1
    startIndex=0
    while startIndex+1<len(array) and array[startIndex]==array[startIndex+1]:
        startIndex+=1
    greaterAtFirst=(array[0]>array[1])  
    for i in range(len(array)-1):
        
        if greaterAtFirst==True:
            if ((i-startIndex)%2==0 and array[i]>array[i+1]) or ((i-startIndex)%2 ==1 and array[i]<array[i+1]):
                continue
        else:
            if ((i-startIndex)%2==1 and array[i]>array[i+1]) or ((i-startIndex)%2 ==0 and array[i]<array[i+1]):
                continue
        while startIndex+1<len(array) and array[startIndex]==array[startIndex+1]:
            startIndex+=1
        res=max(res,i-startIndex+1)
        startIndex=i
        if array[i] > array[i+1]:
            greaterAtFirst=True
        else:
            greaterAtFirst=False
    return max(res,len(array-startIndex))

# print(longestTurbulentSubArray([9,4,2,10,7,8,8,1,9]))
# print(longestTurbulentSubArray([4,8,12,16]))
# print(longestTurbulentSubArray([100]))


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        self.prev=None

def maximumTwinSum(root):
    result=0
    cur=root.next
    prev=root
    length=0
    while cur:
        cur.prev=prev
        prev=cur
        cur=cur.next
        length+=1
    
    lastPointer,firstPointer=prev,root
    i=0
    while i<length//2:
        curSum=lastPointer.val+firstPointer.val
        if curSum>result:
            result=max(result,curSum)
        i+=1
        lastPointer=lastPointer.prev
        firstPointer=firstPointer.next
    
    return result


## the problem boils down to finding a pile of stones that has sum closes to half total sum
## so , we try every possibilty including and excluding stones[i] and use dp to store repeated subproblems
def lastStoneWeight2(stones):
    total=sum(stones)
    target=total//2
    dp=[[0]*(len(stones)) for _ in range(target+1)]

    def helper(curSum,i):
        if curSum >target:return 0
        if i==len(stones):return curSum if curSum <=target else -1
        if dp[curSum][i]!=0:return dp[curSum][i]

        dp[curSum][i]=max(helper(curSum+stones[i],i+1),dp[curSum][i])
        dp[curSum][i]=max(helper(curSum,i+1),dp[curSum][i])

        return dp[curSum][i]
    
    closestSum= helper(0,0)

    return total-2*closestSum
        
        
        
print(lastStoneWeight2([2,7,4,1,8,1]))
print(lastStoneWeight2([31,26,33,21,40]))