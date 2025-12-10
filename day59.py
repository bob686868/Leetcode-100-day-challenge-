def lc3577(complexities):
    for i in range(1,len(complexities)):
        c=complexities[i]
        if c<=complexities[0]:
            return 0
        
    res=1
    for n in range(1,len(complexities)):
        res*=n
    return res

# print(lc3577([1,2,3]))
# print(lc3577([3,3,3,4,4,4]))

from collections import defaultdict,Counter
def lc3583(nums):
    countRight=Counter(nums)
    countLeft=defaultdict(int)
    res=0

    for n in nums:
        countRight[n]-=1
        res+=countLeft[n*2]*countRight[n*2]
        countLeft[n]+=1
    return res %(10**9+7)

# print(lc3583([6,3,6]))
# print(lc3583([0,1,0,0]))