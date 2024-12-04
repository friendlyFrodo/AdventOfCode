import helper_functions
import re


def solve():
    input_text: str = helper_functions.read_in_file(3)
    print(input_text)
    # Define the corrected regex pattern
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don\'t\(\)"

    # Find all matches using re.finditer (returns match objects)
    matches = re.finditer(pattern, input_text)

    # Process the matches to clean empty strings for do() and don't()
    processed_matches = []

    for match in matches:
        # Check if the match is for 'mul(...)'
        if match.group(1) and match.group(2):  # mul(<1-3 digits>,<1-3 digits>)
            # Extract the two values inside the parentheses
            value1 = match.group(1)  # First value (e.g., '12' from 'mul(12,34)')
            value2 = match.group(2)  # Second value (e.g., '34' from 'mul(12,34)')

            processed_matches.append((value1, value2))  # Full match, e.g., 'mul(12,34)'
        elif 'do' in match.group(0):  # For 'do()' or 'don't()'
            processed_matches.append(match.group(0))  # Append the exact match: 'do()' or "don't()"

    # Print the cleaned-up matches
    print(processed_matches)
    summe: int = 0
    multiplier: int = 1
    for processed_match in processed_matches:
        if "do()" in processed_match:
            multiplier = 1
        elif "don't()" in processed_match:
            multiplier = 0
        else:
            processed_match = tuple(processed_match)
            summe += int(processed_match[0]) * int(processed_match[1]) * multiplier

    print(summe)
