import time
from regular_io import regular_io
from mmap_io import mmap_io
import mmap_module

# Benchmarking function
def benchmark(generator_func, filename):
    start_time = time.perf_counter()
    for _ in generator_func(filename):
        pass
    end_time = time.perf_counter()

    return end_time - start_time

FILENAME = "../dataset/example.txt"

# Benchmark Regular I/O
c_time = benchmark(regular_io, FILENAME)
print(f"Regular I/O time: {c_time:.6f} seconds")

# Benchmark mmap I/O
python_time = benchmark(mmap_io, FILENAME)
print(f"mmap I/O time: {python_time:.6f} seconds")

# Benchmark mmap I/O with C extension
python_time = benchmark(mmap_module.mmap_io, FILENAME)
print(f"mmap I/O with C extension time: {python_time:.6f} seconds")
