from pymongo.cursor import Cursor as PymongoCursor
from pytimeline.datapoint import DataPoint

class Cursor(PymongoCursor):
    """
    A cursor / iterator over MongoDB results.

    """
    def __init__(self, *args, **kwargs):
        self.__wrap = DataPoint
        if kwargs:
            self.__wrap = kwargs.pop('wrap', DataPoint)
        super(Cursor, self).__init__(*args, **kwargs)


    def __getitem__(self, index):
        obj = super(Cursor, self).__getitem__(index)
        if isinstance(obj, dict):
            return self.__wrap(obj)
        else:
            # A slice was taken therefore item is the same cursor
            # but with different options set.
            return obj


    def next(self):
        item = super(Cursor, self).next()
        return self.__wrap(item)
