from datetime import date
from dateutil.relativedelta import relativedelta

import pandas as pd
import yfinance as yf

class Price:
    def __init__(self, symbol:str):
        df = yf.download(symbol, period="5y", progress=False)
        df.columns = df.columns.droplevel(1)
        df = df.reset_index()
        df["DateStr"] = df["Date"].dt.strftime("%Y-%m-%d")
        self.df = df

    def date_filter(self, date_start, date_end):
        df = self.df
        if date_start:
            df = df[df["Date"] >= date_start]
        if date_end:
            df = df[df["Date"] <= date_end]
        self.df = df
        return self.df

    def months_ago(self, months:int):
        date_start = pd.Timestamp(date.today() - relativedelta(months=months))
        date_end = pd.Timestamp(date.today())
        return self.date_filter(date_start, date_end)

def main():
    price = Price("AAPL")
    # print(price.df.dtypes)
    # price.date_filter("2021-01-01", "2021-03-31")
    df = price.months_ago(12)
    print(df)
    print(price.df)


if __name__ == "__main__":
    main()
