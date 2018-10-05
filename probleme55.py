
def palindrome(x):
    x=str(x)
    m=0
    for i in range (int(len(x)/2)+1):
       if x[i]!=x[len(x)-i-1]:
           m=1
    if m==0:
        return True
    else:
        return False
    
def retourner(x):
    x=str(x)
    t=str()
    for i in range(len(x)):
        t=t+x[len(x)-i-1]
    return int(t)

def solve(n):
    m=0
    for i in range(n):
        j=0
        t=i
        f=0
        while j<=50 and f==0:
            t=t+retourner(t)
            if palindrome(t):
                f=1
            j+=1
        if j==51:
            m+=1
                
    return m

print(solve(10000))

            

        
    
        

