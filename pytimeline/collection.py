"""
Collection level utilities for PyTimeline.
"""

from pymongo.collection import Collection as PymongoCollection
from pytimeline.cursor import Cursor
from pytimeline.datapoint import DataPoint

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


    def insert(self, doc_or_docs, *args, **kwargs):

        # TODO make manupulate work on DataPoint
        docs = doc_or_docs

        if isinstance(docs, DataPoint):
            docs = [docs.to_dict()]
        elif isinstance(docs, list):
            new_docs = []
            for x in docs:
                if not isinstance(x, DataPoint):
                    raise TypeError('docs_or_docs must a an instance or a list of DataPoint')
                new_docs.append(x.to_dict())

            docs = new_docs
        else:
            raise TypeError('docs_or_docs must a an instance or a list of DataPoint')

        return super(Collection, self).insert(docs, *args, **kwargs)
