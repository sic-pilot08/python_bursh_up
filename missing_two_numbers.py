def two_missing(arr, n):
    mark = [False for i in range(n + 1)]
    for i in range(0, n - 2, 1):
        mark[arr[i]] = True
    for i in range(1, n + 1, 1):
        if mark[i] == False:
            print(i)


lst = [1, 3, 4, 6]
n = 2 + len(lst)
two_missing(lst, n)

