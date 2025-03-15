import time
import count_module


# Pure Python generator function
def python_count_up_to(max_value):
    count = 1
    while count <= max_value:
        yield count
        count += 1


# Benchmarking function
def benchmark(generator_func, max_value):
    start_time = time.perf_counter()
    for _ in generator_func(max_value):
        pass
    end_time = time.perf_counter()

    return end_time - start_time


# Set a high number for performance comparison
MAX_COUNT = 1e9

# Benchmark CPython C extension generator
c_time = benchmark(count_module.count_up_to, MAX_COUNT)
print(f"CPython C extension time: {c_time:.6f} seconds")

# Benchmark pure Python generator
python_time = benchmark(python_count_up_to, MAX_COUNT)
print(f"Pure Python generator time: {python_time:.6f} seconds")

# Speedup factor
if python_time > 0:
    speedup = python_time / c_time
    print(f"Speedup: {speedup:.2f}x faster with C extension")
