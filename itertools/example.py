import itertools

myIters = itertools.product(*[[1, 2], [3, 4], [5, 6]])
for element in myIters:
    print(element)
