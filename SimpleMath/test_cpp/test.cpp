#include "../libsmath/include/smath.h"

#include <iostream>

auto main() -> int
{
    auto text = info();
    printf("This is a shared library C++ test ...\n%s\n", text);

    double first  = 10;
    double second = 20;

    auto sum = add(first, second);
    auto sub = subtract(first, second);
    auto mult = multiply(first, second);
    auto div = divide(first, second);

    // Result: 30 -10 200 0.5
    std::cout << sum  << " " << sub << " " << mult << " " << div << "\n";

    return 0;
}