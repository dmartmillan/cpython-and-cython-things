# Pure Python generator function
def python_count_up_to(max_value):
    count = 1
    while count <= max_value:
        yield count
        count += 1
