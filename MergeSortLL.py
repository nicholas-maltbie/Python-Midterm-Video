"""

Time Linked List Sort of list of integers

"""

import mergesortLL as mLL

def make_node(val, next=None):
    return [val, next]

def get_val(node):
    return node[0]

def get_next(node):
    return node[1]

def set_val(node, val):
    node[0] = val

def set_next(node, next):
    node[1] = next
    
def merge(l1, l2):
    if l1 == None:
        return l1
    elif l2 == None:
        return l2

    ptr = None
    if get_val(l1) < get_val(l2):
        ptr = l1
        l1 = get_next(l1)
    else:
        ptr = l2
        l2 = get_next(l2)
    start = ptr
    
    while l1 and l2:
        if get_val(l1) < get_val(l2):
            set_next(ptr, l1)
            ptr = l1
            l1 = get_next(l1)
        else:
            set_next(ptr, l2)
            ptr = l2
            l2 = get_next(l2)
    if l1:
        set_next(ptr, l1)
    elif l2:
        set_next(ptr, l2)
        
    return start

def mergesort(nums):
    if get_next(nums):
        ptr1 = get_next(nums)
        ptr2 = get_next(nums)
        temp = nums
        while ptr2:
            ptr2 = get_next(ptr2)
            if ptr2:
                ptr1 = get_next(ptr1)
                temp = get_next(nums)
                ptr2 = get_next(ptr2)
        set_next(temp, None)
        return merge(mergesort(nums),
                     mergesort(ptr1))
    return nums

def cmergesort(nums):
    return mLL.mergeLL(nums)


if __name__ == "__main__":
    from datetime import datetime
    
    file_names = ["rand"+str(n)+".txt" for n in range(2,7+1)]
    
    def calc_time(name):
        t1 = datetime.now()
        with open(name) as input_list:
            n = int(input_list.readline().strip())
            ptr = make_node(int(input_list.readline().strip()))
            ll = ptr
            for _ in range(n - 1):
                tmp = make_node(int(input_list.readline().strip()), None)
                set_next(ll, tmp)
                ll = tmp
            mergesort(ptr)
            input_list.close()
        t2 = datetime.now()
        return (t2 - t1).total_seconds()

    def c_calc_time(name):
        t1 = datetime.now()
        with open(name) as input_list:
            n = int(input_list.readline().strip())
            unsorted = [int(input_list.readline().strip()) for _ in range(n)]
            result = cmergesort(unsorted)
            input_list.close()
        t2 = datetime.now()
        return (t2 - t1).total_seconds()
    
    for name in file_names:
        times = [calc_time(name) for i in range(10)]
        average = sum(times) / len(times)
        f = open(name)
        n = int(f.readline().strip())
        f.close()
        print('Took %f seconds to allocate and sort a linked list of size %i' % (average, n))

        times = [c_calc_time(name) for i in range(10)]
        average = sum(times) / len(times)
        f = open(name)
        n = int(f.readline().strip())
        f.close()
        print('Took %f seconds to allocate and sort a list of size %i in C++' % (average, n))

