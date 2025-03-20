
from cy_parser import c_base_parser

def mmap_cython(filename):
    for x in  c_base_parser(filename):
        yield x