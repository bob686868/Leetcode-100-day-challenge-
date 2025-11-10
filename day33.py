from collections import defaultdict
def lc3(s):
    count=defaultdict(int)
    l,r=0,0
    res=1
    while r<len(s):
        count[s[r]]+=1
        if count[s[r]]==1:
            res=max(res,r-l+1)
            r+=1
            continue

        while count[s[r]]>1:
            count[s[l]]-=1
            l+=1
        res=max(res,r-l+1)
        r+=1

    return res

# print(lc3("abcabcbb"))
# print(lc3("bbbbb"))

# def lc4(nums1,nums2):
#     n1,n2=len(nums1),len(nums2)
#     ## use this function to determine num of els in nums2 smaller then the curNum
#     def bisectLeft(nums,target):
#         l,r=0,len(nums)-1

#         while l<r:
#             m=(l+r)//2
#             if nums[m]>target:
#                 r=m-1
#             elif nums[m]<target:
#                 l=m
#             else:
#                 return m
#         return m
#     l,r=0,n1-1
#     while l<=r:
#         m=(l+r)//2
#         i2=bisectLeft(nums1[m])
#         if i2+m>(n1+n2)//2

# print(lc4([1,3],[2]))
# print(lc4([1,2],[3,4]))

def countOpsToMakeZero(num1,num2):
    ops=0
    while num1!=0 and num2!=0:
        ops+=1
        if num1>num2:
            num1-=num2
        else:
            num2-=num1
    return ops

# print(countOpsToMakeZero(2,3))
# print(countOpsToMakeZero(10,10))

def lc5(s):
    start,end=0,0

    ## odd length palindromes
    for i in range(len(s)):
        j=1
        while i+j<len(s) and i-j>-1 and s[i+j] == s[i-j]:
            j+=1
        j-=1
        if 2*j>end-start:
            start,end=i-j,i+j
    
    ## even length palindromes
    for i in range(1,len(s)):
        l,r=i-1,i
        while l>-1 and r<len(s) and s[l]==s[r]:
            l-=1
            r+=1
        r-=1
        l+=1
        if r-l>end-start:
            start,end=l,r

    return s[start:end+1]

# print(lc5("babad"))
# print(lc5("cbbd"))

def lc6(s,numRows):
    if numRows==1:return s
    result=[None]*len(s)
    indexS=0
    for i in range(numRows):
        j=i
        iterationNum=0
        while j<len(s):
            step=(numRows-i-1)*2 if  iterationNum%2 == 0 else i*2
            result[indexS]=s[j]
            j+=step
            iterationNum+=1
            if step>0:
                indexS+=1

    return "".join(result)

# print(lc6("PAYPALISHIRING",3))
# print(lc6("PAYPALISHIRING",4))

def lc7(n):
    tmp=abs(n)
    res=0
    while tmp>0:
        newDig=tmp%10
        if res*10+newDig>2**31-1:
            return 0
        tmp//=10
        res*=10
        res+=newDig
        
    return -1*res if n<0 else res

# print(lc7(123))
# print(lc7(-123))
# print(lc7(120))

def lc8(s):
    i=0
    s=list(s)

    ## ignore whitespaces
    while s[i]=="" and i<len(s):
        i+=1
    
    if i>len(s):
        return 0
    ## determine sign
    isPositive=True
    if s[i]=='-':
        isPositive=False
        i+=1
    
    ## read integer
    res=0
    try:
        while 0<=int(s[i])<=9 and i<len(s):
            res*=10
            res+=int(s[i])
            i+=1
    except:
        if res>2**31-1 and isPositive:
            return 2**31-1
        if res>=2**31 and not isPositive:
            return -2**31
        return res
    return res

print(lc8())
    


