import sys


def apply_operations(nums, op_int):
    result = str(nums[0])  # Start with the first number, converting it to a string for concatenation.

    num_operations = len(nums) - 1

    # Iterate over each adjacent pair of numbers
    for i in range(1, len(nums)):
        # Extract the operation from the binary representation of op_int
        operation = (op_int // (3 ** (i - 1))) % 3

        if operation == 0:  # Addition
            result = int(result) + nums[i]
        elif operation == 1:  # Multiplication
            result = int(result) * nums[i]
        elif operation == 2:  # Concatenation
            result = int(str(result) + str(nums[i]))

    return result


def generate_results(nums):
    n = len(nums)
    results = []

    # There are 3^(n-1) possible combinations of operations
    num_operations = n - 1
    for op_int in range(3 ** num_operations):
        result = apply_operations(nums, op_int)
        results.append(result)

    return results
def print_line_by_line():
    for line in equations:
        print(line)

with open(sys.argv[1], 'r') as f:
    lines = list(map(str.strip, f.readlines()))


equations = [[int(line.split(':')[0]), [int(i) for i in line.split(':')[1].split()]] for line in lines]


part1 = 0
for equation in equations:
    results = generate_results(equation[1])
    if equation[0] in results:
        part1 += equation[0]


print(f'Part 1: {part1}')

part2 = ""
print(f'Part 2: {part2}')