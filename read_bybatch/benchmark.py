import time
from mmap_io import mmap_io
from mmap_io_batch import mmap_io_batch

# Benchmarking function
def benchmark(generator_func, filename):
    start_time = time.perf_counter()
    for _ in generator_func(filename):
        pass
    end_time = time.perf_counter()

    return end_time - start_time

FILENAME = "../dataset/example2.txt"


# Benchmark mmap I/O
python_time = benchmark(mmap_io, FILENAME)
print(f"mmap I/O time: {python_time:.6f} seconds")

# Benchmark mmap with batch I/O
#python_time = benchmark(mmap_io_batch, FILENAME)
#print(f"mmap I/O with batch time: {python_time:.6f} seconds")
