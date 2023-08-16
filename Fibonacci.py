def fibonacci(n):
    fib_sequence = [0, 1]
    for i in range(2, n):
        next_fib = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_fib)
    return fib_sequence

try:
    n = int(input("Digite um número N: "))
    if n <= 0:
        print("Por favor, digite um número positivo.")
    else:
        fib_sequence = fibonacci(n)
        for num in fib_sequence:
            print(num, end=" ")
except ValueError:
    print("Por favor, digite um número válido.")
