

def calculate_horizontal_depth_position(filename):
    values_list = []
    result = 0
    horizontal = 0
    depth = 0

    with open(filename, 'r', encoding='utf-8') as values:
        for value in values:
            values_list.append(value.strip("\n"))

    for value in values_list:
        direction, number = value.split(" ")[0], int(value.split(" ")[1])
        if direction == "forward":
            horizontal += number
        elif direction == "up":
            depth -= number
        elif direction == "down":
            depth += number

    return horizontal * depth
