def lc1925(n):
        res=0
        for a in range(1,n+1):
            for b in range(a,n+1):
                if (a**2+b**2)**0.5>n:break
                if int((a**2+b**2)**0.5) == (a**2+b**2)**0.5:
                    res+=1+(a!=b)
        return res
# print(lc1925(5))
# print(lc1925(12))