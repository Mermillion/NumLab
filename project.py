import math
from typing import List

def is_prime(a: int) -> bool:
    if a <= 1:
        return False
    if a == 2:
        return True
    if a % 2 == 0:
        return False
    sqrt_a = int(math.sqrt(a)) + 1
    for i in range(3, sqrt_a, 2):
        if a % i == 0:
            return False
    return True

def factorization(a: int) -> List[int]:
    if a == 0:
        raise ValueError("Факторизация числа 0 не определена.")
    
    factors = []
    if a < 0:
        factors.append(-1)
        a = abs(a)
    while a % 2 == 0:
        factors.append(2)
        a //= 2
    for i in range(3, int(math.sqrt(a)) + 1, 2):
        while a % i == 0:
            factors.append(i)
            a //= i
    if a > 2:
        factors.append(a)
    return factors

def sieve_of_eratosthenes(n: int) -> List[int]:
    if n < 2:
        return []
    sieve = [True] * (n + 1)
    sieve[0:2] = [False, False]
    for current in range(2, int(math.sqrt(n)) + 1):
        if sieve[current]:
            sieve[current*current:n+1:current] = [False] * len(range(current*current, n+1, current))
    return [num for num, is_prime_flag in enumerate(sieve) if is_prime_flag]

def display_factors(factors: List[int]) -> str:
    return ' * '.join(map(str, factors))

def main():
    while True:
        print("Выберите действие:")
        print("1. Проверить, является ли число простым.")
        print("2. Разложить число на простые множители.")
        print("3. Вывести все простые числа до заданного предела.")
        print("4. Выйти.")
        choice = input("Введите номер действия (1-4): ")

        if choice == '1':
            try:
                number = int(input("Введите число для проверки: "))
                if is_prime(number):
                    print(f"{number} является простым числом.\n")
                else:
                    print(f"{number} не является простым числом.\n")
            except ValueError:
                print("Пожалуйста, введите корректное целое число.\n")

        elif choice == '2':
            try:
                number = int(input("Введите число для факторизации: "))
                factors = factorization(number)
                print(f"Простые множители числа {number}: {display_factors(factors)}\n")
            except ValueError as ve:
                print(f"Ошибка: {ve}\n")

        elif choice == '3':
            try:
                limit = int(input("Введите верхнюю границу диапазона: "))
                primes = sieve_of_eratosthenes(limit)
                if primes:
                    print(f"Простые числа до {limit}: {' '.join(map(str, primes))}\n")
                else:
                    print(f"В диапазоне до {limit} нет простых чисел.\n")
            except ValueError:
                print("Пожалуйста, введите корректное целое число.\n")

        elif choice == '4':
            print("Выход из программы.")
            break

        else:
            print("Некорректный выбор. Пожалуйста, попробуйте снова.\n")

if __name__ == "__main__":
    main()
