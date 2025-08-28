def tri_insertion(liste):
    l = liste
    for i in range(len(l)):
        j = i
        while j > 0 and l[j] < l[j-1]:
            l[j] , l[j-1] = l[j-1], l[j]
            j = j - 1
    return l

print(tri_insertion([4,2,1,5,3,6]))