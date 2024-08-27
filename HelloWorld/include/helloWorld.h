#ifndef HELLOWORLD_H
#define HELLOWORLD_H

#include <string>

void message(const std::string& msg);

extern "C" {

void message(const char* msg);

}

#endif
