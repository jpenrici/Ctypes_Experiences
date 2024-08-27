#ifndef ARR_H
#define ARR_H

#include <array>

auto myArray() -> std::array<int, 10>;

extern "C" {

auto myarray() -> int *;

}

#endif
