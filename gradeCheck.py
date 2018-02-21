def the_input_str(input_str):
    inp = input(input_str)
    return inp


def grade_check(score_input):
    try:
        if score_input in ['a', 'b', 'c', 'd', 'e', 'f']:
            return score_input.upper()
        else:
            scored = int(score_input)
            return scored
    except Exception:
        print('Your Input is Invalid')
        another_input = the_input_str('Input your score or grade: ')
    return grade_check(another_input)


point_array = {}
course_details_array = []


def calculate_point(name, credit_load, score):
    points = ''
    grade = ''
    if score in range(70, 100) or score == 'A':
        points = 5 * credit_load
        grade = 'A'
    elif score in range(60, 69) or score == 'B':
        points = 4 * credit_load
        grade = 'B'
    elif score in range(50, 59) or score == 'C':
        points = 3 * credit_load
        grade = 'C'
    elif score in range(45, 49) or score == 'D':
        points = 2 * credit_load
        grade = 'D'
    elif score in range(40, 44) or score == 'E':
        points = 1 * credit_load
        grade = 'E'
    elif score in range(0, 39) or score == 'F':
        points = 0 * credit_load
        grade = 'F'
    else:
        print('The score input is invalid')

    course_details_array.append(credit_load)
    course_details_array.append(grade)
    course_details_array.append(points)
    point_array[name] = course_details_array
    return point_array
