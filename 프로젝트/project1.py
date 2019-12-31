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
    print("Student\t\t\tName\t\tMidterm\tFinal\tAverage\tGrade")
    print('---------------------------------------------------------------------')
    for student in sorted_students:
        temp = list(student.values())
        student_list.append(temp)
        data = '%s\t%15s\t\t%5s\t%4s\t%6.1f\t%3s\n' % (temp[0], temp[1], temp[2], temp[3], temp[4], temp[5])
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
                if 0 <= int(stud_new) <= 100:
                    if stud_score == 'mid':
                        students[index]['Midterm'] = int(stud_new)
                    else:
                        students[index]['Final'] = int(stud_new)
                    show([tmp_student])
                    print('\n<Score Changed>\n')
                    students[index]['Average'] = (int(students[index]['Final']) + int(students[index]['Midterm'])) / 2
                    get_grade(students[index])
                    data = '%s\t%15s\t\t%5s\t%4s\t%6.1f\t%3s\n' % (
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
    mid_score = int(input('Miderm Score :'))
    final_score = int(input('Final Score :'))
    if 0 <= mid_score and final_score <= 100 :
        stu_temp['Midterm'] = mid_score
        stu_temp['Final'] = final_score
    else:
        print("점수는 0 ~ 100 외의 값은 입력될 수 없습니다.")
        return
    stu_temp['Average'] = (int(stu_temp['Final']) + int(stu_temp['Midterm'])) / 2
    get_grade(stu_temp)
    students.append(stu_temp)
    print('\n<Student Added>\n')
    print("Student\t\t\tName\t\tMidterm\tFinal\tAverage\tGrade")
    print('---------------------------------------------------------------------')
    data = '%s\t%15s\t\t%5s\t%4s\t%6.1f\t%3s\n' % (
        stu_temp['ID'], stu_temp['Name'], stu_temp['Midterm'],
        stu_temp['Final'], stu_temp['Average'], stu_temp['Grade'])
    print(data)

def searchgrade(students):
    stud_sg = input('searchgrade: ')
    found_or_not = 0
    Grades = ('A','B','C','D','F')
    return_stud = list()
    for i in students:
        if stud_sg not in Grades:
            return
        if i['Grade'] in stud_sg:
            print('Grade to search: %s'%i['Grade'])
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
    if len(students) == 0:
        print('List is empty.')
        return
    stud_remove = input('Students ID: ')
    for index, i in enumerate(students):
        if i['ID'] not in stud_remove:
            pass
        elif i['ID'] in stud_remove:
            del students[index]
            print('%s Student removed' %i['ID'])
            found_or_not = i
    if not found_or_not:
        print('NO SUCH PERSON.')

def quit(students):
    while True:
        stud_quit = input('Save data?[yes/no]')
        if stud_quit == 'no':
            print("")
            return
        elif stud_quit == 'yes':
            break
    stud_file = input('File name :')
    students.sort(key=lambda x:x['Average'], reverse=True)
    data = list()
    for x in students:
        data.append(list(x.values())[:-2])
    f = open(stud_file, 'w')
    for i in data:
        a='\t'.join(i)
        a += '\n'
        f.write(a)
    f.close
    exit()

def how():
    print('==================')
    print('    <Command>\n')
    command = ['search', 'show', 'changescore', 'changename', 'searchgrade', 'add', 'remove', 'quit']
    for i,j in enumerate(command):
        print('%d. %s'%(i+1,j))

def changename(students):
    stud_changename = input('Students ID: ')
    for index, i in enumerate(students):
        if i['ID'] not in stud_changename:
            pass
        else:
            tmp_student = dict()
            for key in i:
                tmp_student[key] = i[key]
            stud_name = str(input("How would you change the student's name?"))
            students[index]['Name'] = stud_name
            print('\n<Name Changed>\n')
            show([tmp_student])
            data = '%s\t%15s\t\t%5s\t%4s\t%6.1f\t%3s\n' % (
                students[index]['ID'], students[index]['Name'], students[index]['Midterm'],
                students[index]['Final'], students[index]['Average'], students[index]['Grade'])
            print(data)
            return
    print('NO SUCH PERSON')

def openfile():
    file_name = 'students.txt'

    if len(sys.argv) > 1:
        file_name = sys.argv[1]
    print(file_name)
    with open(file_name, 'r') as f:
    # f = open(file_name, 'r')
        lines = f.readlines()
        return lines

def start(lines):
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
    return students

def loop(students):
    show(students)
    while True:
        user_input = input('#').lower()
        if user_input == 'search':
            search(students)
        elif user_input == 'show':
            show(students)
        elif user_input == 'changescore':
            changescore(students)
        elif user_input == 'searchgrade':
            searchgrade(students)
        elif user_input == 'changename':
            changename(students)
        elif user_input == 'add':
            add(students)
        elif user_input == 'remove':
            remove(students)
        elif user_input == 'quit':
            quit(students)
        elif user_input == '?':
            how()
        else:
            print('명령어가 잘못 되었습니다')
            how()
            pass

if __name__ == '__main__':
    opens = openfile()
    students = start(opens)
    loop(students)

