"""Vehicle longitudinal dynamics model."""

import numpy as np
from typing import Tuple


class LongitudinalVehicleModel:
    """Model for vehicle longitudinal dynamics."""

    def __init__(self, mass: float, resistance_coeff: float = 0.015):
        """
        Initialize the vehicle model.

        Args:
            mass: Vehicle mass in kg
            resistance_coeff: Air resistance coefficient
        """
        self.mass = mass
        self.resistance_coeff = resistance_coeff
        self.g = 9.81  # Gravity acceleration

    def calculate_resistance_force(self, velocity: float) -> float:
        """
        Calculate resistance force at given velocity.

        Args:
            velocity: Vehicle velocity in m/s

        Returns:
            Resistance force in N
        """
        return self.resistance_coeff * velocity ** 2

    def calculate_acceleration(self, traction_force: float, velocity: float) -> float:
        """
        Calculate vehicle acceleration.

        Args:
            traction_force: Traction force in N
            velocity: Current velocity in m/s

        Returns:
            Acceleration in m/s^2
        """
        resistance = self.calculate_resistance_force(velocity)
        net_force = traction_force - resistance
        acceleration = net_force / self.mass
        return acceleration

    def simulate_step(self, velocity: float, traction_force: float, dt: float) -> Tuple[float, float]:
        """
        Simulate one time step of vehicle dynamics.

        Args:
            velocity: Current velocity in m/s
            traction_force: Applied traction force in N
            dt: Time step in seconds

        Returns:
            Tuple of (new_velocity, acceleration)
        """
        acceleration = self.calculate_acceleration(traction_force, velocity)
        new_velocity = velocity + acceleration * dt
        new_velocity = max(0, new_velocity)  # Velocity cannot be negative
        return new_velocity, acceleration
