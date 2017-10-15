#include<iostream>
#include<stdio.h>
#include<ctime>

using namespace std;

struct Node {
    int val;
    Node* next;
};

Node* make_list(int length) {
    Node* start = NULL;
    for (int i = length - 1; i >= 0; i--) {
        Node* next = start;
        start = new Node;
        start->val = i;
        start->next = next;
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

Node* copy_list(Node* start) {
    Node* s = new Node;
    s->val = start->val;
    Node* ptr = start->next;
    Node* curr = s;
    while (ptr->next != NULL) {
        Node* tmp = new Node;
        tmp->val = ptr->val;
        curr->next = tmp;
        curr = tmp;
        ptr = ptr->next;
    }
    return s;
}

int main () {
    int size = 10;
    for (int i = 1; i <= 7; i++) {
        clock_t begin = clock();
        
        Node* list = make_list(size);
        Node* copy = copy_list(list);
        
        clock_t end = clock();
        
        delete_list(list);
        delete_list(copy);
        
        float elapsed_secds = float( end - begin ) /  CLOCKS_PER_SEC;
        
        printf("Took %f seconds to copy a linked list of size 10^%i\n", elapsed_secds, i);
        
        size *= 10;
    }
}

