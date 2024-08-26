#include "../include/smath.h"

auto add(double first, double second) -> double
{
    return SMath::add<double>(first, second);
}

auto subtract(double first, double second) -> double
{
    return SMath::subtract<double>(first, second);
}

auto multiply(double first, double second) -> double
{
    return SMath::multiply<double>(first, second);
}

auto divide(double first, double second) -> double
{
    return SMath::divide<double>(first, second);
}

auto info() -> const char *
{
    std::string const str = SMath::info();
    return str.c_str();
}
