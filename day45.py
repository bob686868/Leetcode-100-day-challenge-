from collections import defaultdict,Counter
def lc1930(s):
    countLeft=defaultdict(int)
    countRight=Counter(s)
    used=set()
    res=0

    for c in s:
        countRight[c]-=1
        for x in countLeft:
            if countRight[x]>0 and x+c+x not in used:
                res+=1
                used.add(x+c+x)
        countLeft[c]+=1
    return res
# print(lc1930("aabca"))
# print(lc1930("adc"))
# print(lc1930("bbcbaba"))

def lc424(s,k):
    res=0
    counter=defaultdict(int)
    maxFreq=0
    r=0  ## not including the right value
    for l in range(len(s)):
        length=r-l
        while r<len(s) and length-maxFreq<=k:
            counter[s[r]]+=1
            maxFreq=max(maxFreq,counter[s[r]])
            r+=1
            length=r-l
            if length-maxFreq<=k:
                res=max(res,r-l)

        counter[s[l]]-=1
        
    return res
# print(lc424("AAAAABBBBCBB",4))
# print(lc424("AABABBA",1))

def lc435(intervals):
    intervals.sort()
    prevEnd,res=intervals[0][1],0

    for j in range(1,len(intervals)):
        s,e=intervals[j]

        if s<prevEnd:
            res+=1
            prevEnd=min(e,prevEnd)
        else:
            prevEnd=max(e,prevEnd)
    return res

# print(lc435([[1,2],[2,3],[3,4],[1,3]]))
# print(lc435([[1,2],[1,2],[1,2]]))
# print(lc435([[1,2],[2,3]]))
from collections import deque
def lc572(root,subRoot):

    def dfs(n1,n2):
        if n1!=n2:return False

        if not dfs(n1.left,n2.left):return False
        if not dfs(n1.right,n2.right):return False

        return True
    ## try every node as the root
    ## to get the nodes , we will do a bfs
    q=deque()
    q.append(root)

    while q:
        node=q.popleft()
        if not node: continue
        if dfs(node,subRoot):return True
        q.append(node.left)
        q.append(node.right)
    return False

def lc190(n):
    res=0
    i=0

    for i in range(32):
        newBit=n&1
        if newBit:res+=(1<<(31-i))
        n>>=1
        i+=1
    return res

# print(lc190(43261596))
# print(lc190(2147483644))

def lc191(n):
    res=0
    while n>0:
        res+=n&1
        n>>=1
    return res

# print(lc191(11))
# print(lc191(128))

def lc322(coins,amount):
    dp=[float('inf')]*(amount+1) ## dp[i]= coins needed to change an amount of i units
    dp[0]=0
    for i in range(amount+1):
        for c in coins:
            if i-c>=0:
                dp[i]=min(dp[i-c]+1,dp[i])
    return dp[-1] if dp[-1]!=float('inf') else -1

# print(lc322([1,2,5],11))
# print(lc322([2],3))


