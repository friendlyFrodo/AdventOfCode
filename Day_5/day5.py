import helper_functions
from collections import Counter
from functools import cmp_to_key


THE_RULES = []

def does_rule_apply_for_first_number(order: list[str], rules: list[str]) -> bool:
    first_string = order.pop(0)
    for test_string in order:
        if f"{test_string}|{first_string}" in rules:
            return False
    return True

def applyRules(a: str,b: str):
    global THE_RULES
    if f"{a}|{b}" in THE_RULES:
        return 1
    return -1



def countForCorrectPages(print_orders: list[str], rules: list[str]) -> int:
    count = 0
    for order in print_orders:
        split_order = order.split(',')
        while len(split_order) > 0:
            if not does_rule_apply_for_first_number(split_order, rules):
                break
            elif len(split_order) == 0:
                split = order.split(',')
                print(len(split))
                print(int(len(split) / 2 - 0.5))
                count += int(split[int(len(split) / 2 - 0.5)])
                break
            else:
                split_order.pop(0)
    print(count)


def makeCorrectOrder(print_orders: list[str], rules: list[str]) -> list[str]:
    print_orders.sort(key=cmp_to_key(applyRules))
    return print_orders

def countForWrongPages(print_orders: list[str], rules: list[str]) -> int:
    count = 0
    for order in print_orders:
        split_order = order.split(',')
        while len(split_order) > 0:
            if not does_rule_apply_for_first_number(split_order, rules):
                print("Current wrong order: ", order.split(','))
                correctOrder = makeCorrectOrder(order.split(','), rules)
                print("The found correct order: ", correctOrder)
                assert order.split(',') != correctOrder, ("Die richtig sortierte Ordnung ist gleich der falsch "
                                                          "sortierten Ordnung")
                assert Counter(order.split(',')) == Counter(correctOrder), "Lists do not contain the same elements"
                middleNumber = int(correctOrder[int(len(correctOrder) / 2 - 0.5)])
                print("middle Number: ", middleNumber)
                count += middleNumber
                break
            elif len(split_order) == 0:
                break
            else:
                split_order.pop(0)
    return count


def solve():
    input_text: str = helper_functions.read_in_file(5)
    lines: list[str] = input_text.splitlines()
    rules: list[str] = []
    print_orders: list[str] = []
    for line in lines:
        if "|" in line:
            rules.append(line)
        elif line == "":
            continue
        else:
            print_orders.append(line)

    global THE_RULES
    THE_RULES = rules
    print(countForWrongPages(print_orders, rules))
