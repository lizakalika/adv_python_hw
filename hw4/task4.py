def decorator(func):
    def wrapper(l):
        n = func(l)
        if n == 0:
            print('Нет(')
        elif n > 10:
            print('Очень много')
    return wrapper

@decorator
def even(l):
    n = 0
    for i in l:
        if i % 2 == 0:
            n += 1
    return n 
    
if __name__ == '__main__':
    l1 = [i for i in range(10)]
    l2 = [1, 3, 7]
    l3 = [i for i in range(100)]
    for list_i in [l1, l2, l3]:
        even(list_i)
