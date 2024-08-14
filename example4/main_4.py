import time

import ctypes

code = ctypes.CDLL('./main_4.so')

code.fib.argtypes = (ctypes.c_int,)
code.fib.restype = ctypes.c_int

n = 35  # N-ni aniqlash # noqa


# Fibonacci sonini Python'da hisoblash # noqa
def python_fib(n):
    if n <= 1:
        return n
    return python_fib(n - 1) + python_fib(n - 2)


# 1. Python kodini sinash # noqa
start_time = time.time()
python_result = python_fib(n)
python_time = time.time() - start_time
print(f"Python'da vaqt: {python_time:.6f} soniya, Natija: {python_result}")  # noqa

# 2. C kodini sinash # noqa
start_time = time.time()
c_result = code.fib(n)
c_time = time.time() - start_time
print(f"C'da vaqt: {c_time:.6f} soniya, Natija: {c_result}")  # noqa

# Vaqt farqini chiqaramiz # noqa
print(f"C kodining tezligi Python'dan {python_time / c_time:.2f} marta tezroq")  # noqa
