# for: Print all even numbers from 1 to 20 using a for loop
print("Even numbers from 1 to 20:")
for num in range(1, 21):
    if num % 2 == 0:
        print(num)

# while: Find the sum of numbers from 1 to 100 using a while loop
sums = 0
current = 1
while current <= 100:
    sums += current
    current += 1
print("\nSum of numbers from 1 to 100:", sums)

# if else: Check if a number is prime
number = int(input("\nEnter a number to check if it is prime: "))
if number > 1:
    is_prime = True
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            is_prime = False
            break
    if is_prime:
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")
else:
    print(f"{number} is not a prime number.")