# Enter your code here. Read input from STDIN. Print output to STDOUT
n1 = int(input())
roll_no1 = set(map(int, input().split()))
b = int(input())
roll_no2 = set(map(int, input().split()))
U = roll_no1.difference(roll_no2)
print(len(U))