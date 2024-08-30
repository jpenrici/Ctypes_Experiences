#ifndef HELLOWORLD_H
#define HELLOWORLD_H

#include <vector>

struct CVector {
    double * values;
    unsigned size;
};

auto myVector() -> std::vector<double>;
auto sum(const std::vector<double>& vec) -> double;

extern "C" {

auto myStruct() -> CVector;
auto sum(const double * vec, unsigned n) -> double;

}

#endif
