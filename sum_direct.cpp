#include <algorithm>
#include <chrono>
#include <iomanip>
#include <iostream>
#include <random>
#include <vector>
#include <string.h>

#include "sums.h"

void 
setup(int64_t N, float A[])
{
   printf(" inside direct_sum problem_setup, N=%lld \n", N);
}

float
sum(int64_t N, float A[])
{
   printf(" inside direct_sum perform_sum, N=%lld \n", N);

   float total = 0.0f;
   for (int64_t i = 0; i < N; i++)
      total += A[i];

   return total;
}

