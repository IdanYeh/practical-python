# report.py
#
# Exercise 2.4
# imports
import csv
import Work.pcost as wp
from pprint import pprint


# functions
def read_portfolio(filename):
    portfolio = []
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        header = next(rows)
        # print(header)
        for data in rows:
            record = dict(zip(header, data))
            try:
                holding = {'name': record['name'], 'shares': int(record['shares']), 'price': float(record['price'])}
                portfolio.append(holding)
            except ValueError:
                print('the following data line: ', data, ' is not compatible.\nline were skipped.')
    return portfolio


def read_prices(filename):
    stocks_dict = {}
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        # header = next(rows)
        # print(header)
        for data in rows:
            # data = line.replace('\n', '').split(',')
            # print(data)
            if len(data) < 1:
                continue
            try:
                stocks_dict[data[0]] = float(data[1])
            except ValueError:
                print('the following data line: ', data, ' is not compatible.\nline were skipped.')
    return stocks_dict


def gain_loss(portfolio, prices):
    gainloss = {}
    for stock in portfolio:
        try:
            gainloss[stock['name']] = round(prices[stock['name']] - stock['price'], 2)
        except ValueError:
            print(f'The stock: {stock[0]} is not in the prices dictionary')
    return gainloss


def make_report(portfolio, gainloss):
    report = []
    for stock in portfolio:
        try:
            temp = list(stock.values())
            temp.append(gainloss[stock['name']])
            report.append(tuple(temp))
        except ValueError:
            print(f'The stock: {stock[0]} is not in the prices dictionary')
    return report

def print_report(rep):
    headers = ('Name', 'Shares', 'Price', 'Change')
    print('%10s %10s %10s %10s' % headers)
    print('---------- ---------- ---------- -----------')
    [print('%10s %10d %10.2f %10.2f' % r) for r in rep]

def porfolio_report(portfolio_filename, prices_filename):
    curr_portfolio = read_portfolio(portfolio_filename)
    # pprint(curr_portfolio)
    price_dict = read_prices(prices_filename)
    # pprint(price_dict)
    gain_loss_dict = gain_loss(curr_portfolio, price_dict)
    # pprint(gain_loss_dict)
    report = make_report(curr_portfolio, gain_loss_dict)
    return report

# commands

if __name__ == '__main__':
    folder_path = r'C:\Users\User\Desktop\Coding\Repositories\dabeaz-course\practical-python\Work\Data'
    portfolio_filename = f'{folder_path}\portfolio.csv'
    prices_filename = f'{folder_path}\prices.csv'
    wp.portfolio_cost(portfolio_filename)
    curr_report = porfolio_report(portfolio_filename, prices_filename)
    print_report(curr_report)
    bla = 1
