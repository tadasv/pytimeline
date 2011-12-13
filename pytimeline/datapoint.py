"""
Document level related operations.
"""

import datetime

class DataPoint(object):
    """
    Document level abstaction.

    """

    def __init__(self, document=None, datetime_key='_dt'):
        """
        DataPoint constructor.

        :Parameters:
          - `document`: initial document state. `document` must be castable to
            `dict`.
          - `datetime_key`: place where the timestamp of the :class:`DataPoint`
            is located. This parameter can be a string or iterable of keys
            representing path to the timestamp.

            Example:

            If we have a document like this:

            .. doctest::

                >>> doc = {
                >>>    '_dt' : datetime.datetime.today() # <- timestamp
                >>> }

            Then `datetime_key` can either be `'_dt'`, `('_dt',)` or `['_dt']`.
            If we have a document where timestamp is nested:

            .. doctest::

                >>> doc = {
                >>>     '_id' : {
                >>>         '_dt' : datetime.datetime.today() # <- timestamp
                >>>     }
                >>> }

            Then `datetime_key` is iterable `('_id', '_dt')`.

        """
        self._data = {}
        self._datetime_key = datetime_key

        if document:
            self._data = dict(document)

        try:
            datetime_value = self._get_datetime_value()
            if not isinstance(datetime_value, datetime.datetime):
                raise TypeError('datetime value must be an instance of datetime.datetime')
        except KeyError:
            self._set_datetime_value(datetime.datetime.today())


    def _get_datetime_value(self):
        if isinstance(self._datetime_key, (str, unicode)):
            return self._data[self._datetime_key]
        elif isinstance(self._datetime_key, (list, tuple)):
            value = None
            for key in self._datetime_key:
                if value is None:
                    value = self._data[key]
                else:
                    value = value[key]

            return value

        raise TypeError("datetime key must be a string or iterable")


    def _set_datetime_value(self, value):
        if not isinstance(value, datetime.datetime):
            raise TypeError('datetime value must be an instance of datetime.datetime')

        if isinstance(self._datetime_key, (str, unicode)):
            self._data[self._datetime_key] = value
        elif isinstance(self._datetime_key, (list, tuple)):

            def __set_value(branch, keys, value):
                if len(keys) == 1:
                    branch[keys[0]] = value
                    return branch
                key = keys.pop(0)
                branch.update(__set_value(branch.setdefault(key, {}), keys, value))
                return branch

            self._data = __set_value(self._data, list(self._datetime_key), value)
        else:
            raise TypeError("datetime key must be a string or iterable")


    def __setitem__(self, name, value):
        self._data[name] = value

    def __getitem__(self, name):
        return self._data[name]

    def __delitem__(self, name):
        del self._data[name]

    def __contains__(self, name):
        return name in self._data

    def __str__(self):
        return "<DataPoint (%s)>" % str(self._data)

    def __repr__(self):
        return str(self)

    def to_dict(self):
        """
        Return :class:`DataPoint` converted to :class:`dict`.

        """
        try:
            datetime_value = self._get_datetime_value()
            if not isinstance(datetime_value, datetime.datetime):
                raise TypeError('datetime value must be an instance of datetime.datetime')
        except KeyError:
            self._set_datetime_value(datetime.datetime.today())

        return dict(self._data)


    def set_datetime(self, value=None):
        """
        Set timestamp for the DataPoint.

        :Parameters:
          - `value`: instance of datetime.datetime. If `value` is `None`,
            timestamp will be set to current time.

        """
        if not value:
            value = datetime.datetime.today()

        self._set_datetime_value(value)


    def datetime(self):
        """
        Get timestamp of the DataPoint.

        """
        return self._get_datetime_value()
