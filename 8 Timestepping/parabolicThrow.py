import numpy as np
import matplotlib.pyplot as plt

def leapfrogIntegration(x0, y0, vx0, vy0, tMax, dt=0.005):
    # Initial conditions
    t = 0
    positions = []
    times = []

    # Initial acceleration (gravity only in y)
    ax = 0
    ay = -9.81

    # Initialize velocity at half step
    vx_half = vx0  # no acceleration in x
    vy_half = vy0 + 0.5 * ay * dt

    # Initial positions
    x = x0
    y = y0

    while t <= tMax:
        positions.append((x, y))
        times.append(t)

        # Update positions with half-step velocities
        x += vx_half * dt
        y += vy_half * dt

        # Update velocities at full step (acceleration constant in this case)
        vx_half += ax * dt
        vy_half += ay * dt

        # Increment time
        t += dt

    print("End position:", tuple(map(lambda x: round(x, 5), positions[-1])))

    # Plotting the trajectory
    x_positions = [pos[0] for pos in positions]
    y_positions = [pos[1] for pos in positions]

    plt.figure(figsize=(10, 5))
    plt.plot(times, y_positions, label='Y Position vs Time')
    plt.plot(times, x_positions, label='X Position vs Time')
    plt.title("Position vs Time")
    plt.xlabel('Time (s)')
    plt.ylabel('Position (m)')
    plt.legend()
    plt.grid()
    plt.show()

    return positions[-1]

# Test run
leapfrogIntegration(0, 0, 9, 8, 3)