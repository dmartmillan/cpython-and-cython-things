import time
from mmap_io import mmap_io
from mmap_io_np import mmap_io_np
from mmap_io_concurrent_future import mmap_io_concurrent

# Benchmarking function
def benchmark(generator_func, filename):
    start_time = time.perf_counter()
    for x in generator_func(filename):
        pass
    end_time = time.perf_counter()

    return end_time - start_time

FILENAME = "../dataset/example2.txt"


# Benchmark mmap I/O operation by line
python_time = benchmark(mmap_io, FILENAME)
print(f"mmap I/O operation by line time: {python_time:.6f} seconds")

# Benchmark mmap I/O operation with numpy
python_time = benchmark(mmap_io_np, FILENAME)
print(f"mmap I/O operation with Numpy time: {python_time:.6f} seconds")

# Benchmark mmap I/O operation with parallel tasks
python_time = benchmark(mmap_io_concurrent, FILENAME)
print(f"mmap I/O operation by parallel tasks time: {python_time:.6f} seconds")
