"""Module for learning Abstract Base Classes in Python."""

from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract class representing a generic animal."""

    @abstractmethod
    def sound(self):
        """Abstract method that returns the sound of the animal."""
        pass


class Dog(Animal):
    """Subclass representing a dog, inheriting from Animal."""

    def sound(self):
        """Returns the specific sound of a dog."""
        return "Bark"


class Cat(Animal):
    """Subclass representing a cat, inheriting from Animal."""

    def sound(self):
        """Returns the specific sound of a cat."""
        return "Meow"
