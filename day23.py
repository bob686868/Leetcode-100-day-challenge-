## we know that bitwise and only makes the number smaller (or unchanged)
## so , max bitwise and is the max el of the array
## then , to get a subarray that have that bitwise and , we need that subarray to contain only that value 
## we can solve the new problem with sliding window
def subarray_with_maximum_bitwise_and(nums):
    max_el=max(nums)
    l,r=0,0
    res=1
    while r<len(nums):
        if nums[r]==max_el:
            res=max(res,r-l+1)
            r+=1
        else:
            r+=1
            l=r
    return res
        

# print(subarray_with_maximum_bitwise_and([1,2,3,3,2,2]))
# print(subarray_with_maximum_bitwise_and([1,2,3,4]
# ))


## try every substring ending at index r 
## then find the index of the first string where we had the same state of mask
## maximize the difference between those indices

def longest_substring_containg_even_vowels(s):
    mask_to_index={0:-1}
    letter_to_power={"a":0,"e":1,"i":2,"o":3,"u":4}
    cur_mask=0
    res=0

    for r,cur_char in enumerate(s):
        if cur_char in letter_to_power:
              cur_mask^=2**letter_to_power[cur_char]
        if cur_mask in mask_to_index:
                res=max(res,r-mask_to_index[cur_mask])
        else:
            mask_to_index[cur_mask]=r

    return res

# print(longest_substring_containg_even_vowels("eleetminicoworoep"))
# print(longest_substring_containg_even_vowels("bcbcbc"))

## there is two ways that the time may be seen 
## the first one is the direct one (greater - smaller)     => only need to check adjacent timePoints if array sorted 
## the second one if the one that loops around the nextday => only need to check it for every timePOint with the smallest time if array is sorted 
# def min_time_difference(timePoints):
    
     
def min_time_difference(timePoints):
     
     def regular_time_diff(t1,t2): ## t1 smaller than t2 
          hrs1,mins1=t1.split(":")
          hrs2,mins2=t2.split(":")
          hrs1,hrs2,mins1,mins2=int(hrs1),int(hrs2),int(mins1),int(mins2)

        ## mins
          res_mins=mins2-mins1
          carry=0
          if res_mins<0:
               res_mins+=60
               carry=-1

            
          res_hours=hrs2-hrs1+carry
          return 60*res_hours+res_mins

     res=float('inf')  
     timePoints.sort()
     first_hr,first_min=timePoints[0].split(":")
     first_hr=str(int(first_hr)+24)
     timePoints.append(first_hr+":"+first_min)

     for i in range(len(timePoints)-1):
          res=min(res,regular_time_diff(timePoints[i],timePoints[i+1]))

     return res

# print(min_time_difference(["23:59","00:00"]))
# print(min_time_difference(["00:00","23:59","00:00"]))

# def different_ways_to_add_paranth(expression):
#      dp=[None for _ in range(len(expression))]
#      ops="+-*"
#      def dfs(n):
#           num1=int(expression[n])
#           while n+1<len(expression) and expression[n+1] not in ops:
#                num1*=10
#                num1+=int(expression[n])
#                n+=1
#           if n==len(expression)-1:
#                return [num1]
#           print(num1)
#           res=[]

#           ## add paranthese direct

#           op=expression[n+1]
#           if op=="+":
#             res1=dfs(n+2)
#             for r in res1:
#                  res.append(num1+r)
#           elif op=="-":
#             res1=dfs(n+2)
#             for r in res1:
#                  res.append(num1-r)
#           else:
#             res1=dfs(n+2)
#             for n in res1:
#                  res.append(num1*r)
          
#           ## add parantheses for the expression num1 with num2

#           num2=int(expression[n])
#           n+=2
#           while n+1<len(expression) and expression[n+1] not in ops:
#               num2*=10
#               num2+=int(expression[n])
#               n+=1
          
#           ## no next num
#           if n==len(expression)-1:
#                 if op == "+":
#                      res.append( num1+num2)
#                 elif op=="-":
#                      res.append( num1-num2)
#                 else:
#                      res.append( num1*num2)

#           ## there is next num
#           else : 
#             if op=="+":
#                 res2=dfs(n+2)
#                 for r in res2:
#                     res.append(num2+r)
#             elif op=="-":
#                 res2=dfs(n+2)
#                 for n in res2:
#                     res.append(num2-r)
#             else:
#                 res2=dfs(n+2)
#                 for n in res2:
#                     res.append(num2*r)
#           return res
          
#      return dfs(0)
     
# print(different_ways_to_add_paranth("2-1-1"))
# print(different_ways_to_add_paranth("2*3-4*5"))

def lexicographical_nums(n):
        res=[]
        stack=[1]
        i=2

        while stack:
            new_num=stack.pop()
            res.append(new_num)
            for num in range(9,-1,-1):
                num_to_append=new_num*10+num
                if num_to_append<=n:
                    stack.append(num_to_append)
            if not stack:
                if i<=9:
                    stack.append(i)
                    i+=1


        return res

# print(lexicographical_nums(13))
# print(lexicographical_nums(2))

def find_length_of_lcm(arr1,arr2):
     res=0
     prefixes=set()

     ## add prefixes of arr2 
     for n in arr2:
          ## step 1 : count num of digits
          tmp=n
          if n==0:
               num_digits=1
          else:
               num_digits=0
               while tmp>0:
                    num_digits+=1
                    tmp//=10

          ## step 2:get prefixes 
          i=1
          prefix=n//10**(num_digits-1)

          while num_digits-i>=0:
            prefixes.add(str(prefix))
            i+=1
            prefix=n//10**(num_digits-i)

     ## for each prefix in arr 1 , check if it is a prefix in arr2
     for n in arr1:
        ## step 1 : count num of digits
            tmp=n
            if n==0:
                num_digits=1
            else:
                num_digits=0
                while tmp>0:
                    num_digits+=1
                    tmp//=10
            print(n,'-----')
            ## step 2:get prefixes 
            i=1
            prefix=n//10**(num_digits-1)
            while num_digits-i>=0:
                prefix=n//10**(num_digits-i)
                print(prefix)
                if str(prefix) in prefixes:
                     res=max(res,len(str(prefix)))
                i+=1
     return res

# print(find_length_of_lcm([1,10,100],[1000]))
# print(find_length_of_lcm([1,2,3],[4,4,4]))
# print(find_length_of_lcm([13,27,45],[21,27,48]))

## for two sentences to be similar , there is two conditions
## 1- every word in the smaller s should be in sentence 1 
## 2- every word that is in s1 but not in s2 should be adjacent
def sentence_similarity(s1,s2):
    if len(s1)<len(s2):
        s1,s2=s2,s1
    s1=s1.split()
    s2=s2.split()
    def helper(s1_words,s2_words):  ## consider s2 to be the smaller one 
        i1=0
        has_mismatched=False

        for i2 in range(len(s2_words)):
            old_i1=i1
            while i1<len(s1_words) and s1_words[i1]!=s2_words[i2]:
                if has_mismatched:return False
                i1+=1
            if old_i1!=i1:
                has_mismatched=True
            if i1==len(s1_words):
                break
            i1+=1
        return True if (s2_words[-1]==s1_words[i1-1] and (i1==len(s1_words) or not has_mismatched)) else False
    return helper(s1,s2) or helper(s1[::-1],s2)
      
# print(sentence_similarity("My name is Haley","My Haley"))
# print(sentence_similarity("A","a A b A"))
# print(sentence_similarity("Y ggUFOmtf woKuTtO W uwJZ Zan wgm zprl Kgn mAY xLlCH phA UIVKIohfw al g m","Jfa jfvmGU bKSSX uQ AmTzbBW EF jdc ft Z g VcM oNlI jeX q mNG YnUgGSnejt Y"))

def mim_add_to_make_parantheses_valid(s):
     delta=0
     res=0
     for p in s :
          if p==")":
               delta-=1
               if delta<0:
                    res+=1
                    delta=0
          elif p=="(":
               delta+=1
     return res+delta
     
# print(mim_add_to_make_parantheses_valid("())"))
# print(mim_add_to_make_parantheses_valid("((("))

def max_width_ramp(nums):
     cur_min=nums[0]
     furthest_greater=0
     res=0
     max_index=0
     for i,n in enumerate(nums):
          if n>=cur_min:
               furthest_greater=i
          if n>=nums[max_index]:
               max_index=i
     
     furthest_greater=max_index if furthest_greater==0 else furthest_greater
     res=furthest_greater 
     for i in range(1,len(nums)-1):
            n=nums[i]
            if n >=cur_min:continue

            old_furthest=furthest_greater
            max_index=max(furthest_greater,i+1)
            for j in range(max(furthest_greater,i+1),len(nums)):
                n2=nums[j]
                if n2>=n:
                    furthest_greater=j
                if n2>=nums[max_index]:
                    max_index=j
            if old_furthest ==furthest_greater:
                furthest_greater=max_index 
            else:
                 res=max(res,furthest_greater-i)
            cur_min=n
     return res

# print(max_width_ramp([6,0,8,2,1,5]))
# print(max_width_ramp([3,2,1]))
# print(max_width_ramp( [9,8,1,0,1,9,4,0,4,1]))


                
                    
                
