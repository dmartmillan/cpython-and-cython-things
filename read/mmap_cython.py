import mmap

from cy_parser import c_base_parser

def mmap_cython(filename):
    with open(filename, "rb") as f:
        mm_obj = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
        yield c_base_parser(mm_obj, filename)
