#include <stdio.h>

int is_palindrome(int num)
{
    int rem, rev, orig;
    rev = 0;

    orig = num;

    while(num != 0)
    {
        rem = num % 10;
        rev = rev * 10 + rem;
        num /= 10;
    }

    return rev == orig;
}

int main(void)
{
    int T, n, i, c;

    scanf("%d", &T);

    for(c= 0; c < T; c++)
    {
        scanf("%d", &n);

        for(i = n+1; !is_palindrome(i); i++)
        {
        }
        printf("%d\n", i);
    }
}