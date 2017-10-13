"""

Time Linked List copy of list of integers

"""

y_comb = \
    lambda F: \
        (lambda procedure: \
            F(lambda x: procedure(procedure)(x)) \
        )(lambda procedure: \
            F(lambda x: procedure(procedure)(x)))

make_node = lambda val, next=None: [val, next]
get_val = lambda node: node[0]
get_next = lambda node: node[1]

max_ll = y_comb(\
    lambda arg:
        lambda n, curr_max:
            arg(get_next(n), max(get_val(n), curr_max)) if n else curr_max)
            #get_val(l), arg(get_next(l)) if get_next(l) else get_val(l))

#copy_ll = lamda l:  

#def copy_list(ll):
#    return (lambda ll, acc: make_node(get_val(ll), acc) if ll else acc)\
#            (copy_list(get_next(ll)), make_node(ll, get_next(ll))) if ll else None

#copy_ll = y_comb(\
#    lambda arg: \
#        lambda l:
#            (lambda node, acc: \
#                make_node(get_val(node), arg(acc)) if acc else None)
#            (get_next(l), get_next(l)))
#                #make_node(get_val(node), arg(get_next(node))) if node else None)


    
#def copy_yield(ll):
#    def helper(sub, acc=None):
#        def helper_helper():
#            yield from helper(get_next(ll), acc)
#        if sub:
#            yield make_node(get_val(sub), next(helper_helper()))
#        yield None
#    if ll:
#        return next(helper(ll))
        

def copy_list(ll):
    if ll:
        s = make_node(get_val(ll))
        ptr = get_next(ll)
        curr = s
        while get_next(ptr):
            curr[1] = make_node(get_val(ptr))
            curr = get_next(curr)
            ptr = get_next(ptr)
        return s

def make_list(size):
    s = make_node(0)
    l = s
    for i in range(1, size):
        n = make_node(i)
        l[1] = n
        l = n
    return s


