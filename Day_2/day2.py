import helper_functions


def diff_list(report: list) -> list:
    diff_list = []
    for i in range(0, len(report)-1):
        diff_list.append(int(report[i+1]) - int(report[i]))
    return diff_list


def values_smaller_four(value_list) -> list[bool]:
    bool_list : list[bool] = []
    for value in value_list:
        bool_list.append(abs(value) < 4)
    return bool_list


def is_continous(value_list) -> bool:
    is_pos = False
    is_neg = False
    for value in value_list:
        if value > 0:
            is_pos = True
        elif value < 0:
            is_neg = True
        else:
            return False

        if is_neg and is_pos:
            return False

    return True


def does_cutting_one_number_help(report: list) -> bool:
    print("Im trying: ", report)
    for i in range(len(report)):
        report_copy = report.copy()
        popped_number = report_copy.pop(i)
        print("popping: ", popped_number, "at Index: ", i)
        diff = diff_list(report_copy)
        print("diff: ", diff)
        if is_safe(report_copy):
            print("Did work!!!")
            return True
    print("Didnt work :/")
    return False


def is_safe(report: list) -> bool:
    diff = diff_list(report)
    if 0 in diff:
        return False
    elif False in values_smaller_four(diff):
        return False
    elif not is_continous(diff):
        return False
    return True


def is_damped_safe(report: list) -> bool:
    diff = diff_list(report)
    if 0 in diff:
        print("Trying to find solution for because 0: ", report)
        print("Diff: ", diff)
        return does_cutting_one_number_help(report)
    elif False in values_smaller_four(diff):
        print("Trying to find solution for because >3: ", report)
        print("Diff: ", diff)
        return does_cutting_one_number_help(report)
    elif not is_continous(diff):
        print("Trying to find solution for because continuity: ", report)
        print("Diff: ", diff)
        return does_cutting_one_number_help(report)
    return True


def solve():
    input_text: str = helper_functions.read_in_file(2)
    reports = input_text.splitlines()
    reports_with_levels = [report.split() for report in reports]
    safe_reports: int = 0
    for report in reports_with_levels:
        if is_damped_safe(report):
            safe_reports += 1
    print(safe_reports)

