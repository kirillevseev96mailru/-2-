import os

directory = r'.'
groups = [100, 1000, 10000, 100000, 1000000]
groups += [float("inf")]
result = dict.fromkeys(groups, 0)


for path_from_top, subdirs, files in os.walk(directory):
    for file in files:
        path = os.path.join(path_from_top, file)
        size = os.path.getsize(path)
        to_group = min(filter(lambda x: size < x, groups))
        result[to_group] += 1

prev_size = 0
for size in groups:
    print(f"Файлов размером (байт) от {prev_size:10} до {size:10} : {result[size]}")
    prev_size = size