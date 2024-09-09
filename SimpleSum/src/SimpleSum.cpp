#include "../include/SimpleSum.hpp"

#include <numeric>


auto sum(std::span<const int> numbers) -> int
{
    return std::accumulate(numbers.begin(), numbers.end(), 0);
}

auto sum_c(int num_numbers, const int *numbers) -> int
{
    return sum(std::span<const int>(numbers, num_numbers));
}
