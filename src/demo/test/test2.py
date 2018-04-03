def demo(a, b):
    return a+b


def func(func, a, b):
    return func(a, b)

print(func(demo, 1, 2))