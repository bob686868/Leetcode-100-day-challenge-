def max_num_of_points_with_cost(points):
    prev_dp=points[-1]

    for i in range(len(points)-2,-1,-1):
        dp=[float('-inf')]*len(points[0])
        for j in range(len(points[0])):
            for k in range(len(points[0])):
                dp[j]=max(dp[j],points[i][j]+prev_dp[k]-abs(k-j))
        prev_dp=dp


    return max(prev_dp)

# print(max_num_of_points_with_cost([[1,2,3],[1,5,1],[3,1,1]]))
# print(max_num_of_points_with_cost([[1,5],[2,3],[4,2]]))

import heapq
def ugly_number_2(n):
    res=[1]
    minHeap=[2,3,5]
    visit=set()
    while n>1:
        val=heapq.heappop(minHeap)
        res.append(val)
        heapq.heappush(minHeap,val*2) if val*2 not in visit else ""
        visit.add(val*2)
        heapq.heappush(minHeap,val*3) if val*3 not in visit else ""
        visit.add(val*3)
        heapq.heappush(minHeap,val*5) if val*5 not in visit else ""
        visit.add(val*5)
        n-=1

    return res

# print(ugly_number_2(11))
# print(ugly_number_2(1))

def two_keys_keyboard(n):
    if n==1:return 0
    dp=[[float('inf')]*(n+1) for _ in range(n+1)] ## (cur_chars, cur_clipboard_size)
    for i in range(n+1):
        dp[n][i]=0

    for num in range(n-1,0,-1):
        for c in range(n,0,-1):
            copy_paste=2+dp[2*num][num] if 2*num<=n else float('inf')
            paste=1+dp[num+c][c] if num+c<=n else float('inf')
            dp[num][c]=min(dp[num][c],copy_paste,paste)
    print(dp)
    return 1+dp[1][1]
# print(two_keys_keyboard(6))
# print(two_keys_keyboard(3))

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def delete_node_from_linked_list(nums,head):
        visit=set()
        available_nums=set()

        cur=head
        while cur:
            available_nums.add(cur.val)
            cur=cur.next

        for n in nums:
            if n in visit or n not in available_nums:continue
            if not head:return None
            while head and head.val==n:
                head=head.next     
            cur=head.next
            prev=head 

            while cur:
                if cur.val==n:
                    prev.next=cur.next
                    cur=prev.next
                    continue
                cur=cur.next
                prev=prev.next
            visit.add(n)
        
        return head if head else None

def insert_gcd_in_linked_list(head):
    def gcd(a,b):
        if a<b:a,b=b,a
        while a%b!=0:
            a,b=a%b,b
            if a<b:a,b=b,a
        return b
    
    cur=head
    next_node=head.next
    while cur:
        newNode=ListNode(gcd(cur.val,next_node.val),next_node)
        cur.next=newNode
        cur=next_node
        next_node=next_node.next
    return head

def linked_list_in_binary_tree(head,root): ## root is the actual binary tree root
        stack=[(head,root)]

        while stack:
            list_node,bt_node=stack.pop()
            if not bt_node:continue
            if list_node.val==bt_node.val:
                next_list_node=list_node.next
                if not next_list_node:
                    return True

                ## take 
                stack.append((next_list_node,bt_node.left)) 
                stack.append((next_list_node,bt_node.right))
                ## skip

                stack.append((head,bt_node.left))
                stack.append((head,bt_node.right))


            else:
                stack.append((head,bt_node.left))
                stack.append((head,bt_node.right))
        return False



    
    
