import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm


# Global model parameters
total_population = 10000
beta = 0.3
gamma = 0.05
max_time = 1000


def run_vaccination_model(vaccination_rate):
    """
    Run SIR model with specific vaccination rate
    :param vaccination_rate: Percentage of population vaccinated
    :return: History of infected count over time
    """
    # Initial state: vaccinated people are immune, cannot be infected
    vaccinated_count = int(total_population * vaccination_rate)
    # Remaining population: S + I + R
    S = total_population - vaccinated_count - 1  # Susceptible
    I = 1  # Initial infected
    R = 0  # Recovered

    I_history = []

    for _ in range(max_time):
        if I <= 0:
            I_history.append(0)
            continue

        # Calculate new infections and recoveries
        new_infected = np.random.binomial(S, beta * I / total_population) if S > 0 else 0
        new_recovered = np.random.binomial(I, gamma)

        # Update state
        S -= new_infected
        I += new_infected - new_recovered
        R += new_recovered

        I_history.append(I)

    # Pad to fixed length
    while len(I_history) < max_time:
        I_history.append(0)

    return I_history


if __name__ == "__main__":
    # Test vaccination rates from 0% to 100%, step 10%
    vaccination_rates = np.arange(0, 1.1, 0.1)
    colors = cm.viridis(np.linspace(0, 1, len(vaccination_rates)))

    plt.figure(figsize=(6, 4), dpi=150)

    for idx, rate in enumerate(vaccination_rates):
        print(f"Running simulation for vaccination rate: {int(rate*100)}%")
        infected_history = run_vaccination_model(rate)
        plt.plot(infected_history, color=colors[idx], label=f'{int(rate*100)}%')

    plt.xlabel('Time')
    plt.ylabel('Number of infected people')
    plt.title('SIR model with different vaccination rates')
    plt.legend(title='Vaccination rate', fontsize=8)
    plt.tight_layout()
    plt.savefig('SIR_vaccination_plot.png')
    plt.show()