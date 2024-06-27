def func():
    x=5
    print('Function Parrt 1')

    yield x
    x +=7
    print('Function part 2')

    yield x
    print('Function part 3')


try:
    #main function
    y = func()
    z = next(y)
    print(z)

    z=next(y)
    print(z)

    z=next(y)
    print(z)

except StopIteration as e:
    pass