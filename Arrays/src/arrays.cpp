#include "../include/arrays.h"

auto myArray() -> std::array<int, 10>
{
    return {10, 20, 30, 40, 50, 60, 70, 80, 90, 100};
}

auto myarray() -> int *
{
    return myArray().data();
}
