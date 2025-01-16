def echanger(l, a,b):
    l[a], l[b] = l[b], l[a]

def inserer(l, i):
    j = i
    while j > 0 and l[j] < l[j-1]:
        echanger(l,j,j-1)
        j = j - 1

def tri_insertion(l):
    for i in range(1,len(l)):
        inserer(l, i)
    return l

print(tri_insertion([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]))