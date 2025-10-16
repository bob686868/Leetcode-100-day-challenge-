def l_2257(m,n,guards,walls):
    grid=[[2]*n for _ in range(m)]
    guarded_cells=0
    is_guarded=0
    guards=set(map(tuple,guards))
    walls=set(map(tuple,walls))

    ## step 1 :build the grid 
    ## 0 -> guard
    ## 1 -> wall
    ## 2 -> unvisited blank cell
    ## 3 -> visited blank cell

    for i in range(m):
        for j in range(n):
            if (i,j) in guards:
                grid[i][j]=0
            elif (i,j) in walls:
                grid[i][j]=1
    ## step 2 : check guarded cells from left to right 

    for i in range(m):
        is_guarded=0
        for j in range(n):
            if grid[i][j]==0:
                is_guarded=1
                guarded_cells+=1
            elif grid[i][j]==1:
                is_guarded=0
                guarded_cells+=1

            elif grid[i][j]==2:
                guarded_cells+=is_guarded
                if is_guarded:
                    grid[i][j]=3
        
    
    ## step 3 : check guarded cells from right to left 

    for i in range(m):
        is_guarded=0
        for j in range(n-1,-1,-1):
            if grid[i][j]==0:
                is_guarded=1
            elif grid[i][j]==1:
                is_guarded=0
            elif grid[i][j]==2:
                guarded_cells+=is_guarded
                if is_guarded:
                    grid[i][j]=3


    ## step 4 : from top to bottom

    for j in range(n):
        is_guarded=0
        for i in range(m):
            if grid[i][j]==0:
                is_guarded=1
            elif grid[i][j]==1:
                is_guarded=0
            elif grid[i][j]==2:
                guarded_cells+=is_guarded
                if is_guarded:
                    grid[i][j]=3
    ## step 5 : from bottom to top

    for j in range(n):
        is_guarded=0
        for i in range(m-1,-1,-1):
            if grid[i][j]==0:
                is_guarded=1
            elif grid[i][j]==1:
                is_guarded=0
            elif grid[i][j]==2:
                guarded_cells+=is_guarded
                if is_guarded:
                    grid[i][j]=3
        print(guarded_cells)

    return m*n-guarded_cells

# print(l_2257(4,6,[[0,0],[1,1],[2,3]],[[0,1],[2,2],[1,4]]))
# print(l_2257(3,3,[[1,1]],[[0,1],[1,0],[2,1],[1,2]]))

def lc_2516(s,k):
    if k==0:return 0

    counts=[0]*3
    minutes=float('inf')
    l,r=0,len(s)-1
    ## step 1 : try taking only from the beginning
     
    while l<len(s) and any([c<k for c in counts]):
        asci=ord(s[l])-ord('a')
        counts[asci]+=1
        l+=1
    if l==len(s) and any([c<k for c in counts]):return -1

    ## step 2 : try removing one character from the left subarray and keep adding from the right subarray
    ##          until we reach desired counts(2,2,2)
    minutes=l
    for l in range(l-1,-1,-1):
        asci=ord(s[l])-ord('a')
        counts[asci]-=1

        while r>=l and any([c<k for c in counts]):
            asci=ord(s[r])-ord('a')
            counts[asci]+=1
            r-=1
        
        if any([c<k for c in counts]):continue
        print(l,'--------',r)
        print(minutes)
        minutes=min(minutes,(l+len(s)-r-1))

    return minutes

# print(lc_2516("aabaaaacaabc",2))
# print(lc_2516("a",1))