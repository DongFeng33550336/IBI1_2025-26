import numpy as np
import matplotlib.pyplot as plt


def run_spatial_SIR():
    """
    Run 2D spatial stochastic SIR model, neighbor-to-neighbor transmission
    :return: Saved grid states at key time points
    """
    # Model parameters
    grid_size = 100
    beta = 0.3  # Infection probability to neighbors
    gamma = 0.05  # Recovery probability
    max_time = 100

    # State definition: 0=Susceptible, 1=Infected, 2=Recovered
    # Initialize grid: all susceptible
    grid = np.zeros((grid_size, grid_size), dtype=int)
    # Random initial outbreak position
    outbreak_x, outbreak_y = np.random.choice(grid_size, 2)
    grid[outbreak_x, outbreak_y] = 1

    # 8 directions of neighbors
    neighbor_offsets = [(-1, -1), (-1, 0), (-1, 1),
                        (0, -1),          (0, 1),
                        (1, -1),  (1, 0), (1, 1)]

    # Save key time points to plot later
    key_time_points = [0, 10, 50, 100]
    saved_grids = {0: grid.copy()}

    for t in range(1, max_time + 1):
        # Use copy to avoid updating during the step
        new_grid = grid.copy()
        # Find all current infected cells
        infected_x, infected_y = np.where(grid == 1)

        for x, y in zip(infected_x, infected_y):
            # First check if current infected cell recovers
            if np.random.rand() < gamma:
                new_grid[x, y] = 2
                continue

            # If not recovered, try to infect neighbors
            for dx, dy in neighbor_offsets:
                nx, ny = x + dx, y + dy
                # Check if neighbor is inside the grid
                if 0 <= nx < grid_size and 0 <= ny < grid_size:
                    # Only susceptible can be infected
                    if grid[nx, ny] == 0:
                        if np.random.rand() < beta:
                            new_grid[nx, ny] = 1

        # Update grid for next step
        grid = new_grid

        # Save if it's a key time point
        if t in key_time_points:
            saved_grids[t] = grid.copy()

    return saved_grids


if __name__ == "__main__":
    print("Running spatial SIR simulation...")
    saved_states = run_spatial_SIR()
    print("Simulation complete, plotting propagation...")

    # Plot 2x2 subplots for different time points
    fig, axes = plt.subplots(2, 2, figsize=(6, 6), dpi=150)
    axes = axes.flatten()
    sorted_times = sorted(saved_states.keys())

    for i, t in enumerate(sorted_times):
        ax = axes[i]
        im = ax.imshow(
            saved_states[t], 
            cmap='viridis', 
            interpolation='nearest',
            vmin=0, vmax=2
        )
        ax.set_title(f'Time {t}', fontsize=9)
        ax.set_xticks([])
        ax.set_yticks([])

    # Add colorbar to explain the colors
    cbar = fig.colorbar(im, ax=axes, fraction=0.02)
    cbar.set_ticks([0, 1, 2])
    cbar.set_ticklabels(['Susceptible', 'Infected', 'Recovered'])

    plt.suptitle('Spatial SIR model propagation', fontsize=10)
    plt.tight_layout()
    plt.savefig('spatial_SIR_plot.png')
    plt.show()