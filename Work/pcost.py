# pcost.py
#
# Exercise 1.27
import csv
import sys


# functions
def portfolio_cost(filename):
    total_cost = 0
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        header = next(rows)
        # print(header)
        for ind, data in enumerate(rows):
            # data = line.replace('\n', '').split(',')
            # print(data)
            record = dict(zip(header, data))
            try:
                nshares = int(record['shares'])
                price = float(record['price'])
                total_cost += nshares * price
            except ValueError:
                print(f"Row {ind+1}: Couldn't convert: {data}")

    return total_cost


# Commands
filename = 'Data/missing.csv'

total_c = portfolio_cost(filename)


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

# total_cost = portfolio_cost('Data/portfolio.csv')
# print('Total cost', total_cost)

total_c = portfolio_cost(filename)
print('Total cost', total_c)

filename = 'Data/portfoliodate.csv'

total_c = portfolio_cost(filename)
print('Total cost', total_c)
