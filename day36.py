def lc27(nums,target):
        remainingNums=len(nums)

        for i,n in enumerate(nums):
            if n == target:
                nums[i]=-1
                remainingNums-=1
        
        j=0
        for i,n in enumerate(nums):
            if nums[i]!=-1:
                nums[j]=nums[i]
                j+=1

        return remainingNums


# print(lc27([3,2,2,3],3))
# print(lc27([0,1,2,2,3,0,4,2],2))

def lc28(haystack,needle):
    if needle=="":return 0

    for j,c in enumerate(haystack):
        if j==len(haystack)-len(needle)+1:return -1
        if haystack[j:j+len(needle)]==needle:return j
    return -1
          
    
# print(lc28("sadbutsad","sad"))
# print(lc28("leetcode","leeto"))

def lc29(dividend,divisor):
     res=0
     isNegative=((divisor<0 and dividend>0) or (dividend<0 and divisor>0) )
     dividend,divisor=abs(dividend),abs(divisor)

     while dividend>=divisor:
          incrementor,decrementor=1,divisor
          while  decrementor<<1<dividend:
               decrementor<<=1
               incrementor<<=1
    
          res+=incrementor
          dividend-=decrementor
                    
     return -res if isNegative else min(res,2**31-1)

# print(lc29(7,-3))
# print(lc29(8,2))

# def lc30(s,words):
     
#      ## step 1 : generate all permutations 
#      perms=set()
#      def dfs(remainingChoices,curStr): ## curStr is a list of indexes that will be converted to a string when
#                                        ## we reach the base case
#           if not remainingChoices:
#                strs=[]
#                for n in curStr:
#                     strs.append(words[n])
#                perms.add(''.join(strs))
#                return
#           for choice in remainingChoices:
#                curStr.append(choice)
#                aux=remainingChoices.copy()
#                aux.remove(choice)
#                dfs(aux,curStr)
#                curStr.pop()
#      remainingChoices={i for i in range(len(words))}
#      dfs(remainingChoices,[])
#      ## step 2: check if any of the substring is contained in perms
#      totalPermsLength=len(words)*len(words[0])
#      result=[]
#      for i in range(len(s)-totalPermsLength+1):
#           if s[i:i+totalPermsLength] in perms:
#                result.append(i) 
#      return result


from collections import Counter,defaultdict
def lc30(s,words):
     wordCounter=Counter(words)
     windowLength=len(words)*len(words[0])
     wordLength=len(words[0])
     
     res=[]
     for l in range(len(s)-windowLength+1):
          r=l+windowLength
          sCounter=defaultdict(int)

          ## get every word
          hasMatched=True
          for i in range(l,r,wordLength):
               curWord=s[i:i+wordLength]
               sCounter[curWord]+=1
               if sCounter[curWord]>wordCounter[curWord]:
                    hasMatched=False
                    break
          if hasMatched and all(sCounter[w] == wordCounter[w] for w in sCounter):
                res.append(l)
     return res

# print(lc30("barfoothefoobarman",["foo","bar"]))
# print(lc30("wordgoodgoodgoodbestword",["word","good","best","word"]))
# print(lc30("baaaacbcc",["bc","ac","aa","ba"]))

def sortSubList(nums,start,end):
     ## quick sort
     def quickSort(l,r):
          if l<start or l>=r or l>end or r>end or r<start:return
          pivot=nums[r]
          i=l
          for j in range(l,r):
               if nums[j]<=pivot:
                    nums[j],nums[i]=nums[i],nums[j]
                    i+=1
          nums[i],nums[r]=nums[r],nums[i]
          
          quickSort(l,i-1)
          quickSort(i+1,r)
     quickSort(start,end)
     return nums

# print(sortSubList([1,3,2],2,2))
def lc31(nums):
        hasSwapped=False
    ## look for the last index where nums isnt strictly decreasing anymore
        for i in range(len(nums)-2,-1,-1):
            if nums[i]<=nums[i+1]:
                ## look for the minimum element greater than nums[i] and coming after it
                minIndex,minValue=-1,float('inf')
                for j in range(i+1,len(nums)):
                    if nums[j]<minValue and nums[j]>nums[i]:
                        minIndex=j
                        minValue=nums[j]
                nums[i],nums[minIndex]=nums[minIndex],nums[i]
                sortSubList(nums,i+1,len(nums)-1)
                hasSwapped=True
                break

        if not hasSwapped :
            nums.sort()
        return nums

# print(lc31([1,2,3]))
# print(lc31([3,2,1]))
# print(lc31([1,3,2]))
import math
def lc2654(nums):
        minLength=len(nums)+1
        nonOneNums=0
        for n in nums:
            if n!=1:
                nonOneNums+=1
                
        for l in range(len(nums)):
            if nums[l]==1 or nonOneNums!=len(nums):
                minLength=1                    
                break
            cur_gcd=nums[l]
            r=l
            while r<len(nums)-1 and cur_gcd!=1 :
                r+=1
                cur_gcd=math.gcd(cur_gcd,nums[r])
            if cur_gcd ==1:
                # print(minLength)
                minLength=min(minLength,r-l+1)
        if minLength==len(nums)+1:return -1
        if minLength==1:return nonOneNums
        return 2*(minLength-1)+(nonOneNums-minLength)

# print(lc2654([2,6,3,4]))
# print(lc2654([6,10,15]))
# print(lc2654([2,10,6,14]))
     


          