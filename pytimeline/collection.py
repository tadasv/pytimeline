"""
Collection level utilities for PyTimeline.
"""

from pymongo.collection import Collection as PymongoCollection
from pytimeline.cursor import Cursor

class Collection(PymongoCollection):
    """
    A Mongo collection
    """

    def find(self, *args, **kwargs):
        """
        Query the database.

        Overrides the original method to use the custom
        :class:`~pytimeline.cursor.Cursor`.

        """
        return Cursor(self, *args, **kwargs)
