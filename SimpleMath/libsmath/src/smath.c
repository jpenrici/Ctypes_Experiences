#include "../include/smath.h"

#include <stdio.h>

double add(double first, double second)
{
    return first + second;
}

double subtract(double first, double second)
{
    return first - second;
}

double multiply(double first, double second)
{
    return first * second;
}

double divide(double first, double second)
{
    return first / (second == 0 ? 1 : second);
}

const char* info()
{
    return "SMath library!";
}
