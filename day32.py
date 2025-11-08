def minOpsToMake0(n):
    res=0
    i=1
    while n>0:
        bit=n%2
        n//=2
        if bit:
            res=-res
            res+=(2**i-1)
        i+=1
    return res

# print(minOpsToMake0(6))
# print(minOpsToMake0(2))

from collections import defaultdict
def twoSum(nums,target):
    numToIndex=defaultdict(list)   

    for i,n in enumerate(nums):
        numToIndex[n].append(i)
    
    nums.sort()
    l,r=0,len(nums)-1

    while l<r:
        curSum=nums[l]+nums[r]
        if curSum>target:
            r-=1
        elif curSum<target:
            l+=1
        else:
            return sorted([numToIndex[nums[l]][0],numToIndex[nums[r]][-1]])

# print(twoSum([2,7,11,15],9))
# print(twoSum([3,2,4],6))

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def addTwoNumbers(l1,l2):
            root=ListNode((l1.val+l2.val)%10)
            carry=(l1.val+l2.val)//10
            l1,l2=l1.next,l2.next
            prev=root

            while l1 and l2:
                prev.next=ListNode((l1.val+l2.val+carry)%10)
                carry=(l1.val+l2.val+carry)//10
                l1,l2=l1.next,l2.next
                prev=prev.next
            while l1:
                prev.next=ListNode((l1.val+carry)%10)
                carry=(l1.val+carry)//10
                prev=prev.next
                l1=l1.next
            while l2:
                prev.next=ListNode((l2.val+carry)%10)
                carry=(l2.val+carry)//10
                prev=prev.next  
                l2=l2.next
            if carry:
                prev.next=ListNode(carry)
                
            return root


    
