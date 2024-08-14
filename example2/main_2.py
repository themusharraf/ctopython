import ctypes

code = ctypes.CDLL("./main_2.so")

print(code.add(25, 30))
