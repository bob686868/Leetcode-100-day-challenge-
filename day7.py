from collections import defaultdict,deque
import heapq
def courseScheduleIV(n,prerequisites,queries):
    dp=defaultdict(set) 
    answer=[]

    ## step 1 : compute adjList
    adj=defaultdict(list)
    for src,dst in prerequisites:
        adj[src].append(dst) 

    ## step 2 : precomputation for every node
    def dfs(node):  ## return prerequisites for the node  
        pres=set()
        for nei in adj[node]:
            if len(dp[node])!=0:pres|=dp[node]
            else:               pres|=dfs(nei)
        
        dp[node]=pres
        presCopy=pres.copy()
        presCopy.add(node)
        return presCopy
    
    for node in range(n):
        if len(dp[node])==0:
            dfs(node)

    ## step 3 : answer queries
    for n1,n2 in queries:
        answer.append(n2 in dp[n1])
    return answer

# print(courseScheduleIV(2,[[1,0]],[[0,1],[1,0]]))
# print(courseScheduleIV(2,[],[[1,0],[0,1]]))

def shortestAlternatingPath(n,redEdges,blueEdges):
        redAdj=defaultdict(list)
        blueAdj=defaultdict(list)

        ## step 1 : build adj lists
        for src,dst in redEdges:
            redAdj[src].append(dst)
        for src,dst in blueEdges:
            blueAdj[src].append(dst)

        answers=[-1 for _ in range(n)]
        answers[0]=0
        filled=1

        ## step 2 : mutlisource bfs 

        q=deque()
        q.append((0,0,True)) ## (node , curCost , True = next edge should be blue)
        q.append((0,0,False))
        redVisit={0} 
        blueVisit={0}
        redVisit

        while q and filled != n:
            node,cost,isNextBlue=q.popleft()
            
            if isNextBlue:
                for nei in blueAdj[node]:
                    if nei not in blueVisit:
                        blueVisit.add(nei)
                        if answers[nei]!=-1:
                            answers[nei]=min(answers[nei],cost+1)
                        else:
                            answers[nei]=cost+1
                            filled+=1
                        q.append((nei,cost+1,False))
            else:
                for nei in redAdj[node]:
                    if nei not in redVisit:
                        redVisit.add(nei)
                        if answers[nei]!=-1:
                            answers[nei]=min(answers[nei],cost+1)
                        else:
                            answers[nei]=cost+1
                            filled+=1
                        q.append((nei,cost+1,True))
        
        return answers

# print(shortestAlternatingPath(3, [[0,1],[1,2]] , []))    
# print(shortestAlternatingPath(3, [[0,1]], [[2,1]])) 

def findClosestNodeToTwoNodes(edges,node1,node2): 
            if node1==node2:return node1
            if edges[node1]==node2 and edges[node2]==node1:return min(node1,node2)
            ## step 1 :check if empty 

            emptyGraph=True
            for dst in edges:
                if dst != -1 :
                    emptyGraph=False
                    break
            if emptyGraph: return -1 
            
            ## step 2 : start bfs from both node1 and node2 
            ## when there is an intersection , set min cost to the obtained value 
            ## keep processing options with that same min cost and then return minimum index

            visit={(node1,1),(node2,2)} ## (node,pathNumber)
            q=deque([(0,node1,1),(0,node2,2)])

            minCost,index=float('inf'),float('inf')
            while q:
                curCost,node,pathNumber=q.popleft()
                if curCost>minCost:break
                otherPath=2 if pathNumber == 1 else 1
                if (node,otherPath) in visit:
                    minCost=curCost
                    index=min(node,index)
                if edges[node]  !=  -1:
                    nei=edges[node]
  
                    if (nei,pathNumber) not in visit:
                        visit.add((nei,pathNumber))
                        q.append((curCost+1,nei,pathNumber))
            return index if index!=float('inf') else -1 

# print(findClosestNodeToTwoNodes([2,2,3,-1],0,1))
# print(findClosestNodeToTwoNodes([1,2,-1],0,2))
# print(findClosestNodeToTwoNodes([5,4,5,4,3,6,-1],0,1))