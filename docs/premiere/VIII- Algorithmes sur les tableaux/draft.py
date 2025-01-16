def tri_insertion(l):
    for i in range(1,len(l)):
        j = i
        while j > 0 and l[j] < l[j-1]:
            l[j], l[j-1] = l[j-1], l[j]
            j = j - 1
    return l

print(tri_insertion([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]))