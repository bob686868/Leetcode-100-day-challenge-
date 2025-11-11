def lc14(strs):
        i=0
        min_len=float('inf')
        for s in strs:
            if len(s)<min_len:
                min_len=len(s)

        for j in range(min_len):
            char=strs[0][j]
            for k in range(1,len(strs)):
                if strs[k][j]!=char:
                    return strs[0][:i]
            i+=1
        return strs[0][:min_len]

# print(lc14(["flower","flow","flight"]))
# print(lc14(["dog","racecar","car"]))

from collections import Counter
def lc15(nums):
        res=set()

        nums.sort()

        for i in range(len(nums)):
            target=-nums[i]
            l,r=i+1,len(nums)-1
            while l<r:
                cur_sum=nums[l]+nums[r]
                if cur_sum<target:
                        l+=1
                elif cur_sum>target:
                        r-=1
                else:
                        res.add(tuple(sorted((nums[i],nums[l],nums[r]))))
                        l+=1
                        r-=1
        triplets=[]
        for r in res:
            num1,num2,num3=r
            triplets.append([num1,num2,num3])

        return triplets

# print(lc15([-1,0,1,2,-1,-4]))
# print(lc15([0,1,1]))

def lc16(nums,target):
        res=float('inf')
        nums.sort()

        for i in range(len(nums)):
            l,r=i+1,len(nums)-1
            while l<r:
                cur_sum=nums[l]+nums[r]+nums[i]
                if cur_sum<target:
                        l+=1
                elif cur_sum>target:
                        r-=1
                else:return target
                if abs(cur_sum-target) < abs(res-target):
                    res=cur_sum
                    if res==target:return target

        return res 

# print(lc16([-1,2,1,-4],1))   
# print(lc16([0,0,0],1))  

def lc17(digits):
    digitToLetters={1:"",2:"abc",3:"def",4:"ghi",5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"wxyz"}

    def dfs(i):
          if i == len(digits):
                return [""]
          combinations=dfs(i+1)
          res=[]
          for c in combinations:
                for l in digitToLetters[int(digits[i])]:
                      res.append(l+c)
          return res
    return dfs(0)

# print(lc17("23"))
# print(lc17("2"))

def lc18(nums,target):
      nums.sort()
      def nSum(target,n,i):
                  if n==2:
                        res=[]
                        l,r=i,len(nums)-1
                        while l<r:
                              cur_sum=nums[l]+nums[r]
                              if cur_sum>target:
                                    r-=1
                              elif cur_sum<target:
                                    l+=1
                              else:
                                    res.append([nums[l],nums[r]])
                              l+=1
                              while l<r and nums[l]==nums[l-1]:
                                    l+=1
                                    
                        return res
                  ## n=3 or n=4
                  else:
                        ways=[]
                        for j in range(i,len(nums)-n+1):
                              if j>0 and j!=i and nums[j]==nums[j-1]:continue
                              res=nSum(target-nums[j],n-1,j+1)
                              if res:
                                    for r in res:
                                          r.append(nums[j])
                              if res:
                                    for r in res:
                                          ways.append(r)
                        return ways
                  
      
      return nSum(target,4,0)

# print(lc18([1,0,-1,0,-2,2],0))
# print(lc18([2,2,2,2,2],8))

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def lc19(head,n):

      ## step 1 : get length of linked list
      tmp=head
      length=0
      while tmp:
            length+=1
            tmp=tmp.next

      ## step 2 : move length - n steps then remove the node
      ## use dummy node to avoid edge cases

      dummy=ListNode(0,head)
      tmp=dummy

      for _ in range(length-n):
            tmp=tmp.next
      
      nextNode=tmp.next.next
      tmp.next=nextNode 

      return dummy.next

def lc20(s):
      stack=[]
      matching={")":"(","}":"{","]":"["}
      for c in s:
            if c in matching.values():
                  stack.append(c)
            else :
                  if stack and stack[-1]==matching[c]:
                        stack.pop()
                  else:
                        return False
      return not stack

# print(lc20("()"))
# print(lc20("()[]{}"))
# print(lc20("(]"))

def lc21(list1,list2):
            dummy=ListNode(0)
            cur=dummy

            while list1 and list2:
                    if list1.val<list2.val:
                        cur.next=ListNode(list1.val)
                        list1=list1.next
                    else :
                        cur.next=ListNode(list2.val)
                        list2=list2.next
                    cur=cur.next
            while list1 :
                    cur.next=ListNode(list1.val)
                    list1=list1.next
                    cur=cur.next

            while list2:
                    cur.next=ListNode(list2.val)
                    list2=list2.next
                    cur=cur.next

            return dummy.next


def lc23(lists):
      values=[]
      for l in lists:
            cur=l
            while cur:
                  values.append(cur.val)
                  cur=cur.next

      values.sort()
      dummy=ListNode(-1)
      cur=dummy
      for v in values:
            cur.next=ListNode(v)
            cur=cur.next

      return dummy.next

def lc24(head):
      if not head:return None
      newHead=head.next
      prev,cur=head,head.next
      if not cur:return head

      while prev and cur:
                  nextNode=cur.next
                  prev.next=nextNode.next if (nextNode and nextNode.next) else nextNode
                  cur.next=prev
                  prev=nextNode
                  if prev:
                        cur=prev.next
      return newHead

            
