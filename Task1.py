import random

# Requirement 2 & 3: Input validation for N > 0
while True:
    N = int(input("Enter the number of times (N) to roll two dice: "))
    if N > 0:
        break
    print("Error: Please enter a positive integer greater than zero.")

# Requirement 4: Roll two dice N times and store sums in a list
dice_sums = []
for _ in range(N):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    dice_sums.append(dice1 + dice2)

# Requirement 5: Second loop to count number of 7s using indexing
count_sevens = 0
for i in range(len(dice_sums)):
    if dice_sums[i] == 7:
        count_sevens += 1

# Requirement 6: Output list and count
print("\n--- Results ---")
print("List of sums rolled:", dice_sums)
print("Number of times the sum was 7:", count_sevens)