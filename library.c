#include <stdio.h>
#include <stdlib.h>

long long sumAll(int x){
    long long sum = 0;
    while (x>0){
        sum = sum + x;
        x--;
    }
    return sum;
}
