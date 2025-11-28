from collections import defaultdict
def lc2872(edges,values,k):
    adj=defaultdict(list)

    for s,d in edges:
        adj[s].append(d)
        adj[d].append(s)
    res=0
    def dfs(node,parent):
        nonlocal res
        curSum=values[node]
        for nei in adj[node]:
            if nei == parent:continue
            curSum+=dfs(nei,node)
        res+=(curSum%k==0)
        return curSum     

    dfs(0,0)
    return res