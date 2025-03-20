def regular_io(filename):
    with open(filename, mode="r", encoding="utf8") as file_obj:
        while line := file_obj.readline():
            yield line

