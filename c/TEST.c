#include <stdio.h>

int main(void)
{
    while(1)
    {
        int x;
        scanf("%d", &x);

        if(x == 42)
            break;
        printf("%d\n", x);
    }

    return 0;
}