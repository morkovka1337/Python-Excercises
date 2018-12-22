def merge(a, b):
    c = []
    a_id, b_id = 0, 0
    while a_id < len(a) and b_id < len(b):
        if a[a_id] < b[b_id]:
            c.append(a[a_id])
            a_id += 1
        else:
            c.append(b[b_id])
            b_id += 1
    c.extend(a[a_id:]) if b_id == len(b) else c.extend(b[b_id:])
    return c

def merge_sort(a):
    if len(a) <= 1:
        return a
    slice_l = int(len(a)/2)
    left, right = merge_sort(a[:slice_l]), merge_sort(a[slice_l:])
    return merge(left, right) 

if __name__ == "__main__":
    from random import randint
    min_ind = -10
    max_ind = 20
    size = 9
    a = [randint(min_ind, max_ind) for k in range(size)]
    from time import time
    t1 = time()
    b = merge_sort(a)
    t2 = time()
    t = t2-t1
    print (a)
    print (b)
    print ("{: 0.8f}".format(t))