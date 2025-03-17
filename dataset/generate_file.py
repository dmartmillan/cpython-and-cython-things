import random
import string

def generate_utf8_file(size_in_mb, file_name):
    mega_byte = 1_000_000  # Approximate size of 1MB in characters
    chars_per_mb = mega_byte   # Each UTF-8 character takes ~2 bytes on average

    with open(file_name, 'w', encoding='utf-8') as file:
        for _ in range(size_in_mb):
            random_text = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation + " ", k=chars_per_mb))
            file.write(random_text)

# Size in MB
SIZE = 1024
generate_utf8_file(SIZE, "example.txt")