from pandas import Series
import warnings
from utility import Utility
warnings.filterwarnings("ignore")


class DataManipulator:
    def __init__(self, data):
        self.df_data = data
        self.utility = Utility

    def data_transform(self):
        self.df_data[['date', 'year_month']] = self.df_data['date'].apply(
            lambda x: Series(self.utility.date_transform(x))
        )
        self.df_data[['discount_price', 'actual_price']] = self.df_data[['discount_price', 'actual_price']].applymap(
            self.utility.price_format)
        return self.df_data


