def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def get_nth_prime(n):
    if n <= 0:
        raise ValueError("n>0")
    
    count = 0
    number = 1

    while count < n:
        number += 1
        if is_prime(number):
            count += 1

    return number

def main():
        n = 10
        prime = get_nth_prime(n)
        print(f"Value: {prime}")

if __name__ == "__main__":
    main()
