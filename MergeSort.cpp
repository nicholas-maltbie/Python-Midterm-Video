//compile with "g++ -std=c++11 MergeSort.cpp -o MergeSort.out"

#include <stdio.h>
#include <ctime>
#include <string>
#include <fstream>

using namespace std;

int* merge (int* l1, int s1, int* l2, int s2) {
    int* l_new = new int[s1 + s2];
    int i = 0, i1 = 0, i2 = 0;
    while (i1 < s1 && i2 < s2) {
        if (l1[i1] < l2[i2]) {
            l_new[i] = l1[i1];
            i1++;
        }
        else {
            l_new[i] = l2[i2];
            i2++;
        }
        i++;
    }
    while (i1 < s1) {
        l_new[i] = l1[i1];
        i1++;
        i++;
    }
    while (i2 < s2) {
        l_new[i] = l2[i2];
        i2++;
        i++;
    }
    return l_new;
}

int* mergesort (int* l, int size) {
    if (size <= 1) {
        int* copy = new int[size];
        for(int i = 0; i < size; i++) {
            copy[i] = l[i];
        }
        return copy;
    }
    int half = (size) / 2;
    int* l1 = mergesort(l, half);
    int* l2 = mergesort(l + half, size - half);
    int* fin = merge(l1, half, l2, size - half);
    delete[] l1;
    delete[] l2;
    return fin;
}

int main () {
    for (int i = 2; i <= 7; i++) {
        clock_t begin = clock();
        
        ifstream infile("rand" + std::to_string(i) + ".txt");
        int n;
        infile >> n;
        int* list = new int[n];
        
        for (int line = 0; line < n; line++) {
            int val;
            infile >> val;
            list[line] = val;
        }
        
        int* sorted = mergesort(list, n);
        
        delete[] list;
        delete[] sorted;
        
        clock_t end = clock();
        
        float elapsed_secds = float( end - begin ) /  CLOCKS_PER_SEC;
        
        printf("Took %f seconds to copy a linked list of size %i\n", elapsed_secds, n);
    }
}

