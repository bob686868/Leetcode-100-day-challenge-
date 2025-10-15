def max_xor_with_subqueries(nums,maximumBit):
    totalXor=0
    result=[]
    for n in nums:
        totalXor^=n

    for i in range(len(nums)-1,-1,-1):
        ## step 1 : get the opposite of the the totalXor up to maximumBit
        best_num=0
        for j in range(maximumBit):
            if totalXor&1<<j==0:
                best_num|=1<<j 
        result.append(best_num)
        totalXor^=nums[i]
    return result

# print(max_xor_with_subqueries([0,1,1,3],2))
# print(max_xor_with_subqueries([2,3,4,7],3))

import math
def minimized_max_of_product_distributed_to_any_store(n,quantities):
    l,r=0,max(quantities)
    res=float('inf')
    while l<=r:
        m=(l+r)//2

        ## test if distributing a max of m is feasible 
        stores=0
        for q in quantities:
            stores+=math.ceil(q/m)

        if stores<=n:
            res=min(res,m)
            r=m-1
            print(stores)
        elif stores>n:
            l=m+1
    return res

# print(minimized_max_of_product_distributed_to_any_store(6,[11,6]))
# print(minimized_max_of_product_distributed_to_any_store(7,[15,10,10]))

def most_beautiful_item_of_each_query(items,queries):
    res=[]
    max_query=max(queries)
    dp=[[0]*(max_query+1) for _ in range(len(items))]  ## (i,cost_spent)

    for i in range(len(items)-1,-1,-1):
        for c in range(max_query-1,-1,-1):
            cost,beauty=items[i]
            if c+cost<=max_query:
                dp[i][c]=max(dp[i][c],beauty+dp[i][c+cost])
    maxs_dp=[]
    first_iteration=True
    for m in dp[0]:
        if first_iteration:
            maxs_dp.append(m)
            first_iteration=False
        maxs_dp.append(max(m,maxs_dp[-1]))

    for q in queries:
        res.append(dp[0][q])

    return res

# print(most_beautiful_item_of_each_query([[1,2],[3,2],[2,4],[5,6],[3,5]],[1,2,3,4,5,6]))
# print(most_beautiful_item_of_each_query([[1,2],[1,2],[1,3],[1,4]],[1]))
