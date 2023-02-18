if __name__ == '__main__':
    n  = int(input())
    A = set(map(int, input().split()))
    other = int(input())
    for i in range(other):
        oper = input().split()
        if oper[0] == "update":
            other_set = set(map(int, input().split()))
            A.update(other_set)
        elif oper[0] == "intersection_update":
            other_set = set(map(int, input().split()))
            A.intersection_update(other_set)
        elif oper[0] == "difference_update":
            other_set = set(map(int, input().split()))
            A.difference_update(other_set)
        elif oper[0] == "symmetric_difference_update":
            other_set = set(map(int, input().split()))
            A.symmetric_difference_update(other_set)
    print(sum(A))