#include "../include/helloWorld.h"

#include <iostream>


void message(const std::string &msg)
{
    std::cout << "Message: " << msg << '\n';
}

void message(const char *msg)
{
    return message(std::string(msg));
}
