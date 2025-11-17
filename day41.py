def lc1437(nums,k):
    count=k+1
    for n in nums:
        if n==1:
            if count<k:return False
            count=0
        else:
            count+=1
    return True

# print(lc1437([1,0,0,0,1,0,0,1],2))
# print(lc1437([1,0,0,1,0,1],2))

def lc61(head,k):
            if  not head:return head
            cur=head
            length=0
            while cur:
                cur=cur.next
                length+=1
            k%=length
            if k==0:return head
            fast,slow=head,head
            for _ in range(k+1):
                fast=fast.next

            while fast:
                fast=fast.next
                slow=slow.next
            tmp=slow.next
            newHead=slow.next
            slow.next=None
            while tmp.next:
                tmp=tmp.next
            tmp.next=head
            return newHead

def lc62(obstacleGrid):
     if obstacleGrid[-1][-1]==1 or obstacleGrid[0][0]==1:return 0
     r,c=len(obstacleGrid),len(obstacleGrid)
     curRow=[0]*c
     curRow[-1]=1    
     for i in range(r-1,-1,-1):
          for j in range(c-1,-1,-1):
               if (i == r-1 and j ==c-1) :continue
               if obstacleGrid[i][j]==1:
                    curRow[j]=0
                    continue
               bottom=curRow[j]
               right=curRow[j+1] if j+1<c else 0
               curRow[j]=bottom+right
     return curRow[0]
     
# print(lc62([[0,0,0],[0,1,0],[0,0,0]]))
# print(lc62([[0,1],[0,0]]))

def lc63(grid):
     r,c=len(grid),len(grid[0])
     curRow=[0]*c
     curRow[-1]=grid[-1][-1]
     for i in range(r-1,-1,-1):
          for j in range(c-1,-1,-1):
               if j==c-1 and i==r-1:continue
               right=curRow[j+1] if j+1<c else float('inf')
               bottom=curRow[j] if i!=r-1 else float('inf')
               curRow[j]=grid[i][j]+min(right,bottom)
     return curRow[0]

# print(lc63([[1,3,1],[1,5,1],[4,2,1]]))
# print(lc63([[1,2,3],[4,5,6]]))

def lc65(s):
    nums = [str(i) for i in range(10)]
    exponent = ["e", "E"]
    signs = ["+", "-"]
    i = 0
    n = len(s)

    # 1) sign
    if i < n and s[i] in signs:
        i += 1
    elif i < n and s[i] not in nums and s[i] != '.':
        return False

    # 2) integer part
    hasNumBeforeDot = False
    while i < n and s[i] in nums:
        hasNumBeforeDot = True
        i += 1
    
    # 3) decimal part (no exponent yet)
    hasNumAfterDot = False
    if i < n and s[i] == ".":
        i += 1
        while i < n and s[i] in nums:
            hasNumAfterDot = True
            i += 1

    # If neither before nor after dot had digits, invalid
    if not hasNumBeforeDot and not hasNumAfterDot:
        return False

    # 4) exponent part
    if i < n and s[i] in exponent:
        i += 1
        if i < n and s[i] in signs:
            i += 1
        if i == n:
            return False  # must have digits after exponent
        hasExponentNum = False
        while i < n and s[i] in nums:
            hasExponentNum = True
            i += 1
        if not hasExponentNum:
            return False

    return i == n

     
# print(lc65(".0e7"))
# print(lc65( "--6"))
# print(lc65("95a54e53"))

def lc66(digits):
     carry=0
     if digits[-1]!=9:
          digits[-1]+=1
          return digits
     digits[-1]=0
     carry=1
     for i in range(len(digits)-2,-1,-1):
          if carry==0:return digits
          newNum=digits[i]+carry
          carry=newNum//10
          digits[i]=newNum%10
     if carry:
          digits.insert(0,carry)
     return digits

     
# print(lc66([1,2,3]))
# print(lc66([1,9,9]))

def lc67(a,b):
     res=[]
     carry=0

     for i in range(max(len(a),len(b))):
         i1=len(a)-1-i
         i2=len(b)-1-i
         n1=int(a[i1]) if i1>-1 else 0
         n2=int(b[i2]) if i2>-1 else 0
         res.append(str((n1+n2+carry)%2))
         carry=(n1+n2+carry)//2
     if carry:res.append("1")
     return ''.join(res[::-1])

# print(lc67("11","1"))
# print(lc67("1010","1011"))

def lc69(x):
     l,r=0,x
     res=0
     
     while l<=r:
          m=(l+r)//2
          if m**2<x:
               res=m
               l=m+1
          elif m**2>x:
               r=m-1
          else:
               return m
     return res

# print(lc69(4))     
# print(lc69(7))    

def lc70(n):
     n1,n2=1,1
     for _ in range(n-1):
          tmp=n2
          n2+=n1
          n1=tmp
     return n2
     
# print(lc70(2))
# print(lc70(3))

def lc68(words,maxWidth):
    res=[]
    l=0
    curLen=0
    for r,w in enumerate(words):
        incrementer=1 if l!=r else 0
        if len(w)+curLen+incrementer<=maxWidth:
            curLen+=len(w)+incrementer
        else:
            subRes=[]
            numWords=r-l
            extraSpaces=maxWidth-curLen
            if numWords==1:
                res.append("".join([words[l]," "*extraSpaces]))
                curLen=len(w)
                l=r
                continue
            remainder=extraSpaces%(numWords-1)
            for i in range(numWords):
                subRes.append(words[l+i])
                if i==numWords-1:
                    continue
                incrementer=1 if remainder > 0 else 0
                subRes.append(" "*(extraSpaces//(numWords-1)+incrementer+1))
                remainder-=1
            res.append(''.join(subRes))
            curLen=len(w)
            l=r
    
    ## last words
    numWords=len(words)-l
    extraSpaces=maxWidth-curLen
    if numWords == 1:
        res.append("".join([words[l]," "*extraSpaces]))

    else:
        subRes=[]
        lenSubRes=-1
        for i in range(numWords):
            lenSubRes+=len(words[l+i])+1
            subRes.append(words[l+i])
            if i!=numWords-1:
                subRes.append(" ")
        subRes.append(' '*(maxWidth-lenSubRes))
        res.append(''.join(subRes))
    return res
    
    
     
# print(lc68(["This", "is", "an", "example", "of", "text", "justification."],16))
# print(lc68(["What","must","be","acknowledgment","shall","be"],16))
# print(lc68(["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"],20))

