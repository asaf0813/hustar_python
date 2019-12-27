def average(x, y):
    return (x * 0.4 + y * 0.6)


def grade_avg(x):
    if x >= 90:
        return 'A'
    elif x >= 80:
        return 'B'
    elif x >= 70:
        return 'C'
    elif x >= 60:
        return 'D'
    else:
        return 'F'


fr = open("score.txt", "r")
fw = open("report.txt", "w")

d = {}
avg = 0
grade = 0

for line in fr:
    line_list = line.split()
    d[line_list[0]] = line_list[1], line_list[2]
    avg = average((float)(d[line_list[0]][0]), (float)(d[line_list[0]][1]))
    grade = grade_avg(avg)
    data = "%s %s %s %.1f(%s)" % (line_list[0], line_list[1], line_list[2], avg, grade)
    fw.write(data)
    print(data)

fr.close()
fw.close()
