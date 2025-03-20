# cy_parser.pyx
# cython: boundscheck=False, wraparound=False

import mmap
from typing import Generator, Tuple, List

def c_base_parser(str file_path):
    """
    Cython-accelerated parser for processing file lines.
    """

    cdef bytes line

    with open(file_path, 'rb') as file_obj:
        with mmap.mmap(file_obj.fileno(), length=0, access=mmap.ACCESS_READ) as mmap_obj:
            while True:
                line = mmap_obj.readline()
                if not line:
                    break
                yield line
