import math

count = int(input())
sizes = map(int, input().split())
disc_size = int(input())

total = 0

for i in sizes:
    if i == 0:
        continue
    else:
        disc_count = math.ceil(i / disc_size)
    total += disc_count * disc_size
    
print(total)
