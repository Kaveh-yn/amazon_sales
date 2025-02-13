from pandas import read_csv, DataFrame
import os
import warnings
from utility import BASE_DIR
warnings.filterwarnings("ignore")



class FetchTarget:
    def __init__(self):
        self.df_data = DataFrame()
        self.directory_path = f'{BASE_DIR}'
        self.file_name = f'Amazon-Products - online.csv'

    def read_from_file(self):
        """Read csv file locally."""
        self.df_data = read_csv(os.path.join(self.directory_path, self.file_name))
        self.df_data = self.df_data.dropna(how='all')
        return self.df_data
