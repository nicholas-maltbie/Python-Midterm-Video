//compile with "g++ -std=c++11 MergeSortLL.cpp -o MergeSortLL.out"

#include <Python.h>
#include <iostream>
#include <stdio.h>
#include <ctime>
#include <fstream>

using namespace std;

struct Node {
    long val = 0;
    Node* next = NULL;
};

Node* merge(Node* l1, Node* l2){
    if (l1 == NULL) return l1;
    else if (l2 == NULL) return l2;

    Node* ptr = NULL;
    if (l1->val < l2->val) {
        ptr = l1;
        l1 = l1->next;
    }
    else {
        ptr = l2;
        l2 = l2->next;
    }
    Node* start = ptr;
    
    while (l1 != NULL && l2 != NULL) {
        if (l1->val < l2->val) {
            ptr->next = l1;
            l1 = l1->next;
        }
        else {
            ptr->next = l2;
            l2 = l2->next;
        }
        ptr = ptr->next;
    }
    if (l1 != NULL) ptr->next = l1;
    else ptr->next = l2;
    
    return start;
}

Node* mergesort(Node* nums) {
    if (nums->next != NULL) {
        Node* ptr1 = nums->next;
        Node* ptr2 = nums->next;
        Node* temp = nums;
        while (ptr2 != NULL) { 
            ptr2 = ptr2->next;
            if (ptr2 != NULL) {
                ptr1 = ptr1->next;
                temp = temp->next;
                ptr2 = ptr2->next;
            }
        }
        temp->next = NULL;
        return merge(mergesort(nums),
                     mergesort(ptr1));
    }
    return nums;
}
    
void delete_list(Node* start) {
    while (start != NULL) {
        Node* next = start->next;
        delete start;
        start = next;
    }
}

// Entry point for Python
long* mergesortLL(long* list, long size) {
    // create a linked list of nodes
    Node *head = nullptr;
    Node *current = nullptr;
    for (int i = 0; i < size; i++) {
        Node *newNode = new Node;
        newNode->val = list[i];
        newNode->next = nullptr;

        if (head == nullptr) {
            head = newNode;
            current = head;
        } else {
            current->next = newNode;
            current = current->next;
        }
    }

    // throw nodes into mergesort()
    Node *result = mergesort(head);

    // nodes are now sorted, so convert back to a list of longs and return
    current = result;
    for (int i = 0; i < size; i++) {
        list[i] = current->val;
        current = current->next;
    }

    return list;
}

// int main() {
//     long *list = new long[5];
//     list[0] = 3;
//     list[1] = 9;
//     list[2] = 2;
//     list[3] = 10;
//     list[4] = 7;
//     cout << list[0] << " " << list[1] << " " << list[2] << " " << list[3] << " " << list[4] << endl;

//     long *result = mergesortLL(list, 5);
//     cout << result[0] << " " << result[1] << " " << result[2] << " " << result[3] << " " << result[4] << endl;

//     return 0;
// }

// int main () {
//     for (int i = 2; i <= 2; i++) {
//         clock_t begin = clock();
        
//         ifstream infile("rand" + std::to_string(i) + ".txt");
//         int n;
//         infile >> n;
        
//         int val;
//         infile >> val;
        
//         Node* ptr = new Node;
//         ptr->val = val;
//         Node* ll = ptr;
//         for (int j = 1; j < n; j++) {
//             Node* tmp = new Node;
//             infile >> val;
//             tmp->val = val;
//             ptr->next = tmp;
//             ptr = ptr->next;
//         }
//         mergesort(ll);
        
//         delete[] ll;
        
//         clock_t end = clock();
        
//         float elapsed_secds = float( end - begin ) /  CLOCKS_PER_SEC;
        
//         printf("Took %f seconds to allocate adn sort a linked linked list of size %i\n", elapsed_secds, n);
//     }
// }
