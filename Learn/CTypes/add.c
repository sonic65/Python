//sample C file to add 2 numbers - int and floats

#include <stdio.h>

int add_int(int, int);
float add_float(float, float);

int add_int(int num1, int num2){
    return num1 + num2;
}

float add_float(float num1, float num2){
    return num1 + num2;
}

/*
// 编译

// #For Linux
// $  gcc -shared -Wl,-soname,adder -o adder.so -fPIC add.c

// #For Mac
// $ gcc -shared -Wl,-install_name,adder.so -o adder.so -fPIC add.c
*/