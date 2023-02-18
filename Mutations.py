def mutations(string,position,value):
    _list = list(string)
    _list[position] = value
    return "".join(_list)
    

s = input("Enter the String:")
p,v = input().split()
print(mutations(s,int(p),v))