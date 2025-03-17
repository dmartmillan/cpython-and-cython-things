import time
import count_module
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from count_python import python_count_up_to


# Benchmarking function
def benchmark(generator_func, max_value):
    start_time = time.perf_counter()
    for _ in generator_func(max_value):
        pass
    end_time = time.perf_counter()

    return end_time - start_time


# Set a high number for performance comparison
MAX_COUNT = 1e10
print(f"For {MAX_COUNT} as max value:")

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

c_times = []
python_times = []

max_counts = [10**x for x in range(1, 13)]

for max_count in max_counts:
    print(f"Benchmarking for {max_count} iterations...")

    # Benchmark CPython C extension generator
    c_time = benchmark(count_module.count_up_to, max_count)
    c_times.append(c_time)

    # Benchmark pure Python generator
    python_time = benchmark(python_count_up_to, max_count)
    python_times.append(python_time)
    print(f"{c_time:.6f} - {python_time:.6f}")

max_counts = np.array(max_counts)
c_times = np.array(c_times)
python_times = np.array(python_times)

# Plot the results
sns.set_style("whitegrid")
plt.figure(figsize=(10, 6))

plt.plot(max_counts, c_times, label="C Extension", marker="o", linestyle="-")
plt.plot(max_counts, python_times, label="Pure Python", marker="s", linestyle="--")

plt.xlabel("Max Count")
plt.ylabel("Execution Time (seconds)")
plt.title("Performance Comparison: C Extension vs Pure Python")
plt.legend()

plot_filename = "./performance_comparison.png"
plt.savefig(plot_filename, dpi=300)
plt.show()

sns.set_style("whitegrid")
plt.figure(figsize=(10, 6))

plt.plot(max_counts, c_times, label="C Extension", marker="o", linestyle="-")
plt.plot(max_counts, python_times, label="Pure Python", marker="s", linestyle="--")

plt.xscale("log")
plt.yscale("log")
plt.xlabel("Max Count (log scale)")
plt.ylabel("Execution Time (seconds, log scale)")
plt.title("Performance Comparison: C Extension vs Pure Python")
plt.legend()

plot_filename = "./performance_comparison_log.png"
plt.savefig(plot_filename, dpi=300)
plt.show()
