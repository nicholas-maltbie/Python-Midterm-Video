#include <Python.h>
#include <stdio.h>
#include <time.h>

using namespace std;

long* copy_list(long* start, long length) {
    long* copy = new long[length];
    for(long i = 0; i < length; i++) {
        copy[i] = start[i];
    }
    return copy;
}

// int main () {
//     int size = 10;
//     for (int i = 1; i <= 8; i++) {
//         clock_t begin = clock();
        
//         int* array = new int[size];
//         for(int j = 0; j < size; j++) {
//             array[j] = j;
//         }
//         int* copy = copy_list(array, size);
        
//         clock_t end = clock();
        
//         delete[] array;
//         delete[] copy;
        
//         float elapsed_secds = float( end - begin ) /  CLOCKS_PER_SEC;
        
//         printf("Took %f seconds to copy a list of size 10^%i\n", elapsed_secds, i);
        
//         size *= 10;
//     }
// }

