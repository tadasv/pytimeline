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


class DataPointIterator(object):
    def __init__(self, list_iterator, cast_to_dict=True):
        self._cast_to_dict= cast_to_dict
        self._list_iterator = list_iterator


    def __iter__(self):
        return self


    def next(self):
        item = self._list_iterator.next()
        if self._cast_to_dict:
            return item.to_dict()
        return item


class DataPointContainer(object):
    def __init__(self, cast_to_dict=True):
        self._container = []
        self._cast_to_dict = cast_to_dict

    def __len__(self):
        return len(self._container)


    def __iter__(self):
        return DataPointIterator(self._container.__iter__(),
                                 self._cast_to_dict)

    def __getitem__(self, key):
        item = self._container[key]
        if self._cast_to_dict:
            return item.to_dict()
        return item


    @classmethod
    def _assert_correct_data_type(cls, data):
        if not isinstance(data, DataPoint):
            raise TypeError('DataPoint instance expected')


    def append(self, data):
        self.__class__._assert_correct_data_type(data)
        return self._container.append(data)


    def insert(self, i, data):
        self.__class__._assert_correct_data_type(data)
        return self._container.insert(i, data)


    def clear(self):
        del self._container
        self._container = []


    def dict_generator(self):
        for item in self._container:
            yield item.to_dict()
