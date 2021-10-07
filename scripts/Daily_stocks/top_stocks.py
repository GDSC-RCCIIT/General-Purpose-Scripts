from tabulate import tabulate
import nsetools
from datetime import datetime as dt


def display_header(header):
    print("----------------------------------------------")
    print(header.center(40))
    print("----------------------------------------------")


def display_stocks(stock_dict):

    headers = ["Sl.", "SYMBOL", "CHANGE %"]
    stocks = [
        [i + 1, stock["symbol"], stock["netPrice"]]
        for i, stock in enumerate(stock_dict)
    ]
    print(tabulate(stocks, headers=headers))


def get_top_stocks():

    nse = nsetools.Nse()

    gainers = nse.get_top_gainers()
    losers = nse.get_top_losers()

    date = dt.now()

    display_header("TOP GAINERS")
    display_stocks(gainers)
    display_header("TOP LOSERS")
    display_stocks(losers)

    print("\nAs of", date.strftime("%H:%M:%S %b %d %Y"))


if __name__ == "__main__":
    get_top_stocks()
