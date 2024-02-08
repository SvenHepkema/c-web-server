import ctypes

lib = ctypes.cdll.LoadLibrary('../c-server/target/libserver.so')

# ======================================

def start_server(port_number: int) -> int:
    """ 
    Starts a server listenting on the specified port number and 
    returns the amount of requests handled.

    If the amount of handled requests is negative, the server crashed,
    """
    error_codes = {
        -1: "Unkown error",
        -2: "Socket failed",
        -3: "Bind failed",
        -4: "Listen failed",
        -5: "Closing the server fd failed",
    }

    result = lib.start_server(port_number)

    if result in error_codes.keys():
        print(f"!!!!! {result} !!!!!!")
        raise Exception(f"Server failed due to: {error_codes[result]}")
    else:
        return result


lib.start_server.argtypes = [
    ctypes.c_int32,
]
lib.start_server.restype = ctypes.c_int32
