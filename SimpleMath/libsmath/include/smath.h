#ifndef SMATH_H
#define SMATH_H

#ifdef __cplusplus
extern "C" {
#endif

double add(double first, double second);
double subtract(double first, double second);
double multiply(double first, double second);
double divide(double first, double second);

const char* info();

#ifdef __cplusplus
}
#endif

#endif // SMATH_H
