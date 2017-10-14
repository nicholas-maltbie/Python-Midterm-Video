"""

Time Linked List copy of list of integers

"""

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

def copy_list(ll):
    if ll:
        s = make_node(get_val(ll))
        ptr = get_next(ll)
        curr = s
        while get_next(ptr):
            set_next(curr, make_node(get_val(ptr)))
            curr = get_next(curr)
            ptr = get_next(ptr)
        return s

def make_list(size):
    s = make_node(0)
    l = s
    for i in range(1, size):
        n = make_node(i)
        set_next(l, n)
        l = n
    return s

if __name__ == "__main__":
    from datetime import datetime
    
    list_sizes = [{'size':10 ** v, 'pow':v} for v in range(1, 7+1)]
    
    def calc_time(n):
        t1 = datetime.now()
        l = make_list(n)
        l2 = copy_list(l)
        t2 = datetime.now()
        return (t2 - t1).total_seconds()
    
    for size in list_sizes:
        n = size['size']
        times = [calc_time(n) for i in range(10)]
        average = sum(times) / len(times)
        print('Took %f seconds to allocate and copy list of size 10^%i' % (average, size['pow']))
        

