
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
        while j<=50:
            t=t+retourner(t)
            if palindrome(t):
                m+=1
                j+=1
    return m


print(solve(10000))

            

        
    
        

