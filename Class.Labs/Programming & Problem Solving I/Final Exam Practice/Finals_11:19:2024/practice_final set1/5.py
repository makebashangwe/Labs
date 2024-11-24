def bubble_sort(lst):
    for i in range(len(lst)):
        for j in range(len(lst)-i-1):
            if lst[j+1]<lst[j]:
                lst[j],lst[j+1] = lst[j+1],lst[j]
            else:
                continue
    return lst


n = input("").strip().split(',')
lst = list(map(int,n))
print(bubble_sort(lst))