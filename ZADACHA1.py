with open('nginx_logs.txt') as f:
    data = []
    for line in f:
        splitted = line.split()
        data.append((splitted[0], splitted[5].replace('"', ''), splitted[6]))
print(data)