import numpy as np
import matplotlib.pyplot as plt


def run_basic_SIR():
    """
    Run the basic stochastic SIR model
    :return: History of S, I, R counts over time
    """
    # Model parameters as required
    total_population = 10000
    beta = 0.3  # Infection rate
    gamma = 0.05  # Recovery rate
    max_time = 1000

    # Initial state
    S = total_population - 1  # All susceptible except 1 initial infected
    I = 1  # Initial infected case
    R = 0  # No recovered at first

    # Track the evolution over time
    S_history = [S]
    I_history = [I]
    R_history = [R]

    # Simulation loop
    for _ in range(max_time):
        if I <= 0:
            # No more infected, stop early
            S_history.append(S)
            I_history.append(I)
            R_history.append(R)
            continue

        # Calculate new infections: each susceptible has probability beta * I/N to get infected
        new_infected = np.random.binomial(S, beta * I / total_population) if S > 0 else 0
        # Calculate new recoveries: each infected has probability gamma to recover
        new_recovered = np.random.binomial(I, gamma)

        # Update state
        S -= new_infected
        I += new_infected - new_recovered
        R += new_recovered

        # Record current state
        S_history.append(S)
        I_history.append(I)
        R_history.append(R)

    return S_history, I_history, R_history


if __name__ == "__main__":
    print("Running basic SIR model...")
    S, I, R = run_basic_SIR()
    print("Simulation complete, plotting results...")

    # Plot the result
    plt.figure(figsize=(6, 4), dpi=150)
    plt.plot(S, label='susceptible')
    plt.plot(I, label='infected')
    plt.plot(R, label='recovered')
    plt.xlabel('Time')
    plt.ylabel('Number of people')
    plt.title('SIR model')
    plt.legend()
    plt.tight_layout()
    plt.savefig('SIR_plot.png')
    plt.show()