def Springs(K1, K2, Ftotal, config):
    # Check that K1, K2, and Ftotal are positive numbers
    if K1 <= 0 or K2 <= 0 or Ftotal <= 0:
        print("Error: K1, K2, and Ftotal must be positive numbers.")
        return None

    # Normalize the configuration string to lowercase to avoid case-sensitivity issues
    config = config.lower()

    if config == "series":
        # Equivalent spring constant for series: 1/Keq = 1/K1 + 1/K2
        Keq = 1 / ((1 / K1) + (1 / K2))
        
        # In series, force is equal across both springs
        F1 = Ftotal
        F2 = Ftotal
        
        # Calculate individual displacements using Hooke's Law (x = F / K)
        x1 = F1 / K1
        x2 = F2 / K2
        
        # Total displacement is the sum of individual displacements
        xtotal = x1 + x2
        
        return Keq, F1, F2, x1, x2, xtotal

    elif config == "parallel":
        # Equivalent spring constant for parallel: Keq = K1 + K2
        Keq = K1 + K2
        
        # In parallel, displacement is equal across both springs
        xtotal = Ftotal / Keq
        x1 = xtotal
        x2 = xtotal
        
        # Calculate individual forces using Hooke's Law (F = K * x)
        F1 = K1 * x1
        F2 = K2 * x2
        
        return Keq, F1, F2, x1, x2, xtotal

    else:
        # Handle invalid configuration strings
        print("Error: Configuration must be 'series' or 'parallel'.")
        return None 
