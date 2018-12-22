class MyList(list):
    def __init__(self, list1 = None):
        if list1:
            self.data = list1.copy()
    def __add__(self, arg):
        return MyList(self.data + arg)
    def __getitem__(self, k):
        return self.data[k]
    def __iter__(self):
        for i in range(self.data.len()):
            yield self.data[i]
    def __getattr__(self, name):
        return getattr(self.data, name)

    
if __name__ == "__main__":
    mylist = MyList()
    mylist1 = MyList([5, 6, 2, 55])
    print (mylist)
    print (mylist1)
    print (mylist1 + [5, 99])
    print ([88, 5] + mylist1)
    print (mylist1[1])
    print (mylist1[0:2])
    mylist1.append(55)
    print (mylist1)
    i = iter(mylist1)
    print (i)
    print (i)
    print (i)
    print (mylist1.sort())