import helper_functions
def solve():
    input_text: str = helper_functions.read_in_file(1)
    input_lines: list[str] = input_text.splitlines()
    list1 : list[int] = []
    list2 : list[int] = []

    for line in input_lines:
        list1.append(int(line.split()[0]))
        list2.append(int(line.split()[1]))

    list1.sort()
    list2.sort()

    diff_score:int = 0

    for i in range(0,min(len(list1),len(list2))):
        diff : int = abs(list1[i]-list2[i])
        diff_score += diff

    print("solution part a: ", diff_score)

    number:int
    similarity_score:int = 0
    for number in list1:
        similarity_score += number * list2.count(number)

    print("solution part b: ",similarity_score)




