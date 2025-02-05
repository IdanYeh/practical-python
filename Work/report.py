# report.py
#
# Exercise 2.4
# imports
import csv
import os.path
from pprint import pprint
import Work.pcost as wp
import Work.tableformat as tableformat
import Work.fileparse as fileparse
from Work.stock import Stock
from Work.portfolio import Portfolio

# functions
def read_portfolio(filename, **opts):
    '''
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares, and price.
    '''
    with open(filename) as lines:
        port = Portfolio.from_csv(lines)
    return port
def read_prices(filename):
    '''
    Read a CSV file of price data into a dict mapping names to prices.
    '''
    with open(filename) as lines:
        return dict(fileparse.parse_csv(lines, types=[str,float], has_headers=False))

def gain_loss(portfolio, prices):
    gainloss = {}
    for stock in portfolio:
        try:
            gainloss[stock['name']] = round(prices[stock['name']] - stock['price'], 2)
        except ValueError:
            print(f'The stock: {stock[0]} is not in the prices dictionary')
    return gainloss


def make_report_data(portfolio, gainloss):
    rows = []
    for s in portfolio:
        try:
            current_price = gainloss[s.name]
            change = current_price - s.price
            summary = (s.name, s.shares, current_price, change)
            rows.append(summary)
        except ValueError:
            print(f'The stock: {s.name} is not in the prices dictionary')
    return rows


def print_report(reportdata, formatter):
    '''
    Print a nicely formatted table from a list of (name, shares, price, change) tuples.
    '''
    formatter.headings(['Name','Shares','Price','Change'])
    for name, shares, price, change in reportdata:
        rowdata = [ name, str(shares), f'{price:0.2f}', f'{change:0.2f}' ]
        formatter.row(rowdata)


def portfolio_report(portfoliofile, pricefile, fmt='txt'):
    '''
    Make a stock report given portfolio and price data files.
    '''
    # Read data files
    portfolio = read_portfolio(portfoliofile, silence_errors=True)
    prices = read_prices(pricefile)

    # Create the report data
    report = make_report_data(portfolio, prices)

    # Print it out
    formatter = tableformat.create_formatter(fmt)
    print_report(report, formatter)

    return report

# commands

if __name__ == '__main__':
    folder_path = r'C:\Users\User\Desktop\Coding\Repositories\dabeaz-course\practical-python\Work\Data'
    portfolio_filename = f'{folder_path}\portfolio.csv'
    prices_filename = f'{folder_path}\prices.csv'
    wp.portfolio_cost(portfolio_filename)
    curr_report = portfolio_report(portfolio_filename, prices_filename)
    bla = 1
    portfolio = read_portfolio(os.path.join(folder_path, 'portfolio.csv'),  silence_errors=True)
    from Work.tableformat import create_formatter, print_table

    formatter = create_formatter('txt')
    print_table(portfolio, ['name', 'shares', 'price'], formatter)
    bla = 2
