stringVal = "AAAAABBBBAAA"


prevChar= stringVal[0]
i = 0
r=[]
t=()
l=0
for c in stringVal:
    l +=1
    if c == prevChar:
        i+=1
        print(f"{prevChar}-{i}")
        
            
    if c != prevChar:
        r.append((prevChar,i))
        print(f"New char {c}")
        i=1
    
    
    if l == len(stringVal):
        r.append((prevChar,i))

    prevChar = c
    
print(r)