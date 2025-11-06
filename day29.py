from sortedcontainers import SortedList
from collections import defaultdict
def xsum(nums,k,x):
        count=defaultdict(int)
        topX=SortedList()
        curSum=0
        others=SortedList()
        res=[]
        def customAdd(n,c):
            nonlocal curSum
            if len(topX)<x:
                if (c,n) in topX:
                    topX.remove((c,n))
                topX.add((c+1,n))
                curSum+=n
                return 
            if (c,n) in topX:
                topX.remove((c,n))
                topX.add((c+1,n))
                curSum+=n
            elif (c,n) in others:
                others.remove((c,n))
                others.add((c+1,n))
            else:
                others.add((c+1,n))

            if not others : return
            othersMax,topXMin=others[-1],topX[0]
            if othersMax[0]>topXMin[0] or (othersMax[0] == topXMin[0] and othersMax[1]>topXMin[1]):
                curSum-=(topXMin[0]*topXMin[1])
                topX.remove(topXMin)
                topX.add(othersMax)
                others.remove(othersMax)
                others.add(topXMin)
                curSum+=(othersMax[0]*othersMax[1])

        def customRemove(n,c):
            nonlocal curSum

            if (c,n) in topX:
                topX.remove((c,n))
                if c-1>0:
                    topX.add((c-1,n))
                elif others:
                    othersMax=others[-1]
                    others.remove(othersMax)
                    topX.add(othersMax)
                    curSum+=othersMax[0]*othersMax[1]
                curSum-=n

            else:
                others.remove((c,n))
                if c-1>0:
                    others.add((c-1,n))

            if not others or c-1==0: return
            othersMax,topXMin=others[-1],topX[0]
            if othersMax[0]>topXMin[0] or (othersMax[0] == topXMin[0] and othersMax[1]>topXMin[1]):
                curSum-=(topXMin[0]*topXMin[1])
                topX.remove(topXMin)
                topX.add(othersMax)
                others.remove(othersMax)
                others.add(topXMin)
                curSum+=(othersMax[0]*othersMax[1])

        for i in range(k-1):
            customAdd(nums[i],count[nums[i]])
            count[nums[i]]+=1
        
        for i in range(k-1,len(nums)):
            customAdd(nums[i],count[nums[i]])  ## insert the element with its count incremented by 1 
            count[nums[i]]+=1
            res.append(curSum)
            customRemove(nums[i-k+1],count[nums[i-k+1]])  ## insert the element with its count decremented by 1 
            count[nums[i-k+1]]-=1
        return res
    

# print(xsum([10,7,6,9,8],2,1))
# print(xsum([1,1,2,2,3,4,2,3],6,2))
# print(xsum([3,8,7,8,7,5],2,2))

def minimumCostWalk(n,edges,queries):
    class UnionFind:
        def __init__(self):
            self.parent=[i for i in range(n)]
            self.rank=[1]*n
            self.score=[2**17 -1]*n

        def find(self,n):
            parent=self.parent
            while parent[n]!=n:
                parent[n]=parent[parent[n]]
                n=parent[n]
            return n
        
        def union(self,n1,n2,weight):
            parent=self.parent
            score=self.score
            rank=self.rank

            p1,p2=self.find(n1),self.find(n2)
            if p1==p2:
                score[p1]&=weight
            elif rank[p1]>rank[p2]:
                rank[p1]+=rank[p2]
                score[p1]&=weight
                parent[p2]=p1
            else:
                rank[p2]+=rank[p1]
                score[p2]&=weight
                parent[p1]=p2
    uf=UnionFind()
    for src,dst,w in edges:
        uf.union(src,dst,w) 

    result=[]
    for q1,q2 in queries:
        p1,p2=uf.find(q1),uf.find(q2)

        if p1!=p2:
            result.append(-1)
        else:
            result.append(uf.score[p1])
    return result           


# print(minimumCostWalk(5,[[0,1,7],[1,3,7],[1,2,1]],[[0,3],[3,4]]))
# print(minimumCostWalk(3,[[0,2,7],[0,1,15],[1,2,6],[1,2,1]],[[1,2]]))

