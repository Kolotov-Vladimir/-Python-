def triangle(n):
    linepast=[1,1]
    linenew=[]
    if n==0:
        return [1]
    else:
        for i in range(0,n-1):
            for j in range(0,len(linepast)+1):
                if j==0 or j==len(linepast):
                   linenew+=[1]
                else:
                    linenew+=[linepast[j - 1]+linepast[j]]
            linepast=linenew
            linenew=[]
        return linepast
k = int(input())
print(triangle(k))
