#include <stdio.h>

int main(void)
{
    int T, i;
    long long int a, l, s, n, d, ft, num;
    scanf("%d", &T);
    for(i = 0; i < T; i++)
    {
        scanf("%lld %lld %lld", &a, &l, &s);
        n = (long long int)(2 * s)/(a + l);
        d = (long long int)(l - a)/(n - 5);
        ft = (long long int)(((2*s)/n)-(n-1)*d)/2;
        num = (long long int)n;

        if (i >= 1) {
            printf("\n%lld\n", num);
        }
        else {
            printf("%lld\n", num);
        }
        while(n >= 1)
        {
            printf("%lld ", ft);
            ft += d;
            n--;
        }

    }
}