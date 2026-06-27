"""Module demonstrating the use of Mixins with SwimMixin, FlyMixin, and Dragon."""


class SwimMixin:
    """Mixin class providing swimming capability."""

    def swim(self):
        """Print swimming behavior."""
        print("The creature swims!")


class FlyMixin:
    """Mixin class providing flying capability."""

    def fly(self):
        """Print flying behavior."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Class representing a Dragon, mixing in swim and fly functionalities."""

    def roar(self):
        """Print the dragon's unique roaring behavior."""
        print("The dragon roars!")
