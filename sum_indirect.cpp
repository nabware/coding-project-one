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
   printf(" inside sum_indirect problem_setup, N=%lld \n", N);

   // Initialize A with random integers in [0, N-1]
   for (int64_t i = 0; i < N; ++i) {
       A[i] = static_cast<float>(lrand48() % N);
   }
}

float
sum(int64_t N, float A[])
{
   printf(" inside sum_indirect perform_sum, N=%lld \n", N);

   float total = 0.0f;
   for (int64_t i = 0; i < N; ++i) {
        int64_t idx = static_cast<int64_t>(A[i]);
        // Ensure idx is in bounds
        if (idx >= 0 && idx < N) {
            total += A[idx];
        }
    }

   return total;
}

