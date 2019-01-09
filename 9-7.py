coba = open('chicken.txt', 'r')
sum = 0
day = 0
for line in coba:
    data = line.strip().split(": ")
    sum = sum + int(data[1])
    day += 1

print(sum / day)
coba.close()