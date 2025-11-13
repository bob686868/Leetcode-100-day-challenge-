def lc3228(s):
    numOnes,steps=0,0
    for i in range(len(s)-1):
        c=s[i]
        if c!="1":continue
        numOnes+=1
        if s[i+1]=="0":
            steps+=numOnes
    return steps

# print(lc3228("1001101"))
# print(lc3228("00111"))

def lc32(s):
    opened,closed=0,0
    res=0

    ## step 1: forwad traversal
    for c in s:
        if c==")":
            closed+=1
            if closed>opened:
                opened,closed=0,0
        else:
            opened+=1
        if closed==opened:
            res=max(res,2*opened)

    ## step 2 :backward traversal

    closed,opened=0,0
    for i in range(len(s)-1,-1,-1):
        c=s[i]
        if c=="(":
            opened+=1
            if opened>closed:
                opened,closed=0,0
        else:
            closed+=1
        if opened==closed:   
            res=max(res,2*opened)
    return res

# print(lc32("(()"))
# print(lc32(")()())"))

def lc33(arr,val):
    def searchForPivot(arr):
        l,r=0,len(arr)-1
        while l<=r:
            m=(l+r)//2
            if arr[m-1]<arr[m]>arr[m+1]:
                return m
            elif arr[m]>arr[-1]:
                l=m+1
            else:
                r=m
        return m
                
    pivot=searchForPivot(arr) if arr[-1]<arr[0] else -1
    ## step 2 : choose the range 
    ## if smaller then last element ( greatest element in the right sorted portion) , then look at the left
    ## else look at the right 

    pivotValue=arr[pivot]
    if pivot!=-1 and pivotValue==val:return pivot
    if pivot==-1:
        l,r=0,len(arr)-1
    elif val>arr[-1]:
        l,r=0,pivot-1
    else:
        l,r=pivot+1,len(arr)-1
    ## step 3 : binary search in that chosen range
    print(l,r)
    while l<=r:
        m=(l+r)//2
        if arr[m] == val:
            return m
        elif arr[m]>val:
            r=m-1
        else:
            l=m+1
    return -1

# print(lc33([4,5,6,7,0,1,2],0))
# print(lc33([1],1))
# print(lc33([1,3],1))

def lc34(nums,target):
    ## first occurence
    l,r=0,len(nums)-1
    firstIndex,secondIndex=-1,-1

    while l<=r:
        m=(l+r)//2
        if nums[m]<target:
            l=m+1
        elif nums[m]>target:
            r=m-1
        else:
            firstIndex=m
            r=m-1
    l,r=0,len(nums)-1
    while l<=r:
        m=(l+r)//2
        if nums[m]<target:
            l=m+1
        elif nums[m]>target:
            r=m-1
        else:
            secondIndex=m
            l=m+1
    return [firstIndex,secondIndex]

# print(lc34([5,7,7,8,8,10],8))
# print(lc34([5,7,7,8,8,10],6))

def lc35(nums,target):
    if nums[-1]<target:return len(nums)
    l,r=0,len(nums)-1
    m=(l+r)//2
    while l<r:
        if nums[m]>target:
            r=m
        elif nums[m]<target:
            l=m+1
        else:
            return m
        m=(l+r)//2

    return m

# print(lc35([1,3,5,6],5))
# print(lc35([1,3,5,6],2))
# print(lc35([1,3,5,6],7))

from collections import defaultdict
def lc36(board):
    boxes=defaultdict(set)
    cols=[set() for _ in range(9)]

    for r in range(9):
        curRow=set()
        for c in range(9):
            val=board[r][c]
            if val==".":continue
            if val in curRow:
                return False
            curRow.add(val)
            if val in cols[c]:
                return False
            cols[c].add(val)
            boxR,boxC=r//3,c//3
            if val in boxes[(boxR,boxC)]:
                return False
            boxes[(boxR,boxC)].add(val)
    return True
            


# print(lc36([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]))
# print(lc36([["8","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]))
        
def lc37(board):
    rows=[set() for _ in range(9)]
    cols=[set() for _ in range(9)]
    boxes=defaultdict(set)
    
    def addVals(val,r,c):
        boxR,boxC=r//3,c//3
        rows[r].add(val)
        cols[c].add(val)
        boxes[(boxR,boxC)].add(val)
    def removeVals(val,r,c):
        boxR,boxC=r//3,c//3
        rows[r].remove(val)
        cols[c].remove(val)
        boxes[(boxR,boxC)].remove(val)

    def backtrack(r,c):
        if c>8:return backtrack(r+1,0)
        if r>8:return True
        ## check if there is incompleted value in curRow
        for j in range(c,9):
            boxR,boxC=r//3,j//3

            val=board[r][j]
            if val==".":
                for v in range(1,10):
                    if v not in rows[r] and v not in cols[j] and v not in boxes[(boxR,boxC)]:
                        
                        addVals(v,r,j)
                        board[r][j]=str(v)
                        if backtrack(r,j+1):return True
                        board[r][j]="."
                        removeVals(v,r,j)
                return False

        ## first row was already filled

        for r in range(r+1,9):
            for j in range(9):
                val=board[r][j]
                if val=='.':
                    boxR,boxC=r//3,j//3
                    for v in range(1,10):
                        if v not in rows[r] and v not in cols[j] and v not in boxes[(boxR,boxC)]:
                            addVals(v,r,j)
                            board[r][j]=str(v)
                            if backtrack(r,j+1):return True
                            board[r][j]="."
                            removeVals(v,r,j)
                    return False
        return True
    
    for r in range(9):
        for c in range(9):
            val=board[r][c]
            if val !='.':
                val=int(val)
                rows[r].add(val)
                cols[c].add(val)
                boxR,boxC=r//3,c//3
                boxes[(boxR,boxC)].add(val)

    backtrack(0,0)
    return board

# print(lc37([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]))

def lc38(n):

    def countAndSay(n):
        if n==1:return "1"

        nextS=countAndSay(n-1)
        curChar=nextS[0]
        curCount=0
        rle=[]

        for c in nextS:
            if c ==curChar:
                curCount+=1
            else:
                rle.append(str(curCount))
                rle.append(curChar)
                curChar=c
                curCount=1
        rle.append(str(curCount))
        rle.append(curChar)
        print(n,rle)
        return ''.join(rle)
    return countAndSay(n)

# print(lc38(4))
# print(lc38(1))

def lc39(candidates,target):
    candidates=list(set(candidates))
    res=[]

    def dfs(i,newTarget,comb):
        if newTarget==0:
            res.append(comb)
            return 
        if i==len(candidates):return 

        ## take 
        if newTarget -candidates[i]>=0:
            comb.append(candidates[i])
            dfs(i,newTarget-candidates[i],comb.copy())
            comb.pop()
        ## skip
        dfs(i+1,newTarget,comb.copy())

    dfs(0,target,[])
    return res

# print(lc39([2,3,6,7],7))
# print(lc39([2,3,5],8))