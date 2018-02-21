from inflect import *
from time import *
from gradeCheck import *
from inputCheck import *


print('***********************')
print('**Calculate your CGPA**')
print('***********************\n')
sleep(2)
print('How many courses do you offer?')
sleep(1.7)
course_num = input('\n' + 'Input TOTAL number of courses here: ')

num = input_check_course_int(course_num)
for_my_iteration = num
p = 0

while num >= 0:
    p += 1
    sleep(0.8)
    course_name_input = (input('\n' + 'Input the Title of the ' + engine().ordinal(p) + ' course here: '))
    course_name = course_name_input.upper()
    sleep(0.5)
    credit_load_input = input('\n' + 'Input the course credit load: ')
    course_credit_load = input_check_credit_load(credit_load_input)
    sleep(0.5)

    score_input = input('\n' + 'Input your score or grade: ')
    scored = grade_check(score_input)

    course_n_points = calculate_point(course_name, course_credit_load, scored)
    # print(course_n_points)
    num -= 1
    if num == 0:
        t_points = []
        c_points = []
        for i in range(for_my_iteration):
            t_points.append(list(course_n_points.values())[i][(i*3)+2])
            c_points.append(list(course_n_points.values())[i][i*3])
        # print(t_points)
        total_points = sum(t_points)
        sum_credit_load = sum(c_points)
        cgpa = total_points / sum_credit_load
        # print(cgpa)
        cgpa_r = round(cgpa, 2)
        # print(cgpa_r)
        cgpa_f = int(cgpa_r*100)
        # print(cgpa_f)

        if cgpa_f in range(450, 501):
            degree = ' FIRST CLASS'
        elif cgpa_f in range(350, 450):
            degree = 'SECOND CLASS UPPER'
        elif cgpa_f in range(250, 350):
            degree = 'SECOND CLASS LOWER'
        elif cgpa_f in range(200, 250):
            degree = 'THIRD CLASS'
        elif cgpa_f in range(150, 200):
            degree = 'PASS'
        elif cgpa_f in range(000, 150):
            degree = 'ATTENDED'
        else:
            degree = 'Not a student'

        # print(course_n_points)
        to_be_printed = 'nothing in here'
        for i in range(for_my_iteration):
            i_name = list(course_n_points.keys())[i]
            i_grade = list(course_n_points.values())[i][(i*3)+1]
            # print(i_grade)
            aggregate = list(course_n_points.values())[i][(i*3)+2]
            # print(aggregate)
            to_be_printed = 'Course: ' + i_name + '\n' + 'grade: ' + str(i_grade) + '\n' + 'Aggregate: ' + str(aggregate)
            sleep(1.5)
            print('\n' + '------------------------')
            print(to_be_printed)
            print('------------------------')
        sleep(3)
        print('\n' + 'Your CGPA is:')
        sleep(1)
        print('*************************')
        print('        ' + str(cgpa_r) + '  ')
        print('****' + degree + '****')
        print('*************************')
        break






