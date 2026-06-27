"""Module for extending the built-in list class with notifications."""


class VerboseList(list):
    """A custom list that prints notifications when items are added or removed."""

    def append(self, item):
        """Add an item to the end of the list and print a notification."""
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """Extend the list by appending elements from the iterable and notify."""
        initial_length = len(self)
        super().extend(iterable)
        items_added = len(self) - initial_length
        print(f"Extended the list with [{items_added}] items.")

    def remove(self, item):
        """Remove the first occurrence of an item and print a notification."""
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """Pop an item from the list at the given index and notify."""
        item = self[index]
        print(f"Popped [{item}] from the list.")
        return super().pop(index)
