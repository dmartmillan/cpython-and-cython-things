# cy_parser.pyx
# cython: boundscheck=False, wraparound=False

from typing import Generator, Tuple, List


def c_base_parser(object mm_obj, str file_path):
    """
    Cython-accelerated parser for processing file lines.
    """
    # Precompute the delimiter value
    cdef str delim = "\t"

    cdef int l_num = 0
    cdef bytes line
    cdef str line_str, first_field
    cdef list row_line
    cdef tuple result

    while True:
        line = mm_obj.readline()
        if not line:
            break
        # Remove the trailing newline efficiently
        line = line.rstrip(b'\n')

        line_str = line.decode("utf-8")

        yield l_num, line_str
        l_num += 1
