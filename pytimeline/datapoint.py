import datetime

class IntegerDateTime(object):
    def __init__(self, *args):
        self._date = 0L

        if args:
            date_obj = datetime.datetime(*args)
            self.from_datetime(date_obj)

    @classmethod
    def today(cls):
        obj = cls()
        obj.from_datetime(datetime.datetime.today())
        return obj

    def __str__(self):
        return "<IntegerDate (%x)>" % self._date

    def __repr__(self):
        return str(self)

    def __int__(self):
        return int(self._date)

    def __long__(self):
        return long(self._date)

    def from_datetime(self, date_obj):
        self._date = 0L
        self._date += (date_obj.year & 0xfff) << 40
        self._date += (date_obj.month & 0xff) << 32
        self._date += (date_obj.day & 0xff) << 24
        self._date += (date_obj.hour & 0xff) << 16
        self._date += (date_obj.minute & 0xff) << 8
        self._date += (date_obj.second & 0xff)

    def to_datetime(self):
        date_obj = datetime.datetime(
                    (self._date >> 40) & 0xffff,
                    (self._date >> 32) & 0xff,
                    (self._date >> 24) & 0xff,
                    (self._date >> 16) & 0xff,
                    (self._date >> 8) & 0xff,
                    self._date & 0xff
                )
        return date_obj


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
            if not isinstance(value, IntegerDateTime):
                raise TypeError('expected instance of IntegerDateTime')
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
            new_dict['_dt'] = IntegerDateTime()

        new_dict['_dt'] = long(new_dict['_dt'])
        return new_dict

    def set_datetime(self, dt=None):
        if not dt:
            self.__setitem__('_dt', IntegerDateTime())
        else:
            self.__setitem__('_dt', dt)
