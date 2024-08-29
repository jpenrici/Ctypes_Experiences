#ifndef HELLOWORLD_H
#define HELLOWORLD_H

#include <vector>

struct CVector {
    double * values;
    unsigned size;
};

auto myVector() -> std::vector<double>;

extern "C" {

auto myStruct() -> CVector;

}

#endif
