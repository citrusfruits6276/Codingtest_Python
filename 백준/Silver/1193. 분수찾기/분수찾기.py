x = int(input())
line = 0
line_end = 0

while line_end < x:
    line += 1
    line_end += line

k = line_end - x

if line % 2 == 0:
    a = line - k
    b = k + 1
else:
    a = k + 1
    b = line - k

print(f"{a}/{b}")
    
    