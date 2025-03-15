# Playing with CPython

```commandline
python3 setup.py build_ext --inplace
pyhton3 throw.py
```

For `MAX_COUNT = 1e9`

```text
CPython C extension time: 26.769842 seconds
Pure Python generator time: 34.367606 seconds
Speedup: 1.28x faster with C extension
```

