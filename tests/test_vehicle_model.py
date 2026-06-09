"""Tests for vehicle model."""

import pytest
from src.vehicle_model import LongitudinalVehicleModel


class TestLongitudinalVehicleModel:
    """Test suite for LongitudinalVehicleModel."""

    @pytest.fixture
    def vehicle(self):
        """Create a test vehicle instance."""
        return LongitudinalVehicleModel(mass=1000)

    def test_initialization(self, vehicle):
        """Test vehicle initialization."""
        assert vehicle.mass == 1000
        assert vehicle.resistance_coeff == 0.015
        assert vehicle.g == 9.81

    def test_calculate_resistance_force(self, vehicle):
        """Test resistance force calculation."""
        # At 0 velocity, resistance should be 0
        assert vehicle.calculate_resistance_force(0) == 0

        # At 10 m/s
        resistance = vehicle.calculate_resistance_force(10)
        expected = 0.015 * 100
        assert resistance == pytest.approx(expected)

    def test_calculate_acceleration(self, vehicle):
        """Test acceleration calculation."""
        # With 0 traction force and 0 velocity
        acceleration = vehicle.calculate_acceleration(0, 0)
        assert acceleration == 0

        # With 5000 N traction force
        acceleration = vehicle.calculate_acceleration(5000, 0)
        expected = 5000 / 1000
        assert acceleration == pytest.approx(expected)

    def test_simulate_step(self, vehicle):
        """Test simulation step."""
        # Starting from rest with 5000 N force for 1 second
        velocity, acceleration = vehicle.simulate_step(0, 5000, 1.0)
        assert acceleration == pytest.approx(5.0)
        assert velocity == pytest.approx(5.0)

    def test_velocity_cannot_be_negative(self, vehicle):
        """Test that velocity cannot go below zero."""
        velocity, _ = vehicle.simulate_step(1.0, -10000, 1.0)
        assert velocity >= 0
