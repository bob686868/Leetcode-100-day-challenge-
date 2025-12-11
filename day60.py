def lc3531(n,buildings):
    maxX,minX={},{} ## min x for a specific value of y
    maxY,minY={},{}

    for b in buildings:
        bx,by=b
        if by not in minX:
            minX[by]=bx
            maxX[by]=bx
        if bx not in minY:
            minY[bx]=by
            maxY[bx]=by
        minX[by]=min(bx,minX[by])
        maxX[by]=max(bx,maxX[by])
        minY[bx]=min(by,minY[bx])
        maxY[bx]=max(by,maxY[bx])
    res=0
    for b in buildings:
        bx,by=b
        if bx>minX[by] and bx<maxX[by] and by>minY[bx] and by<maxY[bx]:
            res+=1
    return res

print(lc3531(3, [[1,2],[2,2],[3,2],[2,1],[2,3]]))
print(lc3531(3,[[1,1],[1,2],[2,1],[2,2]]))
print(lc3531(5,[[1,3],[3,2],[3,3],[3,5],[5,3]]))