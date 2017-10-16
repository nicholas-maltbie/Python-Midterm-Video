"""

Time MergeSort for list of integers

"""

import mergesort as m

def merge(l1, l2):
    l_new = [None] * (len(l1) + len(l2))
    i, i1, i2 = 0, 0, 0
    while i1 < len(l1) and i2 < len(l2):
        if l1[i1] < l2[i2]:
            l_new[i] = l1[i1]
            i1 += 1
        else:
            l_new[i] = l2[i2]
            i2 += 1
        i += 1
    while i1 < len(l1):
        l_new[i] = l1[i1]
        i1 += 1
        i += 1
    while i2 < len(l2):
        l_new[i] = l2[i2]
        i2 += 1
        i += 1
    return l_new

def mergesort(nums):
    if len(nums) > 1:
        return merge(mergesort(nums[:len(nums)//2]),mergesort(nums[len(nums)//2:]))
    return nums

def cmergesort(nums):
    return m.merge(nums)

if __name__ == "__main__":
    from datetime import datetime
    
    file_names = ["rand"+str(n)+".txt" for n in range(2,7+1)]
    
    def calc_time(name):
        t1 = datetime.now()
        with open(name) as input_list:
            n = int(input_list.readline().strip())
            unsorted = [int(input_list.readline().strip()) for _ in range(n)]
            mergesort(unsorted)
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
        print('Took %f seconds to allocate and sort a list of size %i' % (average, n))

        times = [c_calc_time(name) for i in range(10)]
        average = sum(times) / len(times)
        f = open(name)
        n = int(f.readline().strip())
        f.close()
        print('Took %f seconds to allocate and sort a list of size %i in C++' % (average, n))
        

