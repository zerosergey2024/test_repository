a,b = 9,8

a = int(input("Введите первое число-"))
b = int(input("Введите второе число-"))
c = int(input("Введите третье число-"))

if a>b and a>c:
    print("a""Самое большое число")

if b>c:
    print("c""Самое маленькое число")
elif a<b or a<c or b<c:
    print("Измени выбор")