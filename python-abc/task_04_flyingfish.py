"""Module exploring multiple inheritance with Fish, Bird, and FlyingFish."""


class Fish:
    """Class representing a Fish with swim and habitat behaviors."""

    def swim(self):
        """Print fish swimming behavior."""
        print("The fish is swimming")

    def habitat(self):
        """Print fish habitat."""
        print("The fish lives in water")


class Bird:
    """Class representing a Bird with fly and habitat behaviors."""

    def fly(self):
        """Print bird flying behavior."""
        print("The bird is flying")

    def habitat(self):
        """Print bird habitat."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """Class representing a FlyingFish, inheriting from both Fish and Bird."""

    def fly(self):
        """Override the fly method for a flying fish."""
        print("The flying fish is soaring!")

    def swim(self):
        """Override the swim method for a flying fish."""
        print("The flying fish is swimming!")

    def habitat(self):
        """Override the habitat method for a flying fish."""
        print("The flying fish lives both in water and the sky!")
