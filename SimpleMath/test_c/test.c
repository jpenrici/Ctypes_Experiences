#include <stdio.h>
#include "../libsmath/include/smath.h"

int main(void)
{
  printf("This is a shared library C test ...\n%s\n", info());

  double first  = 10;
  double second = 20;

  double sum = add(first, second);
  double sub = subtract(first, second);
  double mult = multiply(first, second);
  double div = divide(first, second);

  // Result: 30.000000 -10.000000 200.000000 0.500000
  printf("%f %f %f %f\n", sum, sub, mult, div);
}