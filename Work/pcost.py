# pcost.py
#
# Exercise 1.27

import csv
import sys
def portfolio_cost(filename):
    total_cost = 0
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        header = next(rows)
        # print(header)
        for data in rows:
            # data = line.replace('\n', '').split(',')
            # print(data)
            try:
                total_cost = total_cost + float(data[1])*float(data[2])
            except ValueError:
                print('the following data line: ', data, ' is not compatible.\nline were skipped.')

    return total_cost


filename = 'Data/missing.csv'

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

# total_cost = portfolio_cost('Data/portfolio.csv')
# print('Total cost', total_cost)

total_c = portfolio_cost(filename)
print('Total cost', total_c)


