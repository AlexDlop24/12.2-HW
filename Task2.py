# Requirement 1: Prompt user for N and validate N > 0
while True:
    N = int(input("How many Fibonacci Numbers do you want? "))
    if N > 0:
        break
    print("Error: Please enter a positive integer greater than zero.")

# Requirement 2 & 3: Compute first N terms (0, 1, ...) and store in a list
fib_list = []
for i in range(N):
    if i == 0:
        fib_list.append(0)
    elif i == 1:
        fib_list.append(1)
    else:
        fib_list.append(fib_list[i - 1] + fib_list[i - 2])

# Requirement 4: Output the list to IDLE shell
print(f"The Fibonacci Sequence with {N} terms:")
print(fib_list)