import time

def measure_runtime(function, *args, **kwargs):
    start = time.time()
    function(*args, **kwargs)
    end = time.time()
    return end - start