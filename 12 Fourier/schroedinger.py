import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Physical constants in dimensionless units (\u03B7 = m = \hbar = 1)
# Spatial grid
def setup_grid(nx=512, x_max=5.0):
    x = np.linspace(-x_max, x_max, nx)
    dx = x[1] - x[0]
    k = 2 * np.pi * np.fft.fftfreq(nx, d=dx)
    return x, k, dx

# Potential: user-defined. Example: harmonic oscillator V(x) = 1/2 * x^2
def potential(x):
    return 0.5 * x**2

# Initial wavefunction: e.g., ground state gaussian\n# or arbitrary user-specified psi(x)
def initial_wavefunction(x):
    # Gaussian ground state of harmonic oscillator
    return (1/np.pi**0.25) * np.exp(-0.5 * x**2)

# Quantum leapfrog (split-operator) step
def leapfrog_step(psi, V, k, dt):
    # Half potential (kick)
    psi = np.exp(-1j * V * dt/2) * psi
    # Full kinetic (drift) via FFT
    psi_k = np.fft.fft(psi)
    psi_k = np.exp(-1j * (k**2)/2 * dt) * psi_k
    psi = np.fft.ifft(psi_k)
    # Half potential (kick)
    psi = np.exp(-1j * V * dt/2) * psi
    return psi

# Set up and run animation
def animate_wavefunction(x, k, V, psi0, dt=0.01, steps=500, interval=20):
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(6, 8))
    # Prepare psi and psi_hat
    psi = psi0.copy()
    Vx = V(x)

    # Set up lines
    line_real, = ax1.plot(x, psi.real, label='Re[\u03C8]')
    line_imag, = ax1.plot(x, psi.imag, label='Im[\u03C8]')
    ax1.set_xlim(x.min(), x.max())
    ax1.set_ylim(-1.1*np.max(np.abs(psi)), 1.1*np.max(np.abs(psi)))
    ax1.set_title('Wavefunction in position space')
    ax1.legend()

    psi_hat = np.fft.fft(psi)
    k_plot = np.fft.fftshift(k)
    line_pw, = ax2.plot(k_plot, np.fft.fftshift(np.abs(psi_hat)**2), label='|\u03C8(k)|^2')
    ax2.set_xlim(k_plot.min(), k_plot.max())
    ax2.set_ylim(0, 1.1*np.max(np.abs(psi_hat)**2))
    ax2.set_title('Momentum-space probability density')
    ax2.legend()

    def update(frame):
        nonlocal psi, psi_hat
        psi = leapfrog_step(psi, Vx, k, dt)
        psi_hat = np.fft.fft(psi)

        # Update position wavefunction plots
        line_real.set_ydata(psi.real)
        line_imag.set_ydata(psi.imag)
        # Update momentum probability
        pk = np.abs(psi_hat)**2
        line_pw.set_ydata(np.fft.fftshift(pk))
        return line_real, line_imag, line_pw

    ani = animation.FuncAnimation(
        fig, update, frames=steps, interval=interval, blit=True
    )
    plt.show()

if __name__ == '__main__':
    # Parameters
    x, k, dx = setup_grid(nx=512, x_max=5.0)
    psi0 = initial_wavefunction(x)
    # Normalize
    psi0 /= np.sqrt(np.sum(np.abs(psi0)**2) * dx)

    # Animate
    animate_wavefunction(x, k, potential, psi0, dt=0.01, steps=500, interval=20)
