import ctypes

c_library = ctypes.CDLL('./out.so')

c_library.sumAll.argtypes = (ctypes.c_int,)

def sumAll(x):
    global c_library
    return c_library.sumAll(
        ctypes.c_int(x)
    )
