## instead of trying every possible way of building stations , we can 
## search for a valid solution (min station power that is achievable)
## so , we will binary search the tange

def maximizeMinPowerCity(stations,r,k):
    left,right=0,10**14
    maxPower=0
    
    def checkValid(m):
        increments=[0]*len(stations)
        curInc=0
        windowSum=0
        incrementsLeft=k

        for i in range(min(r+1,len(stations))):
            windowSum+=stations[i]

        for i in range(len(stations)):
            ## check if station needs power
            if i-1>=0:
                curInc-=increments[i-1]
            curPower=curInc+windowSum
            if curPower<m:
                delta=m-curPower
                if i+2*r<len(increments):
                    increments[i+2*r]+=delta
                curInc+=delta
                incrementsLeft-=delta
                if incrementsLeft<0:return False

            ## update window sum
            if i-r>=0:
                windowSum-=stations[i-r]
            if i+r+1<len(stations):
                windowSum+=stations[i+r+1]
        return True

    while left<=right:
        m=(left+right)//2

        isValid=checkValid(m)
        if isValid:
            left=m+1
            maxPower=m
        else:
            right=m-1
    return maxPower

# print(maximizeMinPowerCity([1,2,4,5,0],1,2))
# print(maximizeMinPowerCity([4,4,4,4],0,3))
# print(maximizeMinPowerCity([13,12,8,14,7],2,23))

def putMarblesInBag(weights,k):
    if len(weights)==2:return 0
    initial=weights[-1]+weights[0]
    cut_contribution=[weights[i]+weights[i+1] for i in range(len(weights)-1)]

    cut_contribution.sort()

    maxScore=initial+sum(cut_contribution[-1:-k:-1])
    minScore=initial+sum(cut_contribution[:k-1])

    return maxScore-minScore

# print(putMarblesInBag([6,39,2,58,43,21,20,59,48],9))
# print(putMarblesInBag([1, 3],2))

def maxValueOfOrderedTriplet(nums):
    prefixMax=[nums[0]]
    postfixMax=[nums[-1]]
    for i in range(len(nums)-1):
        postfixMax.append(max(postfixMax[-1],nums[len(nums)-1-i]))
        prefixMax.append(max(prefixMax[-1],nums[i]))
    postfixMax.reverse()
    res=0
    for i in range(1,len(nums)-1):
        res=max(res,(prefixMax[i]-nums[i])*postfixMax[i])

    return res

print(maxValueOfOrderedTriplet([12,6,1,2,7]))
print(maxValueOfOrderedTriplet([1,10,3,4,19]))
print(maxValueOfOrderedTriplet([1,2,3]))

