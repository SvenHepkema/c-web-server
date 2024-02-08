#!/usr/bin/python3

import interop

port_number = 8080

print(f"Starting server on port {port_number}")

n_requests = interop.start_server(port_number)

print(f"Handled {n_requests} requests.")
