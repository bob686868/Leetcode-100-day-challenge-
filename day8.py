from collections import defaultdict
def bestTeam(scores,ages):

    players=sorted(zip(ages,scores))
    dp=[-1 for _ in range(len(ages))] ## subproblem (starting at index i)
    _,lastScore=players[-1]
    dp[-1]=lastScore
    for i in range(len(players)-2,-1,-1):
        dp[i]=dp[i+1]
        _,scoresI=players[i]
        for j in range(i+1,len(players)):
            _,scoresJ=players[j]
            if scoresI<=scoresJ:
                dp[i]=max(dp[i],scoresI+dp[j])
    return dp[0]
            
# print(bestTeam([1,3,5,10,15],[1,2,3,4,5]))
# print(bestTeam([4,5,6,5],[2,1,2,1]))

def maxCircularSubarray(nums):
        total,curMax,curMin,globalMax,globalMin=nums[0],nums[0],nums[0],nums[0],nums[0]

        for n in nums[1:]:   ## look for min subarray , then we can remove it and keep the rest 
                             ## (if not every number is negative) else return the maximum number
                             ## the max subarray sum may not wrap around , so we might consider the globalMax as maximum if greater then obtain result 
                             ## obtained by removing an inner sum
            total+=n
            curMin=min(n,curMin+n)
            curMax=max(n,curMax+n)
            globalMin=min(curMin,globalMin)
            globalMax=max(curMax,globalMax)

        return max(total-globalMin,globalMax) if globalMax>=0 else globalMax

# print(maxCircularSubarray([1,-2,3,-2]))
# print(maxCircularSubarray([5,-3,5]))

def minimumFlipsToMakeStringIncreasing(s):
    dp=[[len(s)]*2 for _ in range(len(s)+1) ]  ## (minFlipsToMakeSubStringIncreasing , hasChosenOne )

    def dfs(i,hasChosenOne):
        if dp[i][hasChosenOne]!=len(s):return dp[i][hasChosenOne]
        if i==len(s)-1:
            chosenNum=int(hasChosenOne)
            return 0 if chosenNum == s[-1] else 1  
        
        ## flip to one
        incrementer1=1 if s[i] != "1" else 0
        nextCost=dfs(i+1,True)
        dp[i][hasChosenOne]=min(dp[i][hasChosenOne],incrementer1+nextCost)

        incrementer0=1 if s[i] != "0" else 0
        if not hasChosenOne:
            nextCost=dfs(i+1,False)
            dp[i][False]=min(dp[i][False],incrementer0+nextCost)
        return dp[i][hasChosenOne]

    incrementer0=1 if s[0] == "1" else 0
    incrementer1=0 if s[0] == "1" else 1
    return min(incrementer0+dfs(0,False),incrementer1+dfs(0,True))
          

# print(minimumFlipsToMakeStringIncreasing("00110"))
# print(minimumFlipsToMakeStringIncreasing("010110"))

def minTimeToCollectAllApples(n,edges,hasApple):
    ## step 1 : adj list
    adj=defaultdict(list)
    visit={0}
    for src,dst in edges:
        adj[src].append(dst)
        adj[dst].append(src)
    ## step 2 : compute num of all appples
    allApples=0
    for i in range(len(hasApple)):
        if hasApple[i]:
            allApples+=1
    ## step 2 : dfs : returns sum of depths of the deepest apple in the subtrees 
    ## or return -1 if subtree doesnt contain any apple
    applesLeft=allApples 
    def dfs(node):
        nonlocal applesLeft
        if len(adj[node])==0 :return 1 if hasApple[node] else 0
        if applesLeft==0:return 0 
        steps=0
        for nei in adj[node]:
            decrementer=1 if hasApple[nei] else 0 
            if nei not in visit:
                visit.add(nei)
                score=dfs(nei)
                applesLeft-=decrementer
                steps+=score
        return steps + (1 if hasApple[node] or steps > 0 else 0)

    return 2*(dfs(0))
print(minTimeToCollectAllApples(7,[[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]],[False,False,True,False,True,True,False]))
print(minTimeToCollectAllApples(7,[[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]],[False,False,True,False,False,True,False]))