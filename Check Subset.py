T = int(input())
for i in range(T):
    n = int(input())
    A = set(map(int, input().split()))
    n1 = int(input())
    B = set(map(int, input().split()))
    if A.issubset(B):
        print(True)
    else:
        print(False)