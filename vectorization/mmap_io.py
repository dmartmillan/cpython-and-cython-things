import mmap

def mmap_io(filename):
    with open(filename, mode="r", encoding="utf8") as file_obj:
        with mmap.mmap(file_obj.fileno(), length=0, access=mmap.ACCESS_READ) as mmap_obj:
            for line in iter(mmap_obj.readline, b''):
                line = line.decode('utf-8')
                line = line.replace("0", "o")
                yield line
