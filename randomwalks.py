import numpy as np
import matplotlib.pyplot as plt

def simulate_random_walk(dim, n_steps, n_walks):
    """
    Simulate random walks in given dimensions.
    
    Parameters:
    - dim: Number of dimensions (1, 2, or 3).
    - n_steps: Number of steps per walk.
    - n_walks: Number of random walks to simulate.
    
    Returns:
    - walks: A numpy array of shape (n_walks, n_steps, dim) representing the random walks.
    - return_counts: An array of shape (n_walks,) representing the number of returns to the origin for each walk.
    - return_probabilities: An array of shape (n_walks,) representing whether the walk returns to the origin at least once (1 for yes, 0 for no).
    """

    steps = np.random.choice([-1, 1], size=(n_walks, n_steps, dim))
    # Compute cumulative positions for all walks
    walks = np.cumsum(steps, axis=1)
    
    # Count the number of returns to the origin for each walk
    return_counts = np.array([np.sum(np.all(walks[i] == 0, axis=1)) for i in range(n_walks)])
    
    # Check whether each walk ever returns to the origin at least once
    return_probabilities = np.mean(np.array([1 if np.any(np.all(walks[i] == 0, axis=1)) else 0 for i in range(n_walks)]))
    
    return walks, return_counts, return_probabilities

def plot_random_walks(dim, walks, num_walks_to_plot=5):
    plt.figure(figsize=(8, 6))
    
    if dim == 1:
        for i in range(min(num_walks_to_plot, len(walks))):
            plt.plot(walks[i, :, 0], alpha=0.7)
        plt.xlabel("Steps")
        plt.ylabel("Position")
        plt.title("Plot of 5 1D Random Walks")
        plt.scatter(0, 0, color='red', zorder=5)  # Red dot at the origin
    
    elif dim == 2:
        for i in range(min(num_walks_to_plot, len(walks))):
            plt.plot(walks[i, :, 0], walks[i, :, 1], alpha=0.7)
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.title("Plot of 5 2D Random Walks")
        plt.scatter(0, 0, color='red', zorder=5)  # Red dot at the origin
    
    elif dim == 3:
        fig = plt.figure(figsize=(8, 6))
        ax = fig.add_subplot(111, projection='3d')
        for i in range(min(num_walks_to_plot, len(walks))):
            ax.plot(walks[i, :, 0], walks[i, :, 1], walks[i, :, 2], alpha=0.7)
        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.set_zlabel("Z")
        ax.set_title("Plot of 5 3D Random Walks")
        ax.scatter(0, 0, 0, color='red', zorder=5)  # Red dot at the origin

    plt.show()

def plot_return_distribution(return_counts_1d, return_counts_2d, return_counts_3d):
    plt.figure(figsize=(12, 6))

    plt.subplot(131)
    plt.hist(return_counts_1d, bins=range(0, np.max(return_counts_1d)+1), edgecolor='black', alpha=0.7)
    plt.title("1D Return Counts Distribution")
    plt.xlabel("Number of Returns to Origin")
    plt.ylabel("Frequency")
    
    plt.subplot(132)
    plt.hist(return_counts_2d, bins=range(0, np.max(return_counts_2d)+1), edgecolor='black', alpha=0.7)
    plt.title("2D Return Counts Distribution")
    plt.xlabel("Number of Returns to Origin")
    plt.ylabel("Frequency")
    
    plt.subplot(133)
    plt.hist(return_counts_3d, bins=range(0, np.max(return_counts_3d)+1), edgecolor='black', alpha=0.7)
    plt.title("3D Return Counts Distribution")
    plt.xlabel("Number of Returns to Origin")
    plt.ylabel("Frequency")
    
    plt.tight_layout()
    plt.show()