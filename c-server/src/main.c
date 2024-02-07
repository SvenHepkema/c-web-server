#include <stdio.h>
#include "server.h"


int main() {
	int a = 1, b = 2;
	printf("Result of adding %d and %d: %d\n", a, b, add(a, b));
}
