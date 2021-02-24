def prime_checker(n):
    is_prime = True
    for i in range(2,n):
        if n % i == 0:
            is_prime = False
    if is_prime:
        print(f"{i+1} is prime")
    else:
         print(f"{i+1} is not prime")

n = int(input("check this number: "))
prime_checker(n)
