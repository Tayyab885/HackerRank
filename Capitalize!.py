def solve(s):
    # L = s.split(" ")
    # st = ""
    # for item in L:
    #    st+= item.capitalize()
    #    st+=" "
    # return st
    for i in s.split():
        s = s.replace(i,i.capitalize())
    return s
print(solve("hello world"))