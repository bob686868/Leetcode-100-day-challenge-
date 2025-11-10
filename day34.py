def lc8(s):
    if s=="":return 0
    i=0
    s=list(s)

    ## ignore whitespaces
    while i<len(s) and s[i]==" ":
        i+=1
    
    if i>=len(s):
        return 0
    ## determine sign
    isPositive=True
    if s[i]=='-':
        isPositive=False
        i+=1
    elif s[i]=="+":
                i+=1
    
    ## read integer
    res=0
    try:
        while i<len(s) and 0<=int(s[i])<=9 :
            res*=10
            res+=int(s[i])
            i+=1
    except:
        if res>2**31-1 and isPositive:
            return 2**31-1
        if res>=2**31 and not isPositive:
            return -2**31
        return res *(1 if isPositive else -1)

    if res>2**31-1 and isPositive:
        return 2**31-1
    if res>=2**31 and not isPositive:
        return -2**31
    return res *(1 if isPositive else -1)

# print(lc8("-91283472332"))
# print(lc8("42"))
# print(lc8(" -042"))
# print(lc8( "1337c0d3"))

import math
def lc9(x):
     if x<0:return False
     if x==0:return True
     tmp=x
     num_digits=0
     while tmp>0:
          tmp//=10
          num_digits+=1
     i=0
     while i<math.ceil(num_digits/2):
          if (x//10**i)%10 != (x//(10**(num_digits-i-1)))%10:
               return False
          i+=1
     return True 

# print(lc9(121))
# print(lc9(-121))

def lc10(s,p):
     dp=[[None]*len(p) for _ in range(len(s))]

     def dfs(i,j):
          if i>=len(s) and j>=len(p):return True
          if j>=len(p):return False
          if i>=len(s):
               j=(j+1 if p[j]!="*" else j)
               while j<len(p) and p[j]=="*":
                    if j==len(p)-1:
                         return True
                    j+=2
                    return False
          if dp[i][j]!=None:return dp[i][j]
          res=False

          if s[i]==p[j]:
               res|=dfs(i+1,j+1)
          if p[j]=='.':
               res|=dfs(i+1,j+1)

          if j+1<len(p) and p[j+1]=="*":
               res|=dfs(i,j+2)

          if p[j]=="*":
               if j>0:
                    if p[j-1]==s[i] or p[j-1]==".":
                         res|=dfs(i+1,j)
                         res|=dfs(i+1,j+1)
               res|=dfs(i,j+1)

          dp[i][j]=res
          return dp[i][j]

     return dfs(0,0)


# print(lc10("mississippi","mis*is*p*."))
# print(lc10("aa","a*"))
# print(lc10("ab",".*"))

def lc11(height):
     res=0
     l,r=0,len(height)-1

     while l<=r:
          if height[l]>height[r]:
               res=max(res,(r-l)*height[r])
               r-=1
          elif height[r]>height[l]:
               res=max(res,(r-l)*height[l])
               l+=1
          else:
               res=max(res,(r-l)*height[l])
               r-=1
               l+=1
     return res

# print(lc11([1,8,6,2,5,4,8,3,7]))
# print(lc11([1,1]))

def lc12(num):
     res=[]
     def get_num_digits(n):
          if n==0:return 1
          numDigits=0
          while n>0:
               numDigits+=1
               n//=10
          return numDigits

     while num>0:
          numDigits=get_num_digits(num)
          firstDigit=(num//(10**(numDigits-1)))%10

          if firstDigit==4:
               if num==4:
                    res.append('IV')
                    num-=4
               elif numDigits ==2:
                    res.append('XL')
                    num-=40
               elif numDigits ==3:
                    res.append('CD')
                    num-=400
          elif firstDigit==9:
               if num==9:
                    res.append('IX')
                    num-=9
               elif numDigits ==2:
                    res.append('XC')
                    num-=90
               elif numDigits ==3:
                    res.append('CM')
                    num-=900
          else:
               if num>=1000:
                    res.append('M')
                    num-=1000
               elif num>=500:
                    res.append('D')
                    num-=500
               elif num>=100:
                    res.append('C')
                    num-=100
               elif num>=50:
                    res.append('L')
                    num-=50
               elif num>=10:
                    res.append('X')
                    num-=10
               elif num>=5:
                    res.append('V')
                    num-=5
               else:
                    res.append('I')
                    num-=1
          
     return ''.join(res)

# print(lc12(3749))          
# print(lc12(58)) 

def lc13(s):
     i=0
     res=0
     symbolToValue={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
     while i<len(s):
          if i+1<len(s) and s[i]=='I' and s[i+1]=="V":
               res+=4
               i+=2
          elif i+1<len(s) and s[i]=='I' and s[i+1]=="X":
               res+=9
               i+=2
          elif i+1<len(s) and s[i]=='X' and s[i+1]=="L":
               res+=40
               i+=2
          elif i+1<len(s) and s[i]=='X' and s[i+1]=="C":
               res+=90
               i+=2
          elif i+1<len(s) and s[i]=='C' and s[i+1]=="D":
               res+=400
               i+=2
          elif i+1<len(s) and s[i]=='C' and s[i+1]=="M":
               res+=900
               i+=2
          else:
               res+=symbolToValue[s[i]]
               i+=1
     return res

# print(lc13("III"))
# print(lc13("LVIII"))

def minOpsToConvertAllElsToZero(nums):
     stack=[]
     ops=0

     for n in nums:
          if not stack or n>stack[-1]:
               stack.append(n)
               ops+=1
          elif stack and n==stack[-1]:
               continue
          else:
               while stack and stack[-1]>n:
                    stack.pop()
               if not stack or stack[-1]<n:
                    ops+=1
               stack.append(n)

     return ops

# print(minOpsToConvertAllElsToZero([0,2]))
# print(minOpsToConvertAllElsToZero([3,1,2,1]))




