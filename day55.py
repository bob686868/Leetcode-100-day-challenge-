def lc3623(points):
        grps={}
        for x,y in points:
            if y not in grps:grps[y]=0
            grps[y]+=1

        total=0
        res=0
        for g in grps:
            total+=(grps[g])*(grps[g]-1)//2

        for g in grps:
            curGrps=grps[g]*(grps[g]-1)//2
            total-=curGrps
            res+=total*curGrps

        return res%(10**9+7)


print(lc3623([[1,0],[2,0],[3,0],[2,2],[3,2]]))
print(lc3623([[0,0],[1,0],[0,1],[2,1]]))
    
    