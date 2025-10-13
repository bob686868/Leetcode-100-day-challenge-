import heapq
def smallest_num_of_unoccupied_chair(times,targetFriend):
    available_chairs=[i for i in range(len(times))]
    arrival_of_target=times[targetFriend][0]
    occupied_chairs=[] ## ( leaving , chair_num)
    times.sort()
    i=0
    while True:
        arrival,leaving=times[i]
        while occupied_chairs and occupied_chairs[0][0]<arrival:
            leaving2,chair_num=heapq.heappop(occupied_chairs)
            print(chair_num , 'emptied')
            heapq.heappush(available_chairs,chair_num)
        chair_num=heapq.heappop(available_chairs)
        if arrival==arrival_of_target:
            break
        heapq.heappush(occupied_chairs,(leaving,chair_num))
        i+=1
    return chair_num

# print(smallest_num_of_unoccupied_chair([[1,4],[2,3],[4,6]],1))
# print(smallest_num_of_unoccupied_chair([[3,10],[1,5],[2,6]],0))

def max_swap(num):
    ## step 1 : get greatest num after each digit
    tmp=num
    greatest=[tmp%10,]
    digits=[tmp%10]
    tmp//=10
    i=0
    while tmp>0:
        digit=tmp%10
        tmp//=10
        digits.append(digit)
        if digit<greatest[-1]:
            greatest.append(greatest[-1])
        else :
            greatest.append(digit)
        i+=1

    ## step 2 : get the first digit that isnt greater then all the next digits 
    ## and get the index of both the digit to be swapped and the index of the max digit 
    found_greater=False
    max_index=0
    swapped_index=0
    for i in range(len(greatest)-1,0,-1):
        if found_greater:break
        max_index=i
        print('----------')
        print(digits[i])
        for j in range(i-1,-1,-1):
            print(digits[max_index],digits[i])
            if (i==max_index and digits[max_index]<greatest[j]) or (i!=max_index and greatest[j]>=digits[max_index]):
                if not found_greater:print(i , "-------")
                swapped_index=i
                found_greater=True
                max_index=j
    
    ## step 3 : digits manipulation
    if not found_greater:return num

    return (num - digits[swapped_index]*10**(swapped_index) 
                - digits[max_index]*10**(max_index) 
                + digits[max_index]*10**(swapped_index)
                + digits[swapped_index]*10**(max_index))



# print(max_swap(2736))
# print(max_swap(9973))
# print(max_swap(98368))


def min_swaps_to_seperate_balls(s):
    res=0
    def determine_next_unfilled_position(i):
        while i>=0 and s[i]=="1":
            i-=1
        return i  

    next_unfilled_position=determine_next_unfilled_position(len(s)-1) 
    if next_unfilled_position==-1:return 0

    for i,c in enumerate(s) :
        if c == "1" and i<next_unfilled_position:
            res+=(next_unfilled_position-i)
            next_unfilled_position=determine_next_unfilled_position(next_unfilled_position-1) 
            if next_unfilled_position ==-1:return res
    return res

# print(min_swaps_to_seperate_balls("101"))
# print(min_swaps_to_seperate_balls("100"))
# print(min_swaps_to_seperate_balls("111000"))

def count_num_of_max_bitwitse_or_subsets(nums):
    max_bitwiseor=0
    for n in nums:max_bitwiseor|=n
    def dfs(i,cur_bitwiseor):
        if i==len(nums):
            return 1 if cur_bitwiseor==max_bitwiseor else 0
        res=0
        res+=dfs(i+1,cur_bitwiseor|nums[i])
        res+=dfs(i+1,cur_bitwiseor)
        return res
    return dfs(0,0)

# print(count_num_of_max_bitwitse_or_subsets([2,2,2]))
# print(count_num_of_max_bitwitse_or_subsets([3,2,1,5]))

def kth_largest_sum(root,k):
        maximums=[]
        old_level=[root]

        while old_level:
            sum=0
            new_level=[]
            for n in old_level:
                sum+=n.val
                new_level.append(n.left) if n.left else ''
                new_level.append(n.right) if n.right else ''
            maximums.append(sum)
            old_level=new_level
            
        maximums.sort(reverse=True)
        return maximums[k-1] if k-1<len(maximums) else -1 

def split_string_into_max_substrs(s):
    available_substr={""}
    def dfs(i,cur_str):
        if i == len(s):return 1 

        ## add more chars to grp
        res=dfs(i+1,cur_str+s[i])

        ## start new substr
        if cur_str not in available_substr:
            available_substr.add(cur_str)
            res=max(res,1+dfs(i+1,s[i]))
            available_substr.remove(cur_str)

        return res

    return dfs(0,"")

print(split_string_into_max_substrs("ababccc"))
print(split_string_into_max_substrs("aba"))