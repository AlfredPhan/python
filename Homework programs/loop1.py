#Write a program to display all the prime numbers within the range of number using loop
start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

for num in range(start, end):
    # prime numbers are greater than 1
    print(num)
