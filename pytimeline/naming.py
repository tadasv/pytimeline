import datetime

def monthly_name(prefix, date):
    """
    Get a monthly name based on date.

    :Parameters:
      - `prefix`: prefix of the name.
      - `date`: :class:`datetime.date` or :class:`datetime.datetime` instance.

    """
    return '%s%d%02d' % (prefix, date.year, date.month)


def yearly_name(prefix, date):
    """
    Get a yearly name based on date.

    :Parameters:
      - `prefix`: prefix of the name.
      - `date`: :class:`datetime.date` or :class:`datetime.datetime` instance.

    """
    return '%s%d' % (prefix, date.year)


def daily_name(prefix, date):
    """
    Get a daily name based on date.

    :Parameters:
      - `prefix`: prefix of the name.
      - `date`: :class:`datetime.date` or :class:`datetime.datetime` instance.

    """
    return '%s%d%03d' % (prefix, date.year, date.timetuple().tm_yday)



class Generator(object):
    """
    Name generation interface. Other classes should subclass :class:`Generator`
    in order to implement custom database/collection name generators.

    """

    def __init__(self, prefix, start, end):
        """

        :Parameters:
          - `prefix`: name prefix.
          - `start`: start date; instance of :class:`datetime.date` or
            :class:`datetime.datetime`.
          - `end`: end date; instance of :class:`datetime.date` or
            :class:`datetime.datetime`.

        """

        assert(isinstance(start, datetime.date) or
               isinstance(start, datetime.datetime))
        assert(isinstance(end, datetime.date) or
               isinstance(end, datetime.datetime))
        assert(isinstance(prefix, str) or isinstance(prefix, unicode))

        self._start = start
        self._end = end
        self._prefix = prefix


    @staticmethod
    def get_name(prefix, date):
        """
        Method for getting a name based on the given prefix and date.
        This method must be implemented by subclasses.

        :Parameters:
          - `prefix`: name prefix
          - `date`: date; instance of :class:`datetime.date` or
            :class:`datetime.datetime`.

        """
        raise NotImplementedError


    @staticmethod
    def get_day_delta(date):
        """
        Method for getting the number of days that must be added
        to the `date` before generating another name. This method must be
        implemented bu subclasses.

        :Parameters:
          - `date`: date; instance of :class:`datetime.date` or
            :class:`datetime.datetime`.

        """
        raise NotImplementedError


    def generate_names(self):
        """
        Generator that generates names in [`start`, `end`] date range.

        """
        current_date = self._start
        while current_date <= self._end:
            yield self.__class__.get_name(self._prefix, current_date)
            current_date += datetime.timedelta(
                                days=self.__class__.get_day_delta(current_date))


    def get_list(self):
        """
        Return a list of names in [`start`, `end`] date range.

        """
        return list(self.generate_names())


class DailyGenerator(Generator):
    """
    Generator that generates daily names.

    """
    @staticmethod
    def get_name(prefix, date):
        return daily_name(prefix, date)


    @staticmethod
    def get_day_delta(date):
        return 1
