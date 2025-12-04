def lc2211(directions):
    hasStationary=directions[0]=="S"
    res=0
    accumulator=directions[0]=="R"

    for i in range(1,len(directions)):
        if directions[i]=="R":
            accumulator+=1
            continue
        if directions[i]=="S":
            res+=(accumulator)
            hasStationary=True
            accumulator=0

        else:
            if accumulator==0:res+=hasStationary
            else:
                res+=(accumulator+1)
                hasStationary=True
            accumulator=0
    return res

print(lc2211("RLRSLL"))
# print(lc2211("LLRR"))