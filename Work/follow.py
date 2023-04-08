# follow.py
import os
import time


def follow(filename):
    f = open(filename)
    f.seek(0, os.SEEK_END)   # Move file pointer 0 bytes from end of file

    while True:
        line = f.readline()
        if line == '':
            time.sleep(0.1)   # Sleep briefly and retry
            continue
        yield line


def filematch(lines, substr):
    for line in lines:
        if substr in line:
            yield line


if __name__ == '__main__':
    from Work import report

    folder_path = r'C:\Users\User\Desktop\Coding\Repositories\dabeaz-course\practical-python\Work\Data'
    portfolio_filename = f'{folder_path}\portfolio.csv'
    stocks_filename = f'{folder_path}\stocklog.csv'

    portfolio = report.read_portfolio(portfolio_filename)
    for line in follow(stocks_filename):
        fields = line.split(',')
        name = fields[0].strip('"')
        price = float(fields[1])
        change = float(fields[4])
        if name in portfolio:
            print(f'{name:>10s} {price:>10.2f} {change:>10.2f}')

    # lines = follow(stocks_filename)
    # ibm = filematch(lines, 'IBM')
    # for line in ibm:
    #     print(line)