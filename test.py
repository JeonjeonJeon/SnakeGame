import random

sample = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(sample)

index = len(sample) - 1
while index > 0:
    sample[index] = sample[index - 1]
    index -= 1

print(sample)
# result: 9 8 7 6 5 4 3 2 1 0

for i in range(5):
    print(i, end=' ')
# result: 0 1 2 3 4


print()
for i in range(1, 5):
    print(i, end=' ')
# result: 1 2 3 4

print()
while i != 1:
    i = random.randrange(1, 30)
    print(i)
# randrange: 1 ~ 29

i = 1000
print('asfsaefsef')
while i != 30:
    i = random.randrange(30)
    print(i)
print('sffffff')
#randrange: 0 ~ 29