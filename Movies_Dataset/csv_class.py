import pandas as pd
import seaborn as sns
import warnings


class CSV():

    def __init__(self,data):
        pd.set_option('display.max_columns', None)
        pd.set_option('display.max_rows', None)
        self.df = pd.read_csv(data)
