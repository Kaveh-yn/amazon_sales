import jdatetime
from pandas import to_datetime
import os
BASE_DIR = os.path.dirname(os.path.realpath(__file__)).replace('\\', '/')


class Utility:
    @staticmethod
    def date_transform(x):
        """Convert a Gregorian date to Jalali date and extract year & month."""
        jalali_date = jdatetime.datetime.fromgregorian(datetime=to_datetime(x))
        return (
            f"{jalali_date.year}-{jalali_date.month:02d}-{jalali_date.day:02d}",
            f"{jalali_date.year} {jalali_date.j_months_fa[jalali_date.month-1]}"
        )
    
    @staticmethod
    def price_format(x):
        """Convert price from '₹32,999' format to float."""
        return float(str(x).replace('₹', '').replace(',', ''))