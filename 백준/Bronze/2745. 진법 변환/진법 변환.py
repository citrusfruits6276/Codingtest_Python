char_to_number = {str(i): i for i in range(10)}
char_to_number.update({chr(ord('A') + i): i + 10 for i in range(26)})

N, B = input().split()
B = int(B)

result = 0
power = 0
for i in reversed(N):
    result += char_to_number[i] * (B ** power)
    power += 1
    
print(result)
    