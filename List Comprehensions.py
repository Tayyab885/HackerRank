if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    L = [[n1,n2,n3] for n1 in range(x+1) for n2 in range(y+1) for n3 in range(z+1)
     if (n1+n2+n3)!=n]
    print(L)