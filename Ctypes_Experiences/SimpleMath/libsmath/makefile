# Makefile

CC = g++
CFLAGS = -fPIC -Iinclude
LDFLAGS = -shared
LIBDIR = lib
LIBNAME = libsmath.so
SRCDIR = src
INCLUDEDIR = include
TARGET = $(LIBDIR)/$(LIBNAME)
SRCS = $(SRCDIR)/smath.c

all: $(TARGET)

$(TARGET): $(SRCS)
	$(CC) $(CFLAGS) $(LDFLAGS) -o $@ $^

clean:
	rm -f $(TARGET)
