import ctypes

c_library = ctypes.CDLL('./library.so')

c_library.sumAll.argtypes = (ctypes.c_int,)

def sumAll(x):
    global c_library
    return c_library.sumAll(
        ctypes.c_int(x)
    )

def sumAll_python(x):
    return sum(
        range(x+1)
    )
