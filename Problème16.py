
def solve(n):
    t=str(2**n)
    somme=0
    for i in range(len(t)):
        somme+=int(t[i])
    return somme

assert solve(15)==26
print(solve(1000))