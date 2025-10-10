## we know that the difference between max and min doesnt change unless we 
## change the mins or maxs themselves , so , we can just consider the combination of
## removals of smallest and largest nums of nums 

def minimum_difference_between_largest_and_smallest(nums):
    if len(nums)<=3:return 0
    nums.sort()
    if len(nums)==4:
        maxs=nums[3::-1]
    else:
        maxs=nums[len(nums)-1:len(nums)-5:-1]
    mins=nums[0:4]

    res=float('inf')
    i1,i2=-1,2
    for d in range(4):
        res=min(res,maxs[i2-d+1]-mins[i1+d+1])
    return res

# print(minimum_difference_between_largest_and_smallest([5,3,2,4]))
# print(minimum_difference_between_largest_and_smallest([1,5,0,10,14]))

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_in_between_zeros(root):
        cur=root.next
        first_modification=True

        cur_sum=0
        while cur:
            if cur.val==0:
                if first_modification:
                    newNode=ListNode(cur_sum)
                    root=newNode
                    prev=root
                    first_modification=False
                    cur_sum=0
                else:
                    newNode=ListNode(cur_sum)
                    prev.next=newNode
                    prev=newNode
                    cur_sum=0
            else:
                cur_sum+=cur.val
            cur=cur.next
        return root



    