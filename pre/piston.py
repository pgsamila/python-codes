
num_of_pis = raw_input()
a=map(int,raw_input().split())
b=map(int,raw_input().split())

k = 0
for i in b:
    if i == 0:
        a[i+1] = 0

        k = num_of_pis - (i+1)

print(a)

