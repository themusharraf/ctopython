import time

import ctypes

code = ctypes.CDLL('./main_3.so')

code.sum_array.restype = ctypes.c_int

arr = list(range(1, 1000001))  # 1,000,000 elementli massiv # noqa
arr_len = len(arr)

# C tilidagi massivni yaratish uchun Python massivini ctypes massiviga o'giramiz # noqa
c_array = (ctypes.c_int * arr_len)(*arr)

# 1. Python kodini sinash  # noqa
start_time = time.time()
python_sum = sum(arr)
python_time = time.time() - start_time
print(f"Python'da vaqt: {python_time:.6f} soniya")  # noqa

# 2. C kodini sinash # noqa
start_time = time.time()
c_sum = code.sum_array(c_array, arr_len)
c_time = time.time() - start_time
print(f"C'da vaqt: {c_time:.6f} soniya")  # noqa

# Vaqt farqini chiqaramiz # noqa
print(f"C kodining tezligi Python'dan {python_time / c_time:.2f} marta tezroq")  # noqa
