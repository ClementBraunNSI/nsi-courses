def triangle(n):
    print("Triangle de hauteur ", n)
    for i in range(n+1):
        print(((i)*"*"))


def triangle_isocele(n):
    for i in range(n+1):
        if i%2 == 1:
            print(((n-i)//2)*' ' + i*'*')
            

triangle_isocele(12)