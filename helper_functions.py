def read_in_file(day: int) -> str:
    file = open(f'Day_{day}/input.txt', 'r')

    # Read the entire file
    content = file.read()

    # Don't forget to close the file
    file.close()
    return content


