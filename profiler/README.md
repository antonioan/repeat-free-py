
# Profiler Usage

####1
To run profiler, run from the **Terminal**:
```shell script
python -m cProfile -o profiler/profiler.out main.py
```

####2
To analyze results, run from the **Python Console**:
```python
import pstats
import contextlib
with open('profiler.out.txt','w') as f:
    with contextlib.redirect_stdout(f):
        p = pstats.Stats('profiler/profiler.out')
        p.sort_stats('cumulative').print_stats(30)
```
