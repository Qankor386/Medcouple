import time

def measure_runtime(function):
    start = time.time()
    function()
    end = time.time()

    return end - start