#include <stdio.h>

int fib(int n) {
    if (n <= 1)
        return n;
    return fib(n - 1) + fib(n - 2);
}

int main(){
    printf("fib:%d\n",fib(35));
    return 0;
}