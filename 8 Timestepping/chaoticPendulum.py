import numpy as np
import matplotlib.pyplot as plt

def pendulumOnWheelLeapfrog(t_max, dt=0.005):
    # Physical parameters
    g = 9.81  # gravity (m/s^2)
    L = 0.03  # wheel radius (m)
    l = 0.4   # pendulum length (m)
    omega = 10  # wheel angular velocity (rad/s)

    # Dimensionless parameters (from task description)
    gamma = (g / l) / omega**2
    lam = L / l

    # Time variables
    t = 0
    tau = 0  # dimensionless time
    d_tau = omega * dt  # careful: dτ = Ω * dt

    # Initial conditions
    phi = -np.pi / 2  # pendulum angle (rad)
    phi_dot = 0.0    # initial angular velocity of pendulum

    # Initialize velocity at half step (Leapfrog)
    phi_dot_half = phi_dot + 0.5 * (-gamma * np.sin(phi) - lam * np.sin(phi - tau)) * d_tau

    # Data storage for plotting
    positions = []
    times = []

    # Integration loop
    while t <= t_max:
        # Store data
        theta = omega * t  # wheel angle
        mount_x = -L * np.sin(theta)
        mount_y = L * np.cos(theta)
        pendulum_x = mount_x + l * np.sin(phi)
        pendulum_y = mount_y - l * np.cos(phi)
        positions.append((pendulum_x, pendulum_y))
        times.append(t)

        # Step 1: update phi
        phi += phi_dot_half * d_tau

        # Update time
        t += dt / 2
        tau += d_tau / 2

        # Step 2: compute acceleration
        phi_ddot = -gamma * np.sin(phi) - lam * np.sin(phi - tau)

        # Step 3: update phi_dot at half-step
        phi_dot_half += phi_ddot * d_tau

        # Update time
        t += dt / 2
        tau += d_tau / 2

    # Plotting the trajectory
    x_positions = [pos[0] for pos in positions]
    y_positions = [pos[1] for pos in positions]
    times_normalized = (np.array(times) - min(times)) / (max(times) - min(times))

    plt.figure(figsize=(10, 5))
    scatter = plt.scatter(x_positions, y_positions, c=times_normalized, cmap='coolwarm', s=10)
    plt.colorbar(scatter, label='Time (normalized)')
    plt.title("Pendulum on a Wheel: Y vs X with Time as Color Gradient")
    plt.xlabel('X Position (m)')
    plt.ylabel('Y Position (m)')
    plt.grid()
    plt.show()

    print("Simulation completed.")

# Run the simulation
pendulumOnWheelLeapfrog(10)
