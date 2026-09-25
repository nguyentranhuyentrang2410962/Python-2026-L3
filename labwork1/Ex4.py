# Ex4
n = int(input("Enter a number? "))
total = 0
for i in range(1, n):
    if n % i == 0:
        total = total + i
if total == n:
    print(n, "is a perfect number")
else:
    print(n, "is a NOT perfect number")