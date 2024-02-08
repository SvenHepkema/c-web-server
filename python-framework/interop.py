import ctypes
from typing import List

lib = ctypes.cdll.LoadLibrary('../c-server/target/libserver.so')

# ======================================

class UrlPath:
    def __init__(self, url, response):
        self.url = url
        self.response = response

    def register(self) -> None:
        lib.python_register_url(bytes(self.url, 'utf-8'), bytes(self.response, 'utf-8'))


    def __repr__(self) -> str:
        return f"UrlPath '{self.url}' returning: {self.response}"

def start_server(port_number: int, paths: List[UrlPath]) -> int:
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
        -6: "Setting a socket prop failed",
    }

    result = lib.setup_server(port_number)

    for path in paths:
        path.register()

    if result in error_codes.keys():
        raise Exception(f"Server setup failed due to: {error_codes[result]}")

    result = lib.start_server()

    if result in error_codes.keys():
        raise Exception(f"Server failed due to: {error_codes[result]}")
    return result


lib.setup_server.argtypes = [
    ctypes.c_int32,
]
lib.setup_server.restype = ctypes.c_int32

lib.python_register_url.argtypes = [
    ctypes.c_char_p,
    ctypes.c_char_p,
]
lib.python_register_url.restype = ctypes.c_int32

lib.start_server.argtypes = [ ]
lib.start_server.restype = ctypes.c_int32
