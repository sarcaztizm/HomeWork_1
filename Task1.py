# Найти сумму цмфр трехзначного числа
# 123 -> 6
# 100 -> 1

print('Введите трехзначное число')
number = int(input())
if number // 1000 > 0:
    print('Введено неправильное число')
# print(number%10)
# print(number//10)
result = 0
while(number > 0):
    result += number % 10
    number //= 10
print('Сумма цифр трехзначного числа:',result)
