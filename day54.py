def lc2141(n,batteries):
    l,r=0,sum(batteries)//n
    res=0
    while l<=r:
        m=(l+r)//2

        power=0
        for b in batteries:
            power+=min(b,m)
        if power>=n*m:
            res=max(m,res)
            l=m+1
        else:
            r=m-1

    return res

# print(lc2141(2,[3,3,3]))
# print(lc2141(2, [1,1,1,1]))

nums=[1,2,3,4]

