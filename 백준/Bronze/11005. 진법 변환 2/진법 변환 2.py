number_to_char = {
    i : str(i) for i in range(10)
}
number_to_char.update({i + 10 : chr(ord('A') + i) for i in range(26)})

n, b = input().split()
n = int(n)
b = int(b)
char = ""

while n > 0:
    count = n % b
    char += number_to_char[count]
    n = n // b
    
print(char[::-1])