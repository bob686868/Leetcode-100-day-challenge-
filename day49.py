def lc1015(k):
    cur = 1
    visited={1}

    for i in range(k):
        if cur%k==0:return i+1 
        cur*=10
        cur+=1
        cur%=k
        if cur in visited:return -1
        visited.add(cur)
        
    return -1

# print(lc1015(1))
# print(lc1015(2))
# print(lc1015(3))

def lc235(root,p,q):
    def dfs(node):
        if p.val<=node.val<=q.val or q.val<=node.val<=p.val :return node

        elif node.val>q.val:return dfs(node.left)
        return dfs(node.right)
    return dfs(root)

def lc371(a,b):
    aPositive=a>0
    bPositive=b>0
    res=0
    carry=0
    i=0
    while a>0 or b>0 or carry:
        n1=a%10 if aPositive else a%10
        n2=b%10
        res+=((n1+n2+carry)%10)*10**i
        carry=(n1+n2+carry)//10
        a//=10
        b//=10
        i+=1

    return res

# print(lc371(1,2))
# print(lc371(12,29))

def lc238(nums):
        prefix=1
        zeroCount=0
        for n in nums:
            if n==0:zeroCount+=1
            else:prefix*=n
        
        if zeroCount>=2:return [0]*len(nums)
        res=[]
        for n in nums:
            if n!=0:res.append(prefix//n if zeroCount!=1 else 0)
            else:res.append(prefix)
        return res

def lc121(prices):
    res=0
    minP=10**4
    for p in prices:
        if p<minP:minP=p
        else:
            res=max(res,p-minP)
    return res

# print(lc121([7,1,5,3,6,4]))
# print(lc121([7,6,4,3,1]))