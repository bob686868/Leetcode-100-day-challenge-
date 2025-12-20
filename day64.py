def lc2110(prices):
    streak=0
    res=1

    for i in range(1,len(prices)):
        if prices[i]==prices[i-1]-1:
            streak+=1
        else:streak=0
        res+=streak+1
    return res

# print(lc2110([3,2,1,4]))
# print(lc2110( [8,6,7,7]))
