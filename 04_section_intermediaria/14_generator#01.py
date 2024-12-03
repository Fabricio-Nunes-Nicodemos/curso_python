# import sys

# iterable = ['Eu', 'Tenho', '__iter__']
# iterator = iter(iterable)
# lista = [n for n in range(1000000)]
# generator = (n for n in range(1000000))

# print(sys.getsizeof(lista))
# print(sys.getsizeof(generator))

# for n in generator:
#     print(n)

# Introdução às Generator functios em Python
# generator = (n for n in range(100000))

def generator(n=0, maximun=10):
    while True:
        yield n

        n += 1

        if n >= maximun:
            return

gen = generator(5, 8)
for n in gen:
    print(n)