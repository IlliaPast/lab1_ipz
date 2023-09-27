def fibonacci_iterative(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        fib = [0, 1]
        for i in range(2, n + 1):
            fib.append(fib[i - 1] + fib[i - 2])
        return fib[n]

n = int(input("Введіть номер числа Фібоначчі: "))
if n < 0:
    print("Номер повинен бути не менше 0.")
else:
    result = fibonacci_iterative(n)
    print(f"Число Фібоначчі з номером {n} дорівнює {result}.")