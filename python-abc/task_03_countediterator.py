"""Module for tracking the number of items iterated over."""


class CountedIterator:
    """An iterator that counts how many items have been fetched."""

    def __init__(self, some_iterable):
        """Initialize the iterator and the counter."""
        self.iterator = iter(some_iterable)
        self.counter = 0

    def get_count(self):
        """Return the current value of the counter."""
        return self.counter

    def __next__(self):
        """Fetch the next item, increment the counter, and return the item."""
        try:
            item = next(self.iterator)
            self.counter += 1
            return item
        except StopIteration:
            raise StopIteration
