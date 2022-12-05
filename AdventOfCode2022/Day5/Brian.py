import sys
lines, drawing = 512, 9


#sort the image into layers of letters
layers = []
for line in range(drawing-1):
    layer = input().split("    ")
    
    new_layer = []
    for box in layer: 
        if box != "":
            
            if box[0]!=" ":
                new_box = box.split(" ")
                for b in new_box: new_layer.append(b[1:2])
            else:
                new_layer.append("")
                new_box = box[1:].split(" ")
                for b in new_box: new_layer.append(b[1:2])

        else:
            new_layer.append("")
    layers.append(new_layer)

#find the number of columns 
n = int(input().replace(" ", "")[-1])

procedure = {}
for i in range(n): procedure[i+1] = []

#sort the layers into their arrangement
for layer in layers:
    i = 0
    for box in layer:
        
        if box != "":
            procedure[i+1].insert(0,box)

        i += 1
print(procedure)
input()
#do instructions
for i in range(lines-drawing-1):
    instruction = input()
    instruction = instruction.replace("move ","")
    instruction = instruction.replace("from","")
    instruction = instruction.replace("to","")

    a,b,c = list(map(int, instruction.split("  ")))
    
    new = []
    for j in range(a):
        
        new.append(procedure[b][-1])
        procedure[b].pop()

    #part 1
    #procedure[c].extend(new)

    #part 2
    new.reverse()
    procedure[c].extend(new)

answer = ""
for p in procedure:
    answer += procedure[p][-1]
print(answer)
