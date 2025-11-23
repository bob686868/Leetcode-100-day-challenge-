def lc1262(nums):
    dp=[[-1]*3 for _ in range(len(nums))]

    def dfs(index,remainder):
        if index==len(nums) and remainder==0:return 0
        if index==len(nums):return float('-inf')
        if dp[index][remainder]!=-1:return dp[index][remainder]

        
        take=nums[index]+dfs(index+1,(nums[index]+remainder+3)%3)
        skip=dfs(index+1,remainder)
        dp[index][remainder]=max(take,skip)

        return dp[index][remainder]
    res= dfs(0,0)
    return res

# print(lc1262([3,6,5,1,8]))
# print(lc1262([4]))

class Trie:

    def __init__(self):
        self.root={}

    def insert(self, word: str) -> None:
        node=self.root
        for c in word:
            if c not in node:
                node[c]={}
            node=node[c]
        node["end"]=word


    def search(self, word: str) -> bool:
        node=self.root
        for c in word:
            if c not in node:
                return False
            node=node[c]
        return "end" in node

    def startsWith(self, prefix: str) -> bool:
        node=self.root
        for c in prefix:
            if c not in node:
                return False
            node=node[c]
        return True

# t=Trie()
# t.insert("hello")
# print(t.startsWith("h"))
# print(t.startsWith("ha"))
# print(t.search("hello"))
# print(t.search("hel"))

class WordDictionary:

    def __init__(self):
        self.root={}

    def addWord(self, word: str) -> None:
        node=self.root
        for c in word:
            if c not in node:
                node[c]={}
            node=node[c]
        node["end"]={}


    def search(self, word: str,i=0,node=None) -> bool:
        node=self.root if not node else node
        for i in range(i,len(word)):
            c=word[i]
            if c==".":
                for c in node:
                    if c!="end" and self.search(word,i+1,node[c]):
                        return True
            if c not in node:
                return False
            node=node[c]
        return "end" in node

# t=WordDictionary()
# t.addWord("bad")
# t.addWord("dad")
# t.addWord("pad")
# print(t.search("pad"))
# print(t.search("pa"))
# print(t.search(".ad"))
# print(t.search("b.."))

def lc212(board,words):
        r,c=len(board),len(board[0])
        t=Trie()
        for w in words:
            t.insert(w)

        res=[]
        directions=[(0,1),(1,0),(-1,0),(0,-1)]
        def dfs(x,y,node):
            char=board[x][y]
            if char not in node:return
            if "end" in node[char]:res.append(node[char]["end"])
            board[x][y]="#"
            for dx,dy in directions:
                newX,newY=x+dx,y+dy
                if 0<=newX<r and 0<=newY<c:
                    dfs(newX,newY,node[char])
            board[x][y]=char
                    
        for i in range(r):
            for j in range(c):
                dfs(i,j,t.root)
        return list(set(res))

# print(lc212([["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]],["oath","pea","eat","rain"]))
# print(lc212([["a","b"],["c","d"]],["abcb"]))

def lc213(nums):
        if len(nums)<=3:return max(nums)
        dpWithFirst=[0]*len(nums)
        dpWithoutFirst=[0]*len(nums)

        dpWithoutFirst[-1]=nums[-1]
        dpWithFirst[-2]=nums[-2]
        dpWithoutFirst[-2]=max(nums[-2],nums[-1])

        for i in range(len(nums)-3,0,-1):
            dpWithoutFirst[i]=max(nums[i]+dpWithoutFirst[i+2],dpWithoutFirst[i+1])
            
        for i in range(len(nums)-3,-1,-1):
            dpWithFirst[i]=max(nums[i]+dpWithFirst[i+2],dpWithFirst[i+1])
        
        return max(dpWithFirst[0],dpWithoutFirst[1])

# print(lc213([2,3,2]))
# print(lc213([1,2,3,1]))
# print(lc213([1,2,3]))

def lc217(nums):
    return len(nums)!=len(set(nums))

from sortedcontainers import SortedList
from collections import defaultdict
def lc347(nums,k):
    freq=defaultdict(int)
    maxFreq=SortedList()
    for n in nums:
        if freq[n]>0:
            maxFreq.remove((freq[n],n))
        freq[n]+=1
        maxFreq.add((freq[n],n))
    res=[]
    for i in range(k):
        res.append(maxFreq[-i-1][1])
    return res

# print(lc347([1,1,1,2,2,3],2))
# print(lc347([1],1))
# print(lc347([1,2,1,2,1,2,3,1,3,2],2))

def lc91(s):
    dp=[-1]*len(s)

    def dfs(i):
        if i>=len(s):return 1
        if dp[i]!=-1:return dp[i]

        s1=s[i:i+1]
        s2=s[i:i+2]
        res=0
        if s1!="" and 0<=int(s1)<=26 and s1[0]!="0":res+=dfs(i+1)
        if s2!="" and 0<=int(s2)<=26 and s2[0]!="0" and i+2<=len(s):res+=dfs(i+2)
        dp[i]=res
        return dp[i]
        

    return dfs(0)

# print(lc91("12"))
# print(lc91("226"))
# print(lc91("06"))

