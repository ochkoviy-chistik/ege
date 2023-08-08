"""
Входной файл содержит сведения о заявках на проведение занятий в конференц-зале. 
В каждой заявке указаны время начала и время окончания мероприятия (в минутах от начала суток).
Если время начала одного мероприятия меньше времени окончания другого, то провести можно только одно из них. 
Если время окончания одного мероприятия совпадает с временем начала другого, то провести можно оба. 
Определите какое максимальное количество мероприятий можно провести в конференц-зале и каков при этом максимальный перерыв между двумя последними мероприятиями.
"""

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
