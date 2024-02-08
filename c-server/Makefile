CC=gcc
FLAGS=-O3

SRC_DIR=src
OBJ_DIR=obj
TARGET_DIR=target

.PHONY: clean

libserver: $(OBJ_DIR)/server.o
	$(CC) -shared $(OBJ_DIR)/server.o -o $(TARGET_DIR)/$@.so $(FLAGS) 

%.o: $(SRC_DIR)/server.c
	$(CC) -c -o $@ $< $(FLAGS) -fPIC

program: $(SRC_DIR)/main.c $(OBJ_DIR)/server.o $(SRC_DIR)/server.h
	$(CC) $(SRC_DIR)/main.c $(OBJ_DIR)/server.o -o $(TARGET_DIR)/$@ $(FLAGS)

clean:
	rm obj/*
	rm target/*
