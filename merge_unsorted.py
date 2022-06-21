def sort_ab(a, b):
    """Given already-sorted lists, `a` and `b`, return sorted list of both.

    You may not use sorted() or .sort().
    """
a = [1, 3, 5, 7]
b = [2, 6, 8, 10]
c = []

c = a+b
print ("unsorted:", c)
c = sorted(c)
print("sorted:", c)

i, j = 0,0,
c = []

while (i>j):
    c = a[i]
    i = += 1
    j = += 1
    while (j<i):
        c = b[i]
        i = += 1
        j += 1
    #
