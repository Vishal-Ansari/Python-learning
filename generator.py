def gen(n):
    for i in range(n):
        yield i

# g=gen(5)
# # print(g.__next__())
# # print(g.__next__())
# # print(g.__next__())
# # print(g.__next__())

# for i in g:
#     print(i)

h="vishal"
it=iter(h)
print(it.__next__())
print(it.__next__())
print(it.__next__())
print(iter(h))

# for c in h:
#     print(c)