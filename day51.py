def lc3381(nums,k):
    res=float('-inf')
    minPrefix=[float('inf')]*k
    minPrefix[0]=0
    curSum=0

    for i,n in enumerate(nums):
        curSum+=n
        remainder=(k-i-1)%k
        res=max(res,curSum-minPrefix[remainder])

        minPrefix[remainder]=min(minPrefix[remainder],curSum)
    return res

# print(lc3381([1,2],1))
# print(lc3381( [-1,-2,-3,-4,-5],4))
# print(lc3381([-5,1,2,-3,4],2))

def lc124(root):

        res=float('-inf')
        def dfs(node):
            nonlocal res
            if not node:return 0

            sumLeft=max(dfs(node.left),0)
            sumRight=max(dfs(node.right),0)
            sumAll=node.val+sumLeft+sumRight
        
            res=max(res,sumAll)
            
            return max(sumLeft+node.val,sumRight+node.val,node.val)
        res=max(dfs(root),res)
        return res

# def lc371(a,b):
#      signA=1 if a>0 else -1
#      signB=1 if b>0 else -1
#      a,b=abs(a),abs(b)

#      if (signA==-1 and signB==-1) or \
#      (signA==-1 and abs(a)>b) or \
#      (signB==-1 and abs(b)>a):
#             finalSign=-1
#      else:finalSign =1

#      res=0
#      carry=0
#      i=0
#      while carry or a or b:
#           if carry==-1 and a==0 and b==0:break
#           curSum=signA*(a%10)+signB*(b%10)+carry
#           a//=10
#           b//=10
#           if curSum>=0 or (a != 0 or b != 0):
#                curSum%=10
#           else:curSum=abs(curSum)
#           carry=0

#           if curSum<0 and (a!=0 or b!=0):carry=-1
#           elif curSum>10:
#                curSum%=10
#                carry=1
 
#           res+=((curSum)*10**i)%10
#      return curSum*finalSign

# print(lc371(2,-7))
# print(lc371(2,3))

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import defaultdict
def lc105(preorder,inorder):
        numToIndex=defaultdict(int)
        for i,n in enumerate(inorder):
            numToIndex[n]=i
        
        i=0
        def build(s,e):
            nonlocal i
            if s>e:return None
            if i==len(preorder):return None
            newNode=TreeNode(preorder[i])
            pos=numToIndex[preorder[i]]
            i+=1
            newNode.left=build(s,pos-1)
            newNode.right=build(pos+1,e)
            return newNode
        
        return build(0,len(preorder)-1)
          
