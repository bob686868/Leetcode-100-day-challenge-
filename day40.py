def lc1513(s):
    res=0
    numOnes=0
    for c in s:
        if c !="1":
            res+=(numOnes)*(numOnes+1)/2
            numOnes=0
        else:
            numOnes+=1
    res+=(numOnes)*(numOnes+1)/2
    return int(res) %(10**9+7)

# print(lc1513("0110111"))
# print(lc1513("101"))
import copy
def nQueens(n):
    takenCols=set()
    mainDiagonals=set()
    secondaryDiagonals=set()
    res=[]
    curBoard=[['.']*n for _ in range(n)]
    def backtrack(r):
        if r==n:
            res.append(copy.deepcopy(curBoard))
            return
        for i in range(n):
            if i in takenCols or i-r in secondaryDiagonals or i+r in mainDiagonals:
                continue
            secondaryDiagonals.add(i-r)
            mainDiagonals.add(i+r)
            takenCols.add(i)
            curBoard[r][i]='Q'
            backtrack(r+1)
            secondaryDiagonals.remove(i-r)
            mainDiagonals.remove(i+r)
            takenCols.remove(i)
            curBoard[r][i]="."


    backtrack(0)
    ## convert each row to a string
    newRes=[]
    for b in res:
        newBoard=[]
        for row in b:
            newBoard.append(''.join(row))
        newRes.append(newBoard.copy())
    return newRes

# print(nQueens(1))
# print(nQueens(4))

def nQueens2(n):
    takenCols=set()
    mainDiagonals=set()
    secondaryDiagonals=set()
    count=0
    def backtrack(r):
        nonlocal count
        if r==n:
            count+=1
            return
        for i in range(n):
            if i in takenCols or i-r in secondaryDiagonals or i+r in mainDiagonals:
                continue
            secondaryDiagonals.add(i-r)
            mainDiagonals.add(i+r)
            takenCols.add(i)
            backtrack(r+1)
            secondaryDiagonals.remove(i-r)
            mainDiagonals.remove(i+r)
            takenCols.remove(i)

    backtrack(0)

    return count

# print(nQueens2(4))
# print(nQueens2(1))

def lc53(nums):
    curSum=0
    res=float('-inf')
    for n in nums:
        curSum+=n
        res=max(res,curSum)
        if curSum<0:curSum=0
    return res


# print(lc53([-2,1,-3,4,-1,2,1,-5,4]))
# print(lc53([5,4,-1,7,8]))

def lc54(matrix):
    res=[]
    l,r=0,len(matrix[0])-1
    t,b=0,len(matrix)-1

    while l<=r and t<=b:
        ## top
        for i in range(l,r+1):
            res.append(matrix[t][i])
        t+=1
        ## right
        if t>b:break
        for i in range(t,b+1):
            res.append(matrix[i][r])
        r-=1
        if l>r:break
        ## bottom
        for i in range(r,l-1,-1):
            res.append(matrix[b][i])
        b-=1
        if t>b:break
        ## left
        for i in range(b,t-1,-1):
            res.append(matrix[i][l])
        l+=1
    return res

# print(lc54([[1,2,3],[4,5,6],[7,8,9]]))
# print(lc54([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))

def lc55(nums):
    lastReachable=len(nums)-1

    for i in range(len(nums)-2,-1,-1):
        if i+nums[i]>=lastReachable:
            lastReachable=i
    return lastReachable==0

# print(lc55([2,3,1,1,4]))
# print(lc55([3,2,1,0,4]))

def lc56(intervals):
    intervals.sort()
    print(intervals)
    res=[]
    prevStart,prevEnd=intervals[0][0],intervals[0][0]

    for s,e in intervals:
        if s<=prevEnd:
            prevEnd=max(prevEnd,e)
        else:
            res.append([prevStart,prevEnd])
            prevStart=s
            prevEnd=e
    res.append([prevStart,prevEnd])
    return res

# print(lc56([[1,3],[2,6],[8,10],[15,18]]))
# print(lc56([[1,4],[2,3]]))
# print(lc56([[1,2],[4,5]]))

def lc58(s):
    res=0
    s=s.strip()

    for i in range(len(s)-1,-1,-1):
        if s[i]!=" ":
            res+=1
        else:
            break
    return res

# print(lc58("Hello World"))
# print(lc58("   fly me   to   the moon  "))

def lc59(intervals,newInterval):
        if not intervals:return [newInterval]
        res=[]
        newS,newE=newInterval
        i=-1
        hasInserted=False

        for s,e in intervals:
            i+=1
            if newE<s:
                hasInserted=True
                res.append([newS,newE])
                res.append([s,e])
                break
            elif newS>e:res.append([s,e])
            else:
                hasInserted=True

                prevStart,prevEnd=min(s,newS),max(e,newE)
                i=len(res)+1
                while i<len(intervals):
                    nextS=intervals[i][0]
                    if nextS>prevEnd:
                        res.append([prevStart,prevEnd])
                        res.append([nextS,intervals[i][1]])
                        break
                    prevStart,prevEnd=min(prevStart,nextS),max(prevEnd,intervals[i][1])
                    i+=1
                if i==len(intervals):
                    res.append([prevStart,prevEnd])
                break
        i+=1
        while i<len(intervals):
            res.append(intervals[i]) 
            i+=1
        return res if hasInserted else res+[newInterval]   

# print(lc59([[1,3],[6,9]],[2,5]))
# print(lc59([[1,2],[3,5],[6,7],[8,10],[12,16]],[4,8]))

def lc60(n,k):
    tmpN=n
    perm=""
    choices=[str(i) for i in range(1,n+1)]
    factorial=[1,1]
    for i in range(2,n+1):
        factorial.append(factorial[-1]*i)
    def dfs(i):
        nonlocal perm
        nonlocal tmpN
        if len(perm)==n:
            return 
        grp=i//(factorial[tmpN-1])
        perm+=choices[grp]
        subgrp=i%(factorial[tmpN-1])
        choices.remove(choices[grp])
        tmpN-=1
        dfs(subgrp)

    dfs(k-1)
    return perm

# print(lc60(3,3))
# print(lc60(3,1))
# print(lc60(4,9))