#include <arpa/inet.h>
#include <asm-generic/errno.h>
#include <ctype.h>
#include <dirent.h>
#include <errno.h>
#include <fcntl.h>
#include <netinet/in.h>
#include <pthread.h>
#include <regex.h>
#include <signal.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <unistd.h>

#include "server.h"

#define RETURN_IF_ERROR(code)                                                  \
  ({                                                                           \
    if (code < 0) {                                                            \
      log_error_code(code);                                                    \
      return code;                                                             \
    }                                                                          \
  })

#define RETURN_CODE_IF_ERROR(code, propagated_code)                            \
  ({                                                                           \
    if (code < 0) {                                                            \
      log_error_code(code);                                                    \
      return propagated_code;                                                  \
    }                                                                          \
  })

int server_fd;

void log_error_code(int code) {
  if (ERROR_LOGGING_ENABLED && code < 0) {
    printf("LOG - ERROR CODE: ");
    switch (code) {
    case EADDRINUSE:
      printf("EADDRINUSE");
    default:
      printf("UNKOWN ERROR CODE (%d)", code);
    }
    printf("\n");
  };
}

int setup_server(int port_number) {
  struct sockaddr_in server_addr;

  // create server socket
  server_fd = socket(AF_INET, SOCK_STREAM, 0);
  RETURN_CODE_IF_ERROR(server_fd, ERR_CODE_SOCKET_FAILED);
	RETURN_CODE_IF_ERROR(
			setsockopt(server_fd, SOL_SOCKET, SO_REUSEADDR, &(int){1}, sizeof(int)),
			ERR_CODE_SET_SOCKET_PROP_FAILED);

  // config socket
  server_addr.sin_family = AF_INET;
  server_addr.sin_addr.s_addr = INADDR_ANY;
  server_addr.sin_port = htons(port_number);

  RETURN_CODE_IF_ERROR(
      bind(server_fd, (struct sockaddr *)&server_addr, sizeof(server_addr)),
      ERR_CODE_BIND_FAILED);

  RETURN_CODE_IF_ERROR(listen(server_fd, SOCKET_MAX_QUEUE),
                       ERR_CODE_LISTEN_FAILED);

  return 0;
}

void *handle_client(void *arg) {
  int client_fd = *((int *)arg);
  printf("RECEIVED SOMETHING\n");
  free(arg);
  return NULL;
}

int run_server(int *request_count) {
  while (1) {
    // client info
    struct sockaddr_in client_addr;
    socklen_t client_addr_len = sizeof(client_addr);
    int *client_fd = malloc(sizeof(int));

    // accept client connection
    if ((*client_fd = accept(server_fd, (struct sockaddr *)&client_addr,
                             &client_addr_len)) < 0) {
      perror("accept failed");
      continue;
    }

    // create a new thread to handle client request
    pthread_t thread_id;
    pthread_create(&thread_id, NULL, handle_client, (void *)client_fd);
    pthread_detach(thread_id);
    (*request_count)++;
  }

  return 0;
}

int clean_up_server() {
  RETURN_CODE_IF_ERROR(close(server_fd), ERR_CODE_CLOSE_FAILED);

  return 0;
}

void sigint_callback() {
  log_error_code(clean_up_server());
  exit(0);
}

// Returns error code or the number of requests it successfully handled
int start_server(int port_number) {
  int request_count = 0;

  signal(SIGINT, sigint_callback);

  // Setup
  RETURN_IF_ERROR(setup_server(port_number));

  // Run server
  RETURN_IF_ERROR(run_server(&request_count));

  // Close connection
  RETURN_IF_ERROR(clean_up_server());

  return request_count;
}
