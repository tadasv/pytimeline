"""
Database level utilities for PyTimeline.
"""

from pymongo.database import Database as PymongoDatabase
from pytimeline.collection import Collection

class Database(PymongoDatabase):
    """
    A Mongo database.

    """

    def __getattr__(self, name):
        """
        Get a collection of this database.

        """
        return Collection(self, name)


    def create_collection(self, name, options=None, **kwargs):
        """
        Explicitly create a collection in this database.

        This method masks original method and raises
        :class:`NotImplementedError`.

        """
        raise NotImplementedError
