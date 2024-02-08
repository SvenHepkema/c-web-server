import ctypes

lib = ctypes.cdll.LoadLibrary('../c-server/target/libserver.so')

# ======================================

def add(a: int, b: int) -> int:
    return lib.add(a, b)

lib.add.argtypes = [
    ctypes.c_int32,
    ctypes.c_int32,
]
lib.add.restype = ctypes.c_int32


# ======================================

def start_server(port_number: int) -> int:
    """ 
    Starts a server listenting on the specified port number and 
    returns the amount of requests handled.
    """
    return lib.start_server(port_number)

lib.add.argtypes = [
    ctypes.c_int32,
]
lib.add.restype = ctypes.c_int32
