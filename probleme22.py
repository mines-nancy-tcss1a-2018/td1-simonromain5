def read():
    fichier = open('C:\\Users\\Public\\Documents\\Python Scripts\\TD1\\p022_names.txt ','r')
    for ligne in fichier:
        chaine=ligne
        L=chaine.split(',')
    fichier.close()
    return L




def solve(n):
    L=read()
    L=sorted(L)
    sommetot=0
    for i in range(len(L)):
        sommenom=0
        L[i]=str(L[i])
        for j in range(1,len(L[i])-1):
            x=ord(L[i][j])-64
            sommenom+=x
        sommetot+=(i+1)*sommenom
    return sommetot


print(solve(1))

    
