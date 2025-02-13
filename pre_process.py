from pandas import DataFrame, ExcelWriter
from fetch_date import FetchTarget
from data_manipulation import DataManipulator


class PreProcess:
    def __init__(self):
        self.df_data = DataFrame()
        self.df_table_1 = DataFrame()
        self.df_table_2 = DataFrame()

    def fetch_data(self):
        data = FetchTarget()
        self.df_data = data.read_from_file()

    def data_manipulation(self):
        manipulation = DataManipulator(self.df_data)
        self.df_data = manipulation.data_transform()

    def tables(self):
        self.df_table_1 = self.df_data.groupby(by='year_month', as_index=False)[
            ['discount_price', 'actual_price']].sum()
        self.df_data['discount_percentage'] = (1 - (
                    self.df_data['discount_price'] / self.df_data['actual_price'])) * 100
        self.df_table_2 = round(self.df_data.groupby('year_month', as_index=False)['discount_percentage'].mean(), 2)

    def export_result(self):
        with ExcelWriter('export_result.xlsx', engine='xlsxwriter') as writer:
            self.df_table_1.to_excel(writer, sheet_name='Sales_summary', index=False)
            self.df_table_2.to_excel(writer, sheet_name='Discount_overview', index=False)

    def runner(self):
        self.fetch_data()
        self.data_manipulation()
        self.tables()
        self.export_result()
