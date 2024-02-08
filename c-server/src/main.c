#include <stdio.h>
#include <stdbool.h>

#include "server.h"


int main() {
	setup_server(8080);
	start_server();
}
