import mmap
import numpy as np

def operation(line):
    line = line.decode('utf-8')
    return line.replace("0", "o")

CHUNK_SIZE = 20

def mmap_io_np(filename):
    chunk_lines = []

    func_vec = np.vectorize(operation)
    with open(filename, mode="r", encoding="utf8") as file_obj:
        with mmap.mmap(file_obj.fileno(), length=0, access=mmap.ACCESS_READ) as mmap_obj:
            for line in iter(mmap_obj.readline, b''):
                chunk_lines.append(line)
                if len(chunk_lines) == CHUNK_SIZE:
                    yield func_vec(chunk_lines)
                    chunk_lines = []