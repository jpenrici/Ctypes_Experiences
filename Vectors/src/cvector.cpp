#include "../include/cvector.h"
#include <numeric>


auto myVector() -> std::vector<double>
{
    return {10.1, 10.2, 10.3, 10.4, 10.5};
}

auto sum(const std::vector<double> &vec) -> double
{
    auto sum = std::accumulate(vec.begin(), vec.end(), 0.0);
    return sum;
}

auto myStruct() -> CVector
{
    static auto vec = myVector();
    return CVector{vec.data(), static_cast<unsigned int>(vec.size())};
}

auto sum(const double *vec, unsigned int n) -> double
{
    auto total = sum(std::vector<double>(vec, vec + n));
    return total;
}
