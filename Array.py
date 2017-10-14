"""

Time Array copy of list of integers

"""

if __name__ == "__main__":
    from datetime import datetime
    from copy import copy
    
    list_sizes = [{'size':10 ** v, 'pow':v} for v in range(1, 8+1)]
    
    def calc_time(n):
        t1 = datetime.now()
        l = [i for i in range(n)]
        l2 = copy(l)
        t2 = datetime.now()
        return (t2 - t1).total_seconds()
    
    for size in list_sizes:
        n = size['size']
        times = [calc_time(n) for i in range(10)]
        average = sum(times) / len(times)
        print('Took %f seconds to allocate and copy list of size 10^%i' % (average, size['pow']))

