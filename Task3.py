# Prompt user for emissivity (e) and surface area (A)
e = float(input("Enter emissivity of the object (0 to 1): "))
A = float(input("Enter surface area of the object (m^2): "))

sigma = 5.67e-8  # Stefan-Boltzmann constant

T_values = [290, 295, 300]          # Temperature of Object, T (K)
Tc_values = [288, 293, 298, 303]    # Temperature of Surroundings, Tc (K)

# Store results as a 2D list
pnet_table = []
for Tc in Tc_values:
    row = []
    for T in T_values:
        pnet = e * sigma * A * (T**4 - Tc**4)
        row.append(pnet)
    pnet_table.append(row)

# Output results one row at a time to IDLE shell
print("\nNet Radiation Loss, Pnet (W):")
print(f"{'Tc \\ T':<10}{'290':<14}{'295':<14}{'300':<14}")
print("-" * 52)

for i in range(len(Tc_values)):
    row_str = f"{Tc_values[i]:<10}"
    for j in range(len(T_values)):
        row_str += f"{pnet_table[i][j]:<14.4f}"
    print(row_str)