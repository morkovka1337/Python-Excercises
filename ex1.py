class Adder():
    def __init__(self, a):
        self.data = a
    def __add__(self, y):
        return self.add(y)
    def add(self, y):
        print ("Not implemented")

class ListAdder(Adder):
    def add(self, y):
        return self.data + y
    
class DictAdder(Adder):
    def add(self, y):
        self.data.update(y)
        return self.data

if __name__ == '__main__':
    list1 = [5, 6, 7]
    list2 = [7, 8, 9]
    x = Adder([5, 6, 7])
    x = x + [7, 8, 9]
    y = ListAdder([5, 88])
    print (y.add(list2))
    z = DictAdder({'key1' : 'value1'})
    print (z.add({5:'45', 69:'spam'}))