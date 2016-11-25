def partition(a, l, r):
    pivot_key = a[l]
    while(l < r):
        while(l < r and a[r] >= pivot_key):
            r -= 1
        a[l] = a[r]
        while(l < r and a[l] <= pivot_key):
            l += 1
        a[r] = a[l]
    a[l] = pivot_key
    return l

def quick_sort(a, l, r):
    if(l < r):
        pivot_loc = partition(a, l, r)
        quick_sort(a, l, pivot_loc - 1)
        quick_sort(a, pivot_loc + 1, r)

def main():
    a = [49, 38, 65, 97, 76, 13, 27, 49]
    quick_sort(a, 0, 7)
    print a
main()
