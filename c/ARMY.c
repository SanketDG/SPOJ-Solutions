#include <stdio.h>

int find_max(int a[], int n)
{
    int max, i;

    max = a[0];
    for(i = 0; i < n; i++)
    {
        if(a[i] > max)
            max = a[i];
    }

    return max;
}

int main(int argc, char const *argv[])
{
    int g[100], m[100], i, n, j, k, ng, nm;

    scanf("%d", &n);
    for(i = 0; i < n; i++)
    {
        scanf("%d %d", &ng, &nm);
        int g[ng];
        int m[nm];
        for(j = 0; j < ng; j++)
        {
            scanf("%d", &g[j]);
        }
        for(k = 0; k < nm; k++)
        {
            scanf("%d", &m[k]);
        }

        if(find_max(g, ng) >= find_max(m, nm))
            printf("Godzilla\n");
        else if((find_max(g, ng) < find_max(m, nm)))
            printf("MechaGodzilla\n");
        else
            printf("uncertain\n");
    }

    return 0;
}