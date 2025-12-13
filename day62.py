def lc3606(code,businessLine,isActive):
        validB=["electronics","grocery","pharmacy","restaurant"]
        res=[]
        character_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '_' ]
        def isAlphaNum(c):
            return c != "" and all(char in character_list for char in c )

        for i in range(len(code)):
            c,b,a=code[i],businessLine[i],isActive[i]    
            if not a or not isAlphaNum(c) or not b in validB:continue
            res.append((validB.index(b),c))
        res.sort()
        newRes=[]
        for _,code in res:
             newRes.append(code)
        return newRes


# print(lc3606(["SAVE20","","PHARMA5","SAVE@20"],["restaurant","grocery","pharmacy","restaurant"],[True,True,True,True]))
# print(lc3606(["GROCERY15","ELECTRONICS_50","DISCOUNT10"],["grocery","electronics","invalid"],[False,True,True]))