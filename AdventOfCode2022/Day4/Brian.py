import sys

lol = 0
lmao = 0
for line in sys.stdin:
    l1, l2 = line.split(",")
    a,b = map(int, l1.split("-"))
    c,d = map(int, l2.split("-"))
    
    #part 1

    if (b >= d and a<=c) or (b<=d and a>=c):
        lol += 1
    
    #part 2
    
    if a<=c<=b or a<=d<=b or c<=a<=d or c<=b<=d:
        lmao += 1

print(lmao)
