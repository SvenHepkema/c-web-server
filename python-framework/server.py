import ctypes

lib = ctypes.cdll.LoadLibrary('../c-server/target/libserver.so')

class Server:
    def _check_result(self, code: int, action: str) -> int:
        error_codes = {
            -1: "Unkown error",
            -2: "Socket failed",
            -3: "Bind failed",
            -4: "Listen failed",
            -5: "Closing the server fd failed",
            -6: "Setting a socket prop failed",
        }

        if code in error_codes.keys():
            raise Exception(f"{action} failed due to: {error_codes[code]}")

        return code 


    def __init__(self, port: int=8080):
        self.port = port
        self.pages = []

        self._check_result(lib.setup_server(self.port), "Server startup")


    def get_url_root(self) -> str:
        return f"localhost:{self.port}"


    def start(self):
        """ 
        Starts a server listenting on the specified port number and 
        returns the amount of requests handled.

        If the amount of handled requests is negative, the server crashed,
        """

        print(f"Started the server on port {self.port}. The paths below are available:")
        for page in self.pages:
            print(page.get_full_url())

        self._check_result(lib.start_server(), "Server")


    def register(self, page) -> None:
        lib.python_register_url(bytes(page.url, 'utf-8'), bytes(page.response, 'utf-8'))
        self.pages.append(page)



class UrlPath:
    def __init__(self, server: Server, url: str, response: str):
        self.server = server
        self.url = url
        self.response = response


    def get_full_url(self) -> str:
        return f"{self.server.get_url_root()}/{self.url}"


    def __repr__(self) -> str:
        return f"UrlPath '{self.url}' returning: {self.response}"

    def register(self):
        self.server.register(self)
        return self



class HtmlPage(UrlPath):
    def __init__(self, server: Server, url: str):
        self.server = server
        self.url = url
        self.response = ""


    def header(self, text: str):
        self.response += f"<h1>{text}</h1>"
        return self


    def subheader(self, text: str):
        self.response += f"<h4>{text}</h4>"
        return self


    def paragraph(self, text: str):
        self.response += f"<p>{text}</p>"
        return self


    def link_button(self, text: str, page):
        self.response += f"<a href=\"{page.url}\" class=\"button\">"
        self.response += f"<button>{text}</button></a>"
        return self


    def any(self, html: str):
        self.response += html
        return self



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
