import sys

def get_grade(para):
    if para['Average'] >= 90:
        para["Grade"] = "A"
    elif para['Average'] >= 80:
        para["Grade"] = "B"
    elif para['Average'] >= 70:
        para["Grade"] = "C"
    elif para['Average'] >= 60:
        para["Grade"] = "D"
    else:
        para["Grade"] = "F"

def show(students):
    sorted_students = sorted(students, key=lambda x: x['Average'], reverse=True)
    student_list = list()
    print("Student\t\t\tName\t\tMidterm\t\tFinal\t\tAverage\t\tGrade")
    print('---------------------------------------------------------------------------------------------')
    for student in sorted_students:
        temp = list(student.values())
        student_list.append(temp)
        data = '%s\t%15s\t\t%4s\t\t%3s\t\t%6.1f\t\t%4s\n' % (temp[0], temp[1], temp[2], temp[3], temp[4], temp[5])
        print(data)

def search(students):
    stud_found = input('Student ID: ')
    found_or_not = 0
    return_stud = list()
    for i in students:
        if i['ID'] == stud_found:
            found_or_not = i
            break
    if not found_or_not:
        print('NO SUCH PERSON.')
        return
    return_stud.append(found_or_not)
    show(return_stud)

def changescore(students):
    stud_change = input('Students ID: ')
    for index, i in enumerate(students):
        if i['ID'] not in stud_change:
            pass
        else:
            tmp_student = dict()
            for key in i:
                tmp_student[key] = i[key]
            stud_score = str(input('Mid or Final?'))
            if stud_score == 'mid' or stud_score == 'final':
                stud_new = input('Input new score :')
                if 0 < int(stud_new) <= 100:
                    if stud_score == 'mid':
                        students[index]['Midterm'] = int(stud_new)
                    else:
                        students[index]['Final'] = int(stud_new)
                    show([tmp_student])
                    print('Score changed.')
                    students[index]['Average'] = (int(students[index]['Final']) + int(students[index]['Midterm'])) / 2
                    get_grade(students[index])
                    data = '%s\t%15s\t\t%4s\t\t%3s\t\t%6.1f\t\t%4s\n' % (
                    students[index]['ID'], students[index]['Name'], students[index]['Midterm'],
                    students[index]['Final'], students[index]['Average'], students[index]['Grade'])
                    print(data)
                    return
                else:
                    return
            else:
                return
    print('NO SUCH PERSON')

def add(students):
    stu_add = input('Sudent ID : ')
    for i in students:
        if stu_add == i['ID']:
            print('ALREADY EXISTS')
            return
    stu_temp = dict()
    stu_temp['ID'] = stu_add
    stu_temp['Name'] = input('Name :')
    stu_temp['Midterm'] = input('Miderm Score :')
    stu_temp['Final'] = input('Final Score :')
    stu_temp['Average'] = (int(stu_temp['Final']) + int(stu_temp['Midterm'])) / 2
    get_grade(stu_temp)
    students.append(stu_temp)
    print('Student added')

def searchgrade(students):
    stud_sg = input('searchgrade: ')
    found_or_not = 0
    return_stud = list()
    for i in students:
        if i['Grade'] in stud_sg:
            if not isinstance(found_or_not, list):
                found_or_not = list()
            found_or_not.append(i)
    if not found_or_not:
        print('NO RESULTS.')
        return
    return_stud.append(found_or_not)
    show(found_or_not)

def remove(students):
    found_or_not = 0
    stud_remove = input('Students ID: ')
    for index, i in enumerate(students):
        if len(students) == 0:
            print('List is empty')
            return

        if i['ID'] not in stud_remove:
            pass
        elif i['ID'] in stud_remove:
            del students[index]
            print('student removed')
            found_or_not = True
    if not found_or_not:
        print('NO SUCH PERSON')

def quit(students):
    while True:
        stud_quit = input('Save data?[yes/no]')
        if stud_quit == 'no':
            return
        elif stud_quit == 'yes':
            break
    stud_file = input('File name :')
    students.sort(key=lambda x: x['Average'], reverse=True)
    data = [list(x.values())[:-2] for x in students]
    f = open(stud_file, 'w')
    for i in data:
        a = '\t'.join(i)
        a += '\n'
        f.write(a)
    f.close

def how():
    command = ['search','show','changescore','searchgrade','add','remove','quit']
    for i in command:
        print(i)

file_name = 'students.txt'

if len(sys.argv) > 1:
    file_name = sys.argv[1]
print(file_name)
f = open(file_name, 'r')
lines = f.readlines()
f.close()

for index, line in enumerate(lines):
    lines[index] = line.strip().split('\t')

students = list()
for i in lines:
    temp = dict()
    temp['ID'], temp['Name'], temp['Midterm'], temp['Final'] = i
    temp['Average'], temp['Grade'] = '', ''
    students.append(temp)
for index, student in enumerate(students):
    student['Average'] = (int(student['Midterm']) + int(student['Final'])) / 2
    get_grade(students[index])

while True:
    user_input = input('#')
    if user_input == 'search':
        search(students)
    elif user_input == 'show':
        show(students)
    elif user_input == 'changescore':
        changescore(students)
    elif user_input == 'searchgrade':
        searchgrade(students)
    elif user_input == 'add':
        add(students)
    elif user_input == 'remove':
        remove(students)
    elif user_input == 'quit':
        quit(students)
        break
    elif user_input == '?':
        how()
    else:
        pass