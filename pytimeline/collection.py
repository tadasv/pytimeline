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
            for doc in docs:
                if not isinstance(doc, DataPoint):
                    raise TypeError('docs_or_docs must a an instance or a list '
                                    'of DataPoint')
                new_docs.append(doc.to_dict())

            docs = new_docs
        else:
            raise TypeError('docs_or_docs must a an instance or a list of '
                            'DataPoint')

        return super(Collection, self).insert(docs, *args, **kwargs)


    def save(self, to_save, **kwargs):
        # TODO make manipulate work on DataPoint
        if not isinstance(to_save, DataPoint):
            raise TypeError("to_save must be an instance of DataPoint")

        if '_id' not in to_save:
            return self.insert(to_save, **kwargs)
        else:
            self.update({'_id' : to_save['_id']}, to_save, **kwargs)
            return to_save['_id']


    def update(self, spec, document, **kwargs):
        # TODO make manipulate work on DataPoint
        if not isinstance(document, DataPoint):
            raise TypeError("document must be an instance of DataPoint")

        return super(Collection, self).update(spec, document.to_dict(),
                                              **kwargs)
