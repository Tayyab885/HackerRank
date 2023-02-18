def split_and_join(line):
    s = line.split(" ")
    new_string = "-".join(s)
    return new_string
    
    

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)