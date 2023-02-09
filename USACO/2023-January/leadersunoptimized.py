
#Input
N = int(input())
cowString = [*input()]
endCow = input().split(" ")

#Counts total G cows and H cows (SUPER UNOPTIMIZED)
gCount = 0
hCount = 0
for i in range(len(endCow)):
    endCow[i] = int(endCow[i])
    if(cowString[i] == "G"):
        gCount += 1
    else:
        hCount += 1

#Adds up the total amount of same-breed cows after each cow. 
#If the total count of G or H breeds is the same as the count of a cow at its current index and all cows after it, 
#add a "g" or "h" to the String to show its a leader (UNBELIEVABLY UNOPTIMIZED)
for cow in range(N):
    tempHCount = 0
    tempGCount = 0
    for i in range(cow, endCow[cow]):
        if(cowString[i][0] == "G"):
            tempGCount += 1
        else:
            tempHCount += 1

    if(cowString[cow] == "G" and tempGCount == gCount):
        cowString[cow] = cowString[cow] + "g"
    elif(cowString[cow] == "H" and tempHCount == hCount):
        cowString[cow] = cowString[cow] + "h"


pairs = []
gCrit = []
hCrit = []

#Checks all conditions
#Checks all winning conditions (UNOPTIMIZED
for cow in range(N):
    gCompatible = False
    hCompatible = False
    for i in range(cow, endCow[cow]):
        if(cowString[cow] == "Gg"):
            gCompatible = True
        elif(cowString[cow] == "Hh"):
            hCompatible = True
        elif(cowString[cow][0] == "G" and cowString[i] == "Hh"):
            gCompatible = True
        elif(cowString[cow][0] == "H" and cowString[i] == "Gg"):
            hCompatible = True
    if(gCompatible):
        gCrit.append(cow+1)
    elif(hCompatible):
        hCrit.append(cow+1)

#Adds all the unique pairs to a List to output
for g in gCrit:
    for h in hCrit:
        pairs.append([g, h])

#Prints output
#Although this algorithm is unoptimized, it is accurate. It earned 11/17 test cases (Not too bad!)
print(len(pairs))
