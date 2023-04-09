
#include <stdio.h>
#include <stdlib.h>
#include "MathFunction.h"
using namespace std;

int main(int argc, char *argv[])  //本身的命令会当作第一个参数
{
    if (argc < 3){
        printf("Usage: %s base exponent \n", argv[0]);
        return 1;
    }
    double base = atof(argv[1]);
    int exponent = atoi(argv[2]);
    double result = power(base, exponent);
    printf("%g ^ %d is %g\n", base, exponent, result);
    return 0;
}