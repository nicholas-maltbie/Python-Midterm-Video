#include<iostream>
#include<stdio.h>
#include<ctime>

using namespace std

struct Node {
    int val;
    Node* next;
}

Node* make_list(int length) {
    Node* start = NULL;
    for (int i = length - 1; i >= 0; i++) {
        start = new Node(i, start);
    }
    return start;
}

void delete_list(Node* start) {
    while (start != NULL) {
        Node* next = start->next;
        delete start;
        start = next;
    }
}

int* copy_list(int* start, int length) {
    int* copy = new int[length];
    for(int i = 0; i < length; i++) {
        copy[i] = start[i];
    }
    return copy
}

int main () {
    int size = 10
    for(int i = 1; i <= 7; i++) {
        cock_t begin = clock();
        
        int* array = new int[size];
        for(int i = 0; i < size; i++) {
            array[i] = i;
        }
        int* copy = copy_list(start, size);
        
        clock_t end = clock();
        
        delete[] array;
        delete[] copy;
        
        double elapsed_secds = double(end - begin) / CLOCKS_PER_SEC;
        
        printf("Took %d seconds to copy a list of size 10^%i", elapsed_secds, i);
        
        size *= 10;
    }
}

