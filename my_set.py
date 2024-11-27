my_set={1,2,1,3,2,2.0,3.4,1.1,2.0,3.4,'r','o','l','l','r'}
print(my_set)
my_set.add((False,'ST',(8,7,6,5)))
print(my_set)
print(type(my_set))
my_set.discard((False,'ST',(8,7,6,5)))
print(my_set)
