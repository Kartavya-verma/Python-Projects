def rotate(m):
    print("[",end = "")
    for i in range(len(m)):
        print("[",end = "")
        for j in range(len(m[i])-1,-1,-1):
            if(j!=0):
                print(str(m[j][i])+", ",end="")
            else:
                print(m[j][i],end= "")
        if(i!=(len(m)-1)):
            print("], ",end="")
        else:
            print("]",end="")
    return("]")


rotate([[1,2],[3,4]])