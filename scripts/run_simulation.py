#!/usr/bin/env python
"""Script to run vehicle simulations."""

import numpy as np
import matplotlib.pyplot as plt
from src.vehicle_model import LongitudinalVehicleModel


def simulate_acceleration(vehicle, traction_force, duration, dt=0.01):
    """
    Simulate vehicle acceleration.

    Args:
        vehicle: LongitudinalVehicleModel instance
        traction_force: Constant traction force in N
        duration: Simulation duration in seconds
        dt: Time step in seconds

    Returns:
        Tuple of (time, velocity, acceleration) arrays
    """
    t = np.arange(0, duration, dt)
    v = np.zeros_like(t)
    a = np.zeros_like(t)

    for i in range(1, len(t)):
        v[i], a[i] = vehicle.simulate_step(v[i - 1], traction_force, dt)

    return t, v, a


def plot_results(time, velocity, acceleration, title="Vehicle Simulation"):
    """
    Plot simulation results.

    Args:
        time: Time array
        velocity: Velocity array
        acceleration: Acceleration array
        title: Plot title
    """
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

    ax1.plot(time, velocity, "b-", linewidth=2)
    ax1.set_xlabel("Time (s)")
    ax1.set_ylabel("Velocity (m/s)")
    ax1.set_title(f"{title} - Velocity vs Time")
    ax1.grid(True, alpha=0.3)

    ax2.plot(time, acceleration, "r-", linewidth=2)
    ax2.set_xlabel("Time (s)")
    ax2.set_ylabel("Acceleration (m/s²)")
    ax2.set_title(f"{title} - Acceleration vs Time")
    ax2.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    # Create vehicle
    vehicle = LongitudinalVehicleModel(mass=1000)

    # Simulate constant acceleration
    print("Running acceleration simulation...")
    t, v, a = simulate_acceleration(vehicle, traction_force=5000, duration=20)

    print(f"Final velocity: {v[-1]:.2f} m/s")
    print(f"Simulation completed. Total time: {t[-1]:.2f} s")

    # Plot results
    plot_results(t, v, a, "Constant Acceleration")
