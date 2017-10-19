"""

Time Array copy of list of integers

"""

import copylist as cl

def copy_list(array):
    new = [None] * len(array)
    for i in range(len(array)):
        new[i] = array[i]
    return new

def c_copy_list(array):
    return cl.copy_list(array)

if __name__ == "__main__":
    from datetime import datetime
    
    list_sizes = [{ 'size': 10 ** v, 'pow': v } for v in range(1, 7+1)]
    
    def calc_time(n):
        t1 = datetime.now()
        l = [i for i in range(n)]
        l2 = copy_list(l)
        t2 = datetime.now()
        return (t2 - t1).total_seconds()

    def c_calc_time(n):
        t1 = datetime.now()
        l = [i for i in range(n)]
        l2 = c_copy_list(l)
        t2 = datetime.now()
        return (t2 - t1).total_seconds()

    for size in list_sizes:
        n = size['size']
        times = [calc_time(n) for i in range(10)]
        average = sum(times) / len(times)
        print('Took %f seconds to allocate and copy list of size 10^%i' % (average, size['pow']))

        n = size['size']
        times = [c_calc_time(n) for i in range(10)]
        average = sum(times) / len(times)
        print('Took %f seconds to allocate and copy list of size 10^%i in C++' % (average, size['pow']))
