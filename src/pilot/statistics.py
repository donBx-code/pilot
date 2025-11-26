# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

def calcMean(n:int, x:list[int]) ->float :
    return sum(x)/n
    
def calcMedian(n:int, x:list) -> float :
    
    sx = sorted(x)
    nx:int = len(sx)
    
    if nx % 2 ==1:
        md = sx[nx//2]
    else:
        md = ((sx[nx//2 - 1]) + (sx[nx//2]))/2
    
    return md
    
def calcMode(n:int, x:list[int]) ->int:
    count = {}
    
    for item in x:
        count[item] = count.get(item, 0) +1
        
        
    if not count:
        return []
        
    maxf = max(count.values())
    
    md = sorted([item for item, cnt in count.items() if cnt == maxf])
    
    return md[0]
    
def weightedMean(X, W):
    # Write your code here
    wm  = 0.0
    wi = 0.0
    
    for i in range(len(X)):           
  
        wm += (X[i] * W[i])
        wi += W[i] 
                 
    #round to  1 decimal place
    return (round(wm/wi, 1))

    



if __name__ == '__main__':
    from io import StringIO


    # Store the original stdin
    original_stdin = sys.stdin


    myData = """10
    64630 11735 14216 99233 14470 4978 73429 38120 51135 67060
    """
    sys.stdin = StringIO(myData)
    
    n = int(input().strip())
    x = list(map(int, input().rstrip().split()))

    print (calcMean(n, x))
    print (calcMedian(n,x))
    print (calcMode(n, x))

   
    # Restore the original stdin
    sys.stdin = original_stdin