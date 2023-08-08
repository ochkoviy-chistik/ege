fn = '26.txt'

with open(fn, 'r') as file:
    n = int(file.readline())

    arr = []
    for _ in range(n):
        start, stop = map(int, file.readline().split())
        arr.append(
            (start, stop)
        )

arr.sort(key=lambda x: x[1])

lst = []
gr = 0

for start, stop in arr:
    if start >= gr:
        gr = stop
        lst.append(
            (start, stop)
        )

last = lst[-2][1]
best = 0

for start, stop in arr:
    if last < stop:
        best = max(best, stop - last)
        last = stop

print(len(lst), best)
