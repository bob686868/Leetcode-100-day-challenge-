def lc717(nums):
    i=0
    while i<len(nums)-1:
        if nums[i]==1:i+=2
        else:i+=1
    return i==(len(nums)-1)

# print(lc717([1,0,0]))
# print(lc717([1,1,1,0]))

def lc71(path):
        stack=[]
        i=0
        def readWord():
            nonlocal i
            word=[]
            while i<len(path) and path[i]!="/":
                word.append(path[i])
                i+=1
            stack.append(''.join(word))
        
        while i<len(path):
            ## read slash
            stack.append(path[i])
            i+=1
            ## skip redundant slashes
            while i<len(path) and path[i]=="/":
                i+=1
            if i==len(path):stack.pop();break
            
            ## read word or dots
            if i+1==len(path) and path[i]==".":break
            if path[i]=='.' and path[i+1]=="." and (i+2==len(path) or path[i+2]=="/"):
                i+=2
                stack.pop()  ## remove newly added slash
                if stack:stack.pop()  ## remove word 
                if stack:stack.pop()   ## remove slash before word
            elif path[i]=="." and path[i+1] =="/" :
                i+=1
                stack.pop()
            else:
                readWord()
        if stack and stack[-1]=="/":stack.pop()
        return "".join(stack) if len(stack)>0 else "/"

# print(lc71("/a/../../b/../c//.//"))            
# print(lc71("/home//foo/"))            
# print(lc71("/home/user/Documents/../Pictures"))            
# print(lc71( "/.../a/../b/c/../d/./"))   

def lc72(word1,word2):
    if len(word2)>len(word1):word1,word2=word2,word1
    n1,n2=len(word1),len(word2)
    dp=[[n1+n2]*n2 for _ in range(n1)]
    def dfs(i,j):
        if i==n1 and j==n2:return 0
        if i==n1:return n2-j
        if j==n2:return n1-i
        if word1[i]==word2[j]:
            steps=dfs(i+1,j+1)
        else:
            steps=1+min(dfs(i+1,j),dfs(i+1,j+1))
        dp[i][j]=min(dp[i][j],steps)
        return steps
    return dfs(0,0)
# print(lc72( "horse","ros"))         
# print(lc72("intention","execution"))   

def lc73(matrix):
    r,c=len(matrix),len(matrix[0])
    isFirstColZero=False
    isFirstRowZero=True

    for i in range(r):
        for j in range(c):
            if matrix[i][j]==0:
                matrix[i][0]=0
                matrix[0][j]=0
                if j==0:isFirstColZero=True
                if i==0:isFirstRowZero=True

    for i in range(1,r):
        for j in range(1,c):
            if matrix[i][0]==0 or (j==0 and isFirstColZero) or (j!=0 and matrix[0][j]==0):
                matrix[i][j]=0
    
    for i in range(r):
        if isFirstColZero:
            matrix[i][0]=0

    for j in range(c):
        if isFirstRowZero:
            matrix[0][j]=0
    
    return matrix

# print(lc73( [[1,1,1],[1,0,1],[1,1,1]]))
# print(lc73([[0,1,2,0],[3,4,5,2],[1,3,1,5]]))


