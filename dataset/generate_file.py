import random
import string

def generate_utf8_file(size_in_mb, file_name):
    target_size = size_in_mb * 1_000_000  # Total target size in characters
    line_length = 100  # Length of each line in characters
    # Each line has an extra newline character, so account for that in the size
    num_lines = target_size // (line_length + 1)
    characters = string.ascii_letters + string.digits + string.punctuation + " "

    with open(file_name, 'w', encoding='utf-8') as file:
        for _ in range(int(num_lines)):
            random_line = ''.join(random.choices(characters, k=line_length))
            file.write(random_line + "\n")

# Size in MB
SIZE = 10000
generate_utf8_file(SIZE, "example2.txt")