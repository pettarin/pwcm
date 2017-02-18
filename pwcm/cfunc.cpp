#include "cfunc.h"

__attribute__ ((target ("default")))
int _dosomething(void)  {
    return 0;
}

__attribute__ ((target ("sse")))
int _dosomething(void)  {
    return 1;
}

__attribute__ ((target ("sse2")))
int _dosomething(void) {
    return 2;
}

__attribute__ ((target ("sse3")))
int _dosomething(void) {
    return 3;
}

__attribute__ ((target ("sse4a")))
int _dosomething(void) {
    return 40;
}

__attribute__ ((target ("sse4.1")))
int _dosomething(void) {
    return 41;
}

__attribute__ ((target ("sse4.2")))
int _dosomething(void) {
    return 42;
}
