import requests
import pandas as pd

class StockPortfolio:
    def __init__(self, api_key):
        self.api_key = api_key
        self.portfolio = {}

    def add_stock(self, symbol, shares):
        if symbol in self.portfolio:
            self.portfolio[symbol]['shares'] += shares
        else:
            self.portfolio[symbol] = {'shares': shares, 'avg_price': self.get_stock_price(symbol)}

    def remove_stock(self, symbol, shares):
        if symbol in self.portfolio:
            if self.portfolio[symbol]['shares'] >= shares:
                self.portfolio[symbol]['shares'] -= shares
                if self.portfolio[symbol]['shares'] == 0:
                    del self.portfolio[symbol]
            else:
                print("Not enough shares to remove.")
        else:
            print("Stock not found in portfolio.")

    def get_stock_price(self, symbol):
        url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=1min&apikey={self.api_key}'
        response = requests.get(url)
        data = response.json()
        try:
            latest_close = list(data['Time Series (1min)'].values())[0]['4. close']
            return float(latest_close)
        except KeyError:
            print("Error retrieving data for symbol:", symbol)
            return None

    def track_performance(self):
        performance = {}
        for symbol, info in self.portfolio.items():
            current_price = self.get_stock_price(symbol)
            if current_price:
                performance[symbol] = {
                    'shares': info['shares'],
                    'avg_price': info['avg_price'],
                    'current_price': current_price,
                    'total_investment': info['shares'] * info['avg_price'],
                    'current_value': info['shares'] * current_price,
                    'profit_loss': (current_price - info['avg_price']) * info['shares']
                }
        return pd.DataFrame(performance).T


# Usage
api_key = 'YOUR_API_KEY'
portfolio = StockPortfolio(api_key)

# Add stocks
portfolio.add_stock('AAPL', 10)  # 10 shares of Apple
portfolio.add_stock('GOOGL', 5)   # 5 shares of Google

# Remove stocks
portfolio.remove_stock('AAPL', 2)  # Remove 2 shares of Apple

# Track performance
performance_df = portfolio.track_performance()
print(performance_df)