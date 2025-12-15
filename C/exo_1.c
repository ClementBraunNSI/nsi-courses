#include <stdio.h>
#include <stdlib.h>

int suite(int n){
    int i = 0;
    int u_deb = 1;
    if (n==0){
        return u_deb;
    }
    else{
        while (i < n){
            u_deb = 2*u_deb + 1;
            i++;
        }
    }
    return u_deb;
}

int suite_for(int n){
    int u = 1;
    if (n == 0){
        return u;
    }
    else{
        for (int i = 0; i < n; i++){
            u = 2*u + 1;
        }
    }
    return u;
}

int suite_rec(int n){
    if (n == 0){
        return 1;
    }
    else{
        return 2*suite_rec(n-1) + 1;
    }
}

int* suite_tab(int n){
    int* tab = malloc(n * sizeof(int));
    tab[0] = 1;
    for (int i = 1; i<n+1 ; i++){
        tab[i] = tab[i-1]*2 + 1;
    }
    return tab;
}

int fibo(int n){
    if (n == 0){
        return 0;
    }
    else if (n == 1){
        return 1;
    }
    else{
        return fibo(n-1) + fibo(n-2);
    }
}

int fibo_iter(int n){
    if (n == 0){
        return 0;
    }
    else if (n == 1){
        return 1;
    }
    else{
        int i = 0;
        int fibo_1 = 0;
        int fibo_2 = 1;
        while (i < n - 1){
            int fibo_3 = fibo_1 + fibo_2;
            fibo_1 = fibo_2;
            fibo_2 = fibo_3;
            i++;
        }
        return fibo_2;
    }
}

int main(void){
    int n = 3;
    int u = suite(n);
    int u2 = suite_for(n);
    int u3 = suite_rec(n);
    int* u4 = suite_tab(n);
    printf("%d %s", u, "suite avec while");
    printf("%d %s", u2, "suite avec for");
    printf("%d %s", u3, "suite avec recursion");
    for (int i = 0; i < n+1; i++){
        printf("%d %s", u4[i], "suite avec tableau");
    }
    printf("%d %s", fibo(5), "suite de fibonacci avec recursion");
    printf("%d %s", fibo_iter(5), "suite de fibonacci avec iteration");

    int x;
    while (x != 0){
        printf("Entrez un nombre (0 pour arrêter) : ");
        scanf("%d", &x);
    }

}
