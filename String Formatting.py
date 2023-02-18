def print_formatted(number):
    # for i in range(1,number+1):
    #     print(f"   {i}  {oct(i)[2:]}  {hex(i)[2:].capitalize()}  {bin(i)[2:]}   ")
    l = len(bin(number)) - 2

    for i in range(1, number + 1):
        f = ""
        for c in "doXb":
            if f:
                f += " "
            f += "{:>" + str(l) + c + "}"
        print(f.format(i, i, i, i))
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)