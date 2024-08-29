#include "../include/cvector.h"


auto myVector() -> std::vector<double>
{
    return {10.1, 10.2, 10.3, 10.4, 10.5};
}

auto myStruct() -> CVector
{
    static auto vec = myVector();
    return CVector{vec.data(), static_cast<unsigned int>(vec.size())};
}
