num = int(input())

for c in range(num + 1):
    if c % 2 == 0 and c != 0:
        print(f'{c}^2 = {int(c ** 2)}')
