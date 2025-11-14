from collections import defaultdict

def lc2536(n,queries):
    endpoint=defaultdict(int)
    for r1,c1,r2,c2 in queries:
        endpoint[(r1,c1)]+=1
        endpoint[(r2+1,c2+1)]+=1
        endpoint[(r1,c2+1)]-=1
        endpoint[(r2+1,c1)]-=1
    
    increments=[[0]*n for _ in range(n+1)] ## extra row to avoid edge cases

    increments[1][0]=endpoint[(0,0)]
    ## fill other rows
    for i in range(1,n+1):
        for j in range(n):
            increments[i][j]=increments[i][j-1]+endpoint[(i-1,j)]
    
    ## fill the actual matrix using the same memory of increments table
    for i in range(1,n+1):
        for j in range(n):
            increments[i][j]+=increments[i-1][j]
    return increments[1:][:]

# print(lc2536(3,[[1,1,2,2],[0,0,1,1]]))
# print(lc2536(2,[[0,0,1,1]]))

def jumpGame2(jumps):
    n=len(jumps)
    dp=[float('inf')]*n
    dp[-1]=0

    for i in range(n-2,-1,-1):
        jump=jumps[i]
        for j in range(i+1,min(jump+i+1,n)):
            dp[i]=min(dp[i],1+dp[j])
    return dp[0]

# print(jumpGame2([2,3,1,1,4]))
# print(jumpGame2([2,3,0,1,4]))

import math
def lc4(nums1,nums2):
    if len(nums2)<len(nums1):nums1,nums2=nums2,nums1
    
    n1,n2=len(nums1),len(nums2)
    l,r=-1,n1-1

    while l<=r:
        m1=((l+r)//2)                  ## aka we took m1+1 elements from  nums1
        m2=math.ceil((n1+n2)/2)-(m1+2) ## the total number of nums we need to take is ceil((n1+n2)/2)
        arr1Left,arr1Right=(nums1[m1] if m1>=0 else float('-inf')),(nums1[m1+1] if m1+1<n1 else float('inf'))
        arr2Left,arr2Right=(nums2[m2] if m2>=0 else float('-inf')),(nums2[m2+1] if m2+1<n2 else float('inf'))

        if arr1Left>arr2Right:
            r=m1-1
        elif arr2Left>arr1Right:
            l=m1+1
        else:
            if (n1+n2)%2:
                return max(arr1Left,arr2Left)
            
            return (max(arr1Left,arr2Left)+min(arr1Right,arr2Right))/2
        
            
# print(lc4([-10,-9,-8],[1,2]))
# print(lc4([1,3],[2]))
# print(lc4([1,2],[3,4]))

def lc42(height):
    monoDecreasingStack=[(height[0],0)]  ## strictly decreasing
    res=0
    for r in range(1,len(height)):
        rightHeight=height[r]
        while monoDecreasingStack and rightHeight>=monoDecreasingStack[-1][0]:
            midHeight,_=monoDecreasingStack.pop()
            
            leftHeight,i=monoDecreasingStack[-1] if monoDecreasingStack else (-1,r-1)
            res+=((r-i-1)*((min(rightHeight,leftHeight))-midHeight))
        monoDecreasingStack.append((rightHeight,r))
    return res

# print(lc42([0,1,0,2,1,0,1,3,2,1,2,1]))
# print(lc42([4,2,0,3,2,5]))

def lc43(num1,num2):
    if num1=="0" or num2=="0":return "0"

    res=[]
    carry=0

    for i in range(len(num1)-1,-1,-1):
        for j in range(len(num2)-1,-1,-1):
            exponent=(len(num1)+len(num2)-2)-i-j
            totalSum=int(num1[i])*int(num2[j])
            if len(res)<exponent+1:res.append(0)
            res[exponent]+=(totalSum+carry)
            carry=(res[exponent])//10
            res[exponent]%=10
        exponent+=1
        while carry>0:
            if len(res)<exponent+1:res.append(0)
            res[exponent]+=carry
            carry=res[exponent]//10
            res[exponent]%=10
            exponent+=1

    
    for i,r in enumerate(res):
        res[i]=str(res[i])
    return ''.join(res)[::-1]

# print(lc43('123','456'))
# print(lc43('1235','4568'))

def lc44(s,p):
        dp=[[None]*len(p) for _ in range(len(s))]

        def dfs(i,j):
            if j>=len(p) and i>=len(s):return True
            if j>=len(p) and i<len(s):return False
            if i>=len(s) and j<len(p):
                while j<len(p):
                    if p[j]!="*":return False
                    j+=1
                return True
            if dp[i][j]!=None:return dp[i][j]
            if s[i]==p[j] or p[j]=="?":return dfs(i+1,j+1)
            if p[j]=="*":
                dp[i][j]=dfs(i,j+1) or dfs(i+1,j)
                return dp[i][j]
            dp[i][j]=False
            return dp[i][j]

        return dfs(0,0)

# print(lc44("aa","a"))
# print(lc44("aa","*"))
# print(lc44("adceb","*a*b"))

