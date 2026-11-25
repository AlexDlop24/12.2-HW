def Springs(K1, K2, Ftotal, config):
    # Ensure K1, K2, and Ftotal are positive[cite: 1]
    if K1 <= 0 or K2 <= 0 or Ftotal <= 0:
        print("Error: Inputs must be positive numbers.")
        return

    config = config.lower()

    if config == "series":
        Keq = 1 / (1 / K1 + 1 / K2)  #[cite: 1]
        F1 = F2 = Ftotal  #[cite: 1]
        x1, x2 = F1 / K1, F2 / K2  #[cite: 1]
        xtotal = x1 + x2  #[cite: 1]
        return Keq, F1, F2, x1, x2, xtotal  #[cite: 1]

    elif config == "parallel":
        Keq = K1 + K2  #[cite: 1]
        x1 = x2 = xtotal = Ftotal / Keq  #[cite: 1]
        F1, F2 = K1 * x1, K2 * x2  #[cite: 1]
        return Keq, F1, F2, x1, x2, xtotal  #[cite: 1]

    else:
        print("Error: Configuration must be 'series' or 'parallel'.")
