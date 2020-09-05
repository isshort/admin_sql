import time


def get_date(date):
    return time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(date / 1000.0))
