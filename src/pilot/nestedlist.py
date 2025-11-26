#Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
#Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.


if __name__ == '__main__':
    from io import StringIO


    # Store the original stdin
    original_stdin = sys.stdin

    #mydata = """9
    #3 7 8 5 12 14 21 13 18"""

    mydata ="""5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39"""

    sys.stdin = StringIO(mydata)
    n = int(input().strip())

    data = list(map(int, input().rstrip().split()))

    print(sorted(data))
    res = quartiles(data)

    print(res)

     # Restore the original stdin


    sys.stdin = original_stdin