import ctypes

lib = ctypes.cdll.LoadLibrary('../c-server/target/libserver.so')
lib.add.argtypes = [
    ctypes.c_int32,
    ctypes.c_int32,
]
lib.add.restype = ctypes.c_int32

def add(a: int, b: int) -> int:
    return lib.add(a, b)
