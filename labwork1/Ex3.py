# Ex3
n = int(input("Enter the number?"))
is_prime = True
if n <= 1:
    is_prime = False
for i in range(2, n):
    if n % i == 0:
        is_prime = False
if is_prime:
    print(n, "is a prime number")
else:
    print(n, "is a NOT prime number")
