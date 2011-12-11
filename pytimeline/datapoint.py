import datetime

class DataPoint(object):
    def __init__(self, *args, **kwargs):
        self._data = {}

        if args:
            if len(args) > 1:
                raise TypeError('single argument expected')
            self._data = dict(args[0])

        if '_dt' not in self._data:
            self.set_datetime()
        else:
            self.set_datetime(self._data['_dt'])

    def __setitem__(self, name, value):
        if name == '_dt':
            if not isinstance(value, datetime.datetime):
                raise TypeError('expected instance of datetime.datetime')
            self._data[name] = value
            return
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
        new_dict = dict(self._data)
        if '_dt' not in new_dict:
            new_dict['_dt'] = datetime.datetime.today()

        return new_dict

    def set_datetime(self, dt=None):
        if not dt:
            self.__setitem__('_dt', datetime.datetime.today())
        else:
            self.__setitem__('_dt', dt)
