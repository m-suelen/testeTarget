fibo = list()
t1 = 0
t2 = 1
t3 = 0
num = int(input('Digite um número: '))
print(t1, end=' ')
for i in range(10):
    t1 = t2
    t2 = t3
    t3 = t1 + t2
    fibo.append(t3)

for n in fibo:
    if n == num:
        print(f'\033[1;32m{n}\033[m', end=' ')
    else:
        print(n, end=' ')

if num in fibo:
    print('\nO número pertence a sequência')
else:
    print('\nO número não pertence a sequência')
