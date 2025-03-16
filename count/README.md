#### count module

```commandline
python3 setup.py build_ext --inplace
pyhton3 throw.py
```

```text
For 10000000000.0 as max value:
CPython C extension time: 178.526327 seconds
Pure Python generator time: 451.412966 seconds
Speedup: 2.53x faster with C extension
```

#### Performance comparison

Linear scale

![linear comparison](performance_comparison.png)

Logarithmic scale

![log comparison](performance_comparison_log.png)
