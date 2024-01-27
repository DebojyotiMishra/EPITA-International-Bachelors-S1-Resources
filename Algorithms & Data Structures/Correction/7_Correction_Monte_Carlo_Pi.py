# PALISSON Antoine
import random
import matplotlib.pyplot as plt

## Monte Carlo Algorithm
def monte_carlo_pi(num_samples):
    inside_circle = 0

    for _ in range(num_samples):
        x, y = random.random(), random.random()
        distance = x**2 + y**2

        if distance <= 1:
            inside_circle += 1

    pi_estimate = 4 * inside_circle / num_samples
    return pi_estimate

print(monte_carlo_pi(1000000))

## Drawing the Figure
def plot_monte_carlo_pi(num_samples):
    x_inside = []
    y_inside = []
    x_outside = []
    y_outside = []

    for _ in range(num_samples):
        x, y = (2 * random.random() - 1), (2 * random.random() - 1)
        distance = x**2 + y**2

        if distance <= 1:
            x_inside.append(x)
            y_inside.append(y)
        else:
            x_outside.append(x)
            y_outside.append(y)

    pi_estimate = 4 * len(x_inside) / num_samples

    _, ax = plt.subplots()
    circle = plt.Circle((0, 0), 1, color='blue', fill=False)
    ax.add_artist(circle)
    plt.scatter(x_inside, y_inside, color='green', s=1)
    plt.scatter(x_outside, y_outside, color='red', s=1)
    plt.xlim(-1, 1)
    plt.ylim(-1, 1)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.title(f"Monte Carlo Pi Approximation with {num_samples} Samples")
    plt.figtext(0.5, 0.01, f"Pi Approximation: {pi_estimate:.6f}", ha="center", fontsize=14, color="black")
    plt.show()

plot_monte_carlo_pi(10000)