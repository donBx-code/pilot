#Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
#Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.
import sys

if __name__ == '__main__':
    from io import StringIO


    # Store the original stdin
    original_stdin = sys.stdin

    #mydata = """9
    #3 7 8 5 12 14 21 13 18"""

    mydata ="""12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print"""

    sys.stdin = StringIO(mydata)
    n = int(input().strip())
    
    arr = []
    
    for _ in range(n):
        s = input().split()        
       
        if s[0] == "print":
            print(arr)
            
        elif s[0] == "insert":
            arr.insert(int(s[1]), int(s[2]) )
            #print(arr)
        
        elif s[0] == "remove":
            arr.remove(int(s[1]))
            #print(arr)            
            
        elif s[0] == "append":
            arr.append(int(s[1]))
            #print(arr)
            
        elif s[0] == "sort":
            arr.sort()
            #print(arr)
        
        elif s[0] == "pop":
            arr.pop()
        
        elif s[0] == "reverse":
            arr.reverse()



     # Restore the original stdin

    sys.stdin = original_stdin 