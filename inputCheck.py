def the_input_str(input_str):
    return input(input_str)


def input_check_course_int(input_val):
    try:
        input_value = int(input_val)
        return input_value
    except Exception:
        print('WARNING: Your Input should be a number not a letter!!!')
    another_input = the_input_str('\n' + 'Please input correct TOTAL number of courses: ')
    return input_check_course_int(another_input)


def input_check_credit_load(input_val):
    try:
        input_value = int(input_val)
        return input_value
    except Exception:
        print('WARNING: Your Input should be a number not a letter!!!')
    another_inp = the_input_str('\n' + 'Input the course credit load again: ')
    return input_check_credit_load(another_inp)



