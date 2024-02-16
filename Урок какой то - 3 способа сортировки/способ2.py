#сортировка шелла
def ShellSort(data, size):
    interval = size // 2
    while interval > 0:
        for i in range(interval, size):
            temp = data[i]
            j = i
            while j >= interval and data[j - interval] > temp:
                data[j] = data[j - interval]
                j -= interval
            data[j] = temp
        interval //= 2
