if __name__ == '__main__':
    n = int(input("Total values: "))
    values = map(int,input().split())
    t = tuple(values)
    print(hash(t))