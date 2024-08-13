a = int(input ("Введіть а: "))

while (a < 1 or a > 100):
    a = int(input ("Введіть а: "))

b = int(input ("Введіть b: "))

while (b < 1 or b > 100):
    b = int(input ("Введіть ще раз b: "))

if a < b:
    r = (b / a - 1)

elif a == b:
    r = -295

else:
    r = (a - 235) / b

print("Результат обчислення виразу: " , r)
