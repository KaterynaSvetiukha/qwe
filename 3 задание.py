

n = int(input("Введіть число: "))

while (n < 1 or n > 9):
  n = int(input("Введіть число 1 < n < 9: "))

for i in range(1, n + 1):
  for j in range(i, 0, -1):
   print(j, end = "")
  print()