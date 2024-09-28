import yfinance as yf
import os


def get_data(ticker_symbol, start_date, end_date):
    # Download the stock data
    stock_data = yf.download(ticker_symbol, start=start_date, end=end_date)

    # Save the stock data to a CSV file
    dataset_path = os.path.join('dataset', f'{ticker_symbol}-stock.csv')
    os.makedirs(os.path.dirname(dataset_path), exist_ok=True)
    stock_data.to_csv(dataset_path, index=False, header=True)

    return dataset_path

if __name__ == '__main__':
    # Define the ticker symbol for the stock
    ticker_symbol = 'TSLA'

    # Define the start and end dates for the stock data
    start_date = '2014-01-01'
    end_date = '2024-09-01'

    # Get the stock data
    dataset_path = get_data(ticker_symbol, start_date, end_date)

