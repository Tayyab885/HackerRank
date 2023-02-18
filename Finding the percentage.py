if __name__ == '__main__':
    n = int(input("Enter No. of students"))
    student_marks = {}
    average = 0
    for i in range(n):
        name,*line = input().split()
        score = list(map(float,line))
        student_marks[name] = score
    user_input = input("Enter Student Name: ")
    for marks in student_marks[user_input]:
        average += marks
    result = average/len(student_marks[user_input])
    print("%.2f" %result)

