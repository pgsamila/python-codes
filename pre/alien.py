
n = int(raw_input())

a = bin(n)[2:].zfill(32)

backwards = a[::-1]


b = int(backwards, 2)

print(b)