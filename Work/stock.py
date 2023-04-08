# stock.py

class Stock:
    '''
    An instance of a stock holding consisting of name, shares, and price.
    '''
    __slots__ = ('name', '_shares', 'price')
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @property
    def shares(self):
        return self._shares

    @shares.setter
    def shares(self, value):
        if not isinstance(value, int):
            raise TypeError('Expected int')
        self._shares = value

    def __repr__(self) -> str:
        return f"Stock({self.name}, {self.price}, {self.shares})"

    def cost(self):
        '''
        Return the cost as shares*price
        '''
        return self.shares * self.price

    def sell(self, nshares):
        '''
        Sell a number of shares
        '''
        self.shares -= nshares

