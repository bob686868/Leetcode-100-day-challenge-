def findAllPossibleRecipes(recipes,ingredients,supplies):
    supplies=set(supplies)
    notReachable=set()
    edges={}

    ## build graph

    for i,r in enumerate(recipes):
        if r not in edges:
            edges[r]=[]
        for ingredient in ingredients[i]:
            edges[r].append(ingredient)

    def canPrepare(recipe):
        if recipe in supplies:return True
        if recipe in notReachable:return False
        if recipe not in edges:return False
        
        notReachable.add(recipe)
        for ing in edges[recipe]:
            if not canPrepare(ing):
                return False
            supplies.add(ing)
        notReachable.remove(recipe)

        return True
    
    result=[]
    for r in recipes:
        if canPrepare(r):
            result.append(r)

    return result

# print(findAllPossibleRecipes(["ju","fzjnm","x","e","zpmcz","h","q"],[["d"],["hveml","f","cpivl"],["cpivl","zpmcz","h","e","fzjnm","ju"],["cpivl","hveml","zpmcz","ju","h"],["h","fzjnm","e","q","x"],["d","hveml","cpivl","q","zpmcz","ju","e","x"],["f","hveml","cpivl"]],["f","hveml","cpivl","d"]))
# print(findAllPossibleRecipes(["bread","sandwich"],[["yeast","flour"],["bread","meat"]],["yeast","flour","meat"]))
# print(findAllPossibleRecipes(["bread","sandwich","burger"],[["yeast","flour"],["bread","meat"],["sandwich","meat","bread"]],["yeast","flour","meat"]))

from collections import defaultdict
def num_of_complete_components(n,edges):

    ## build adj list
    adj=defaultdict(list)
    for src,dst in edges:
        adj[src].append(dst)
        adj[dst].append(src)

    visit=set() ## to avoid readding to the stack
    stack=[]
    res=0

    for i in range(n):
        marked=set()   ## to avoid recounting an edge from the other node perspective
        if i in visit:
            continue
        stack.append(i) ## (cur,prev)
        visit.add(i)
        cur_edges=0
        while stack:
            node=stack.pop()
            for nei in adj[node]:
                if nei not in marked:
                    cur_edges+=1
                if nei not in visit:
                    visit.add(nei)
                    stack.append(nei)
            marked.add(node)
        n=len(marked)
        if cur_edges==(n)*(n-1)//2:
            res+=1
    return res

# print(num_of_complete_components(6,[[0,1],[0,2],[1,2],[3,4]]))
# print(num_of_complete_components(6,[[0,1],[0,2],[1,2],[3,4],[3,5]]))

        
            

    
