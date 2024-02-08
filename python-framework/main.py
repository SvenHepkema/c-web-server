#!/usr/bin/python3

import interop

a = 1
b = 2
print(f"Adding {a} and {b} results in: {interop.add(a, b)}")

port_number = 8080

print(f"Starting server on port {port_number}")

n_requests = interop.start_server(port_number)

print(f"Handled {n_requests} requests.")
