import time

def fibonacci_sequence():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

def main():
    fib_sequence = fibonacci_sequence()

    try:
        while True:
            fibonacci_number = next(fib_sequence)
            print(f"Следующее число Фибоначчи: {fibonacci_number}")
            time.sleep(0.1)  # пауза в 1 секунду
    except KeyboardInterrupt:
        print("\nПрограмма завершена пользователем.")

if __name__ == "__main__":
    main()
