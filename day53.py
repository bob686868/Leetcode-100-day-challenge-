def lc1590(nums,p):
    remainder=sum(nums)%p
    if remainder == 0 : return 0
    prefixes={0:-1}  ## prefix sum to startIndex
    curSum=0
    res=len(nums)

    for i,n in enumerate(nums):
        curSum=(curSum+n) % p
        neededNum=(curSum-remainder) % p
        if neededNum not in prefixes:
            prefixes[curSum]=i
            continue
        res=min(res,i-prefixes[neededNum])
        prefixes[curSum]=i
    return res if res!=len(nums) else -1

# print(lc1590( [3,1,4,2],6))
# print(lc1590([6,3,5,2],9))

