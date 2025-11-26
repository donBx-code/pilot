
# list = [expression  for item in iterable if condision]
x = 1
y = 1
z = 2
n = 3
#aa = [list((a,b,c)) for a in range(x +1)  for b in range(y +1) for c in range(z +1)  if sum((a,b,c)) != n]
 

aa = [[a,b,c] for a in range(x +1)  for b in range(y +1) for c in range(z +1)  if a + b + c != n]
print(aa)