// ================
// CONSTANTS
// ================

// General
const bool ERROR_LOGGING_ENABLED = true;
const int SOCKET_MAX_QUEUE = 10;

// Error codes
const int ERR_CODE_UNKNOWN = -1;
const int ERR_CODE_SOCKET_FAILED = -2;
const int ERR_CODE_BIND_FAILED = -3;
const int ERR_CODE_LISTEN_FAILED = -4;
const int ERR_CODE_CLOSE_FAILED = -5;
const int ERR_CODE_SET_SOCKET_PROP_FAILED = -6;

// ================


int start_server(int port_number);
