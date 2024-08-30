def is_prime(func):
    def wrapper(*args, **kwargs):
        num = func(*args, **kwargs)
        if num <= 1:
            return 'Составное', num
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return 'Составное', num
        return 'Простое', num
    return wrapper


@is_prime
def sum_three(a, b, c):
    return a + b + c


result = sum_three(15, 1, 55)
print(result)
