
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
