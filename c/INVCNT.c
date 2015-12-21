#include <stdio.h>

long long merge(int a[], int low, int mid, int high)
{
    int temp[200001];
    int i, j, k;
    long long inv_count;
    i = low;
    j = mid;
    k = low;

    inv_count = 0;

    while((i <= mid - 1) && (j <= high))
    {
        if(a[i] <= a[j])
            temp[k++] = a[i++];
        else {
            temp[k++] = a[j++];
            inv_count = inv_count + (mid - i);
        }
    }
    while(i <= mid - 1)
        temp[k++] = a[i++];
    while(j<=high)
        temp[k++] = a[j++];
    for(i=low; i<=high; i++)
    {
        a[i] = temp[i];
    }

    return inv_count;
}

long long mergesort(int a[], int l, int h)
{
    int mid;
    long long inv_count;
    inv_count = 0;
    if(h > l)
    {
        mid = (l + h)/2;
        inv_count = mergesort(a, l, mid);
        inv_count += mergesort(a, mid+1, h);
        inv_count += merge(a, l, mid+1, h);
    }
    return inv_count;
}

int main(int argc, char const *argv[])
{
    int n, i, j, l, a[200001];


    scanf("%d", &n);
    for(j = 0; j < n; j++)
    {
        scanf("%d", &l);
        for(i = 0; i < l; i++)
        {
            scanf("%d", &a[i]);
        }
        printf("%lld\n", mergesort(a, 0, l-1));
    }
    return 0;
}