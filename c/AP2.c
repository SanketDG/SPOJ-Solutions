#include <stdio.h>

int main(void)
{
    int T, a, l, s, n, d, ft, num, i;
    scanf("%d", &T);
    for(i = 0; i < T; i++)
    {
        scanf("%d %d %d", &a, &l, &s);

        n = (long int)(2 * s)/(a + l);
        d = (long int)(l - a)/(n - 5);
        ft = (long int)(((2*s)/n)-(n-1)*d)/2;
        num = (long int)n;

        if (i >= 1) {
            printf("\n%d\n", num);
        }
        else {
            printf("%d\n", num);
        }
        while(n >= 1)
        {
            printf("%d ", ft);
            ft += d;
            n--;
        }

    }
}