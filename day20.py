def averageWaitingTime(customers):
    time=customers[0][0]+customers[0][1]
    watiting_time=customers[0][1]

    for i in range(1,len(customers)):
        arrivalTime,elapsedTime=customers[i]
        if arrivalTime<time:
            watiting_time+=time-arrivalTime+elapsedTime
            time+=elapsedTime

        else:
            watiting_time+=elapsedTime
            time=arrivalTime+elapsedTime
    return watiting_time/len(customers) 

# print(averageWaitingTime([[1,2],[2,5],[4,3]]))
# print(averageWaitingTime([[5,2],[5,4],[10,3],[20,1]]))

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import defaultdict
def build_tree_from_description(descriptions):
    nodes=defaultdict(int)
    visit=set()

    for d in descriptions:
        n1,n2,left=d
        if not nodes[n1]:
            nodes[n1]=TreeNode(n1)
            visit.add(n1)
        if not nodes[n2]:
            nodes[n2]=TreeNode(n2)
            visit.add(n2)

        if left :
            nodes[n1].left=nodes[n2]
        else:
            nodes[n1].right=nodes[n2]
    
    ## search for root

    for d in descriptions:
        visit.remove(d[1])
    return nodes[next(iter(visit))] 

def delete_nodes_and_return_forest(root,to_delete):
        roots={root}
        has_deleted=False

        def dfs(node,target): ## returns (next_node,target_node_left,target_node_right)
            nonlocal has_deleted
            if node.val==target:
                has_deleted=True
                return (None,node.left,node.right)
            
            left,target_left,target_right=dfs(node.left,target) if node.left else (None,None,None)
            node.left=left 
            if not has_deleted:
                right,target_left,target_right=dfs(node.right,target) if node.right else (None,None,None)
                node.right=right  


            return (node,target_left,target_right)
        
        for e in to_delete:
            has_deleted=False
            for r in roots:
                if r.val==e:
                    forest1=r.left
                    forest2=r.right
                    roots.remove(r)
                    roots.add(forest1) if forest1 else None
                    roots.add(forest2) if forest2 else None 
                    break
                _,forest1,forest2=dfs(r,e)
                if has_deleted:
                    roots.add(forest1) if forest1 else None
                    roots.add(forest2) if forest2 else None 
                    break

        return roots

def sort_the_jumbled_nums(mapping,nums): ## consider jumbled to be the given num and consider regular to be the converted one 
    jumbled_to_regular=defaultdict(int)
    def convert_to_regular(n):
        res,i=0,0
        while n>0:
            digit=n%10
            res+=(mapping[digit]*10**i)
            i+=1
            n//=10
        return res
    
    for n in nums:
        jumbled_to_regular[n]=convert_to_regular(n)
    nums.sort(key=lambda x:jumbled_to_regular[x])
    return nums

# print(sort_the_jumbled_nums([8,9,4,0,2,1,3,5,7,6],[991,338,38]))
# print(sort_the_jumbled_nums([0,1,2,3,4,5,6,7,8,9],[789,456,123]))

import heapq
def city_with_minimum_neighbors(n,edges,distanceThreshold):
    adj=defaultdict(list)
    res,resIndex=float('inf'),-1
    for src,dst,w in edges:
        adj[src].append((dst,w))
        adj[dst].append((src,w))

    def djikstras(node):
        res=-1  ## dont count the node as a neighbor of itself
        minHeap=[(0,node)]
        visit=set()

        while minHeap and minHeap[0][0]<=distanceThreshold:
            dist,node=heapq.heappop(minHeap)
            if node in visit: continue
            res+=1
            visit.add(node)
            for nei,weight in adj[node]:
                if nei not in visit:
                    heapq.heappush(minHeap,(dist+weight,nei))
        return res 

    for num in range(n):
        nei=djikstras(num)
        if nei<=res:
            resIndex=num
            res=nei
    return resIndex

# print(city_with_minimum_neighbors(4,[[0,1,3],[1,2,1],[1,3,4],[2,3,1]],4))
# print(city_with_minimum_neighbors(5,[[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]],2))

def string_conversion_min_cost(source,target,original,changed,cost):
            cache=[[float('inf')]*26 for _ in range(26)]
            adj={}
            res=0

            for i in range(len(changed)):
                if original[i] not in adj:
                    adj[original[i]]=[]
                adj[original[i]].append((changed[i],cost[i]))

            def djikstras(src,target):
                minHeap=[(0,src)]
                visit=set()

                while minHeap:
                    cost,node=heapq.heappop(minHeap)
                    if node in visit:continue
                    cache[ord(src)-ord('a')][ord(node)-ord('a')]=cost
                    visit.add(node)
                    if node==target:return cost
                    if node not in adj:continue
                    for nei,cost2 in adj[node]:
                        if nei not in visit:
                            heapq.heappush(minHeap,(cost+cost2,nei))
                return float('inf')
            for i in range(len(source)):
                l1,l2=source[i],target[i]
                if l1==l2:continue
                asci1,asci2=ord(l1)-ord('a'),ord(l2)-ord('a')
                if cache[asci1][asci2]!=float('inf'):
                    res+=cache[asci1][asci2]
                    continue
                c=djikstras(l1,l2)
                res+=c
                cache[asci1][asci2]=c
                if res==float('inf'):return -1
            return res

# print(string_conversion_min_cost("abcd","acbe",["a","b","c","c","e","d"],["b","c","b","e","b","e"],[2,5,5,1,2,20]))
# print(string_conversion_min_cost( "aaaa","bbbb",["a","c"],["c","b"],[1,2]))

    


    





    