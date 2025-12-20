def lc2147(corridor):
        res=1
        i=0
        seats=0
        totalSeats=0

        while i<len(corridor):
            if corridor[i]!="S":
                i+=1
                continue
            seats+=1
            totalSeats+=1
            if seats!=2:
                i+=1
                continue  
            oldI=i
            i+=1
            while i<len(corridor) and corridor[i]!="S":
                i+=1
            if i==len(corridor):break
            res*=(i-oldI)
            seats=0

        return res % (10**9+7) if (totalSeats%2==0 and totalSeats) else 0

# print(lc2147("SSPPSPS"))
# print(lc2147("SSSPPPSPPSPSSSSSSPPPSPP"))
        