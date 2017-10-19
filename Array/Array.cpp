#include <Python.h>
#include <stdio.h>
#include <time.h>

using namespace std;

long* copy_list(long* start, long length) {
    long* copy = new long[length];

    for (long i = 0; i < length; i++) {
        copy[i] = start[i];
    }

    return copy;
}
