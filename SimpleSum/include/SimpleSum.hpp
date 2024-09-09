#pragma once

#include <span>


auto sum(std::span<const int> numbers) -> int;

extern "C" {

auto sum_c(int num_numbers, const int * numbers) -> int;

}
