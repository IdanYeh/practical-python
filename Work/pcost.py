# pcost.py
#
# Exercise 1.27
import csv
import sys
from Work import report


# functions
def portfolio_cost(filename):
    '''
    Computes the total cost (shares*price) of a portfolio file
    '''
    portfolio = report.read_portfolio(filename, silence_errors=True)
    return portfolio.total_cost


# Commands
if __name__ == '__main__':

    filename_main = 'Data/missing.csv'

    total_c = portfolio_cost(filename_main)


    if len(sys.argv) == 2:
        filename_main = sys.argv[1]
    else:
        filename_main = 'Data/portfolio.csv'

    # total_cost = portfolio_cost('Data/portfolio.csv')
    # print('Total cost', total_cost)

    total_c = portfolio_cost(filename_main)
    print('Total cost', total_c)

