
def selection_sort(matr):
    sorted_len = 0
    matr_len = len(matr)
    while sorted_len < matr_len:
        minimum_ind = None
        for i in range(sorted_len, matr_len):
            if minimum_ind == None or matr[i] <= matr[minimum_ind] :
                minimum_ind = i
        matr[sorted_len], matr[minimum_ind] = matr[minimum_ind], matr[sorted_len]
        sorted_len += 1
    return a
    
if __name__ == '__main__':
    from random import randint
    min_ind = -10
    max_ind = 20
    size = 4000
    a = [randint(min_ind, max_ind) for k in range(size)]
    from time import time
    t1 = time()
    b = selection_sort(a)
    t2 = time()
    print ("Sort works properly - ", sorted(a) == b)
    t = t2-t1
    print ("{: 0.8f}".format(t))