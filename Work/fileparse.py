# fileparse.py
#
# Exercise 3.3
import csv


def parse_csv(filename, select=None, types=None, has_headers=False, delimiter=',', silence_errors=False):
    '''
    Parse a CSV file into a list of records
    '''
    with open(filename) as f:
        rows = csv.reader(f, delimiter=delimiter)
        if select is not None and has_headers==False:
            raise RuntimeError("select argument requires column headers")

        if has_headers==True:
            # Read the file headers
            headers = next(rows)
            if select is None:
                select = headers

            if types is None:
                types = [str]*len(headers)

            indices = [i for i, element in enumerate(headers) if element in select]
            headers = [headers[i] for i in indices]

            records = []
            for ii, row in enumerate(rows):
                if not row:    # Skip rows with no data
                    continue
                row = [row[i] for i in indices]
                if not silence_errors:
                    try:
                        row = [func(val) for func, val in zip(types, row)]
                    except ValueError as e:
                        print(f"Row {ii+1}: Couldn't covert {row} \nRow {ii+1}: Reason {e}")

                record = dict(zip(headers, row))
                records.append(record)
        else:
            records = []
            for row in rows:
                if not row:  # Skip rows with no data
                    continue
                record = tuple(row)
                records.append(record)

    return records


if __name__ == '__main__':
    folder_path = r'C:\Users\User\Desktop\Coding\Repositories\dabeaz-course\practical-python\Work\Data'
    portfolio_filename = f'{folder_path}\missing.csv'
    prices_filename = f'{folder_path}\prices.csv'

    portfolio = parse_csv(portfolio_filename, select=['name', 'shares', 'price'], types=[str, int, float], has_headers=True, delimiter=',', silence_errors=False)

    bla = 1
