import numpy as np
import random



def valide (L,m):                                   #fonction qui donne la validité de la liste L jusqu'à l'indice m
    a=0
    for i in range (m):
        if (L[i] in L[:i]) or (L[i] in L[i+1:m+1]):  #on regarde si il y a une reine placée dans la même ligne
            a=1
        else :
            j=1
            while i+j<=m and a==0:
                if L[i+j]==L[i]+j or L[i+j]== L[i]-j: #on regarde s'il y a des reines dans les diagonales
                    a=1
                j+=1
            j=1
            while i-j>=0 and a==0:
                if L[i-j]==L[i]-j or L[i-j]==L[i]+j:
                    a=1
                j+=1
    if a==1:
        return False
    else:
        return True


def indicepossible(L,m):                         #fonction qui donne les indices possibles d'une liste pour une ligne m en tenant compte des éléments de la liste : L[:m]
    M=[]
    for i in range (len(L)):
       L[m]=i
       if valide(L,m):
           M.append(i)
    return M


def nombre(n):                                  #fonction qui donne le nombre de cas possible pour un échiquier de taille n*n
    L=np.zeros((n,n))
    m=1
    
    for i in range(n):
        L[i,0]=i
    while m<n:
        T=L[:]
        a=0
        for i in range(len(T)):
            M=indicepossible(L[i+a],m)
            if len(M)==0:
                L=np.delete(L,(i+a), axis=0)
                a+=-1
            elif len(M)==1:
                L[i+a,m]=M[0]
            else:
                L[i+a,m]=M[0]
                for j in range (1,len(M)):
                    X=np.zeros((1,n))
                    for l in range(m):
                        X[0,l]= T[i,l]
                    X[0,m]=M[j]
                    L=np.concatenate((L,X))
                    
        m+=1
        L = np.unique(L, axis=0)
    L = np.unique(L, axis=0)
    return L

print(nombre(4))
                    
            
    
    
    

    